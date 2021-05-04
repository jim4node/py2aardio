# -*- coding: utf-8 -*-
#         在此前提下，对本软件的使用同样需要遵守 Apache 2.0 许可。
    # 开始测试
test = 1 #
a = '#1'    #test2
b = "#2"
c = '汉字'
names = ["zhao", "钱", "sun", "李"]   # 数组
"""
测试写成多行的列表,元组和字典
"""
colors = [
    "黑",
    "白",
    "红"
]
#元组
tup = (
    1,
    2,
    3
)
#字典
dict = {
    'john': 'boy',
    'lily': 'girl'
}

# 函数的参数写成多行
do_some_thing(
    p1='a',
    p2='b',
    p3='c'
)

from functools import wraps
from rq.core.events import EVENT, Event
from rq.utils.logger import user_system_log

#---------父类 Test-----------#
class Test(object):
    # 构造函数
    def __init__(self):
        self.a = 0
    # 不规范的注释缩进
#----------------------
        self.b = 0
        # -很长的语句,多行
        if ((maxp-current_price)/current_price)*100>1 \
            or sum(hi['volume'])<0.5*hiday['volume'] \
            or 100*(current_price-sum(hi['money'])/sum(hi['volume']))/hiday['close']>2:
            g.security.remove(stock)
            

#--------子类 ChildTest--------
class ChildTest(Test):
    def __init__(self):
        self.b = 1

#--------孙类 SubChildTest, 继承自多个类--------
class SubChildTest(Test, ChildTest):
    def __init__(self):
        self.c = 2
       self.d=4 # 不规范的缩进3
         self.e=5 # 不规则的缩进5


"""
# 运行策略
# @param func
# @return wrapper
"""
def run_when_strategy_not_hold(func):
    # test begin 
    if True:
        a = 1
    elif False :
        a = 0
    else:
        a = 2
    
    try:
        a = 1 + w
    except e:
        # 不带 as 的异常
        print(e)
        pass
    except Exception as e:
        # 带 as 的异常
        print('Exception error')
    finally:
        print('ok')
    # end test
    
    from utils.logger import system_log
    def wrapper(*args, **kwargs):
        if not Environment.get_instance().config:
            return func(*args, **kwargs)
        else:
            system_log.debug(_(u"not run {}({}, {}) because strategy is #hold#").format(func, args, kwargs))

    return wrapper

def fun_try():
    try:
        print('try--start')
        a = 1/0
    except:
        print 'normal except'
    except Exception:
        print 'Exception'
    except ValueError as e:
        print('ValueError')
    finally:
        return 'finally'
 
print(fun_try())

# 类
class Strategy(object):
    def __init__(self, event_bus, scope, ucontext):
        # 类的属性和方法
        self._user_context = ucontext
        self._current_universe = set()

        self._init = scope.get('init', None)
        self._handle_bar = scope.get(
            'handle_bar', None
            )

        if func_before_trading is not None and func_before_trading.__code__.co_argcount > 1:
            self._before_trading = lambda context: func_before_trading(context, None)
            user_system_log.warn(_(u"deprecated parameter[bar_dict] in '%s' function." % ('before_trading')))
        else:
            self._before_trading = func_before_trading
        self._after_trading = scope.get('after_trading', None)

        if self._open_auction is not None:
            event_bus.add_listener(
                EVENT.OPEN_AUCTION, 
                self.open_auction
            )

    @property
    def user_context(self):
        return self._user_context

    def init(self):
        if self._init:
            # with 语句, 没法转换:(
            with ExecutionContext(EXECUTION_PHASE.ON_INIT):
                with ModifyExceptionFromType(EXC_TYPE.USER_EXC):
                    self._init(self._user_context)
        
        # 分为多行的函数参数
        event_bus.publish_event(
            Event(EVENT.POST_USER_INIT),
            True
        )


