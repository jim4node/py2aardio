"""
Python版冰山委托-买入策略_K线骑士-CSDN博客
https://blog.csdn.net/qq_25863231/article/details/104968893
"""
import random  # 导入随机数库

def CancelPendingOrders():     # CancelPendingOrders 函数作用是取消当前交易对所有挂单。
    while True:                # 循环检测，调用GetOrders 函数，检测当前挂单，如果orders 为空数组，即len(orders) 等于0，说明订单全部取消了，可以退出函数，调用return 退出。
        orders = _C(exchange.GetOrders)
        if len(orders) == 0:
            return 

        for j in range(len(orders)):     # 遍历当前挂单数组，调用取消订单的函数CancelOrder,逐个取消挂单。
            exchange.CancelOrder(orders[j]["Id"])
            if j < len(orders) - 1:      # 除了最后一个订单，每次都执行Sleep 让程序等待一会儿，避免撤单过于频繁。
                Sleep(Interval)

LastBuyPrice = 0       # 设置一个全局变量，记录最近一次买入的价格。
InitAccount = None     # 设置一个全局变量，记录初始账户资产信息。

def dispatch():        # 冰山委托逻辑的主要函数
    global InitAccount, LastBuyPrice     # 引用全局变量
    account = None                       # 声明一个变量，记录实时获取的账户信息，用于对比计算。
    ticker = _C(exchange.GetTicker)      # 声明一个变量，记录最近行情。
    LogStatus(_D(), "ticker:", ticker)   # 在状态栏输出时间，最新行情
    if LastBuyPrice > 0:                 # 当LastBuyPrice大于0时，即已经委托开始时，执行if条件内代码。
        if len(_C(exchange.GetOrders)) >  0:    # 调用exchange.GetOrders 函数获取当前所有挂单，判断有挂单，执行if条件内代码。
            if ticker["Last"] > LastBuyPrice  and ((ticker["Last"] - LastBuyPrice) / LastBuyPrice) > (2 * (EntrustDepth / 100)):  # 检测偏离程度，如果触发该条件，执行if内代码，撤单。
                Log("偏离过多, 最新成交价:", ticker["Last"], "委托价", LastBuyPrice)
                CancelPendingOrders()
            else:
                return True
        else:     # 如果没有挂单，证明订单完全成交了。
            account = _C(exchange.GetAccount)     # 获取当前账户资产信息。
            Log("买单完成, 累计花费:", _N(InitAccount["Balance"] - account["Balance"]), "平均买入价", _N((InitAccount["Balance"] - account["Balance"]) / (account["Stocks"] - InitAccount["Stocks"])))  # 打印交易信息。
        LastBuyPrice = 0   # 重置 LastBuyPrice为0

    BuyPrice = _N(ticker["Buy"] * (1 - EntrustDepth / 100))   # 通过当前行情和参数，计算挂单价格。
    if BuyPrice > MaxBuyPrice:    # 判断是否超过参数设置的最大价格
        return True

    if not account:               # 如果 account 为 null ,执行if 语句内代码，重新获取当前资产信息，复制给account
        account = _C(exchange.GetAccount)

    if (InitAccount["Balance"] - account["Balance"]) >= TotalBuyNet:  # 判断买入所花费的总钱数，是不是超过参数设置。
        return False

    RandomAvgBuyOnce = (AvgBuyOnce * ((100.0 - FloatPoint) / 100.0)) + (((FloatPoint * 2) / 100.0) * AvgBuyOnce * random.random())   # 随机数 0~1
    UsedMoney = min(account["Balance"], RandomAvgBuyOnce, TotalBuyNet - (InitAccount["Balance"] - account["Balance"]))

    BuyAmount = _N(UsedMoney / BuyPrice)   # 计算买入数量
    if BuyAmount < MinStock:         # 判断买入数量是否小于 参数上最小买入量限制。
        return False 
    LastBuyPrice = BuyPrice          # 记录本次下单价格，赋值给LastBuyPrice
    exchange.Buy(BuyPrice, BuyAmount, "花费：￥", _N(UsedMoney), "上次成交价", ticker["Last"]) # 下单
    return True

def main():
    global LoopInterval, InitAccount    # 引用 LoopInterval, InitAccount 全局变量
    CancelPendingOrders()               # 开始运行时，取消所有挂单
    InitAccount = _C(exchange.GetAccount)   # 初始记录 开始时的账户资产
    Log(InitAccount)                        # 打印初始账户信息
    if InitAccount["Balance"] < TotalBuyNet:    # 如果初始时资产不足，则抛出错误，停止程序
        raise Exception("账户余额不足")
    LoopInterval = max(LoopInterval, 1)      # 设置LoopInterval至少为1
    while dispatch():                        # 主要循环，不停调用 冰山委托逻辑函数 dispatch ，当dispatch函数 return false 时才停止循环。
        Sleep(LoopInterval * 1000)           # 每次循环都暂停一下，控制轮询频率。
    Log("委托全部完成", _C(exchange.GetAccount))   # 当循环执行跳出时，打印当前账户资产信息。
