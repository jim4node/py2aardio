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

# 测试u字符串和多行字符串
a = ("1..."
    "2..."
    "3...")
b = ('a...'
    'b...'
    'c...')
    
c = (u"c1..."
    u"c2..."
    u"c3...")
d = (u'd1...'
    u'd2...'
    u'd3...')
print(_(u"1.There is no data between {start_date} and {end_date}. Please check your"
                  u" data bundle or select other date period.").format(
                    start_date, end_date))
print(('2.There is no data between {start_date} and {end_date}. Please check your'
                  ' data bundle or select other date period.').format(s, e))
# 测试字符串重复拼接
s = "a" * 10
 
# 函数的参数写成多行
do_some_thing(
    p1='a',
    p2='b',
    p3='c'
)
# 测试部分函数替换
sourceDir = os.path.join(os.path.dirname(__file__), "test")
destPath = os.path.abspath(os.path.join(dir, "test"))
a = isinstance(obj, AClassType)
b = isinstance(ids, six.string_types)
c = isinstance(num, six.integer_types)

# 测试 import
from functools import wraps
from rq.core.events import EVENT, Event
from rq.utils.logger import user_system_log
from rq.core.events import Event as evt, EVENT as EVT   # 测试
from rq.utils.exception import (
    patch_user_exc,
    patch_system_exc,
    EXC_EXT_NAME,
    InvalidArgument,
)

#---------父类 Test-----------#
class Test(object):     # 继承自object
    # 构造函数
    def __init__(self):
        self.a = 0
    # 不规范的注释缩进
#----------------------
        self.b = 0
        
    def stock(self):    # 任意成员函数
        # -很长的语句,多行, 用反斜杠断行
        if ((maxp-price)/price)*100>1 \
            or sum(hi['volume'])<0.5*hiday['volume'] \
            or 100*(price-sum(hi['money'])/sum(hi['volume']))/hiday['close']>2:
            remove(stock)
        # 测试:很长的语句,写成多行, 不带反斜杠
        if ((maxp-price)/price)*100>1 or
            sum(hi['volume'])<0.5*hiday['volume'] or
            100*(price-sum(hi['money'])/sum(hi['volume']))/hiday['close']>2:
            remove(stock)
        elif sum(lo['volume'])>0.3*loday['volume'] or
            100*(price-sum(lo['money'])/sum(lo['volume']))/loday['close']>3:
            add(stock)

#--------子类 ChildTest--------
class ChildTest(Test):  # 继承自父类 Test
    def __init__(self): # 构造函数
        self.b = 1

#--------孙类 SubChildTest, 继承自多个类--------
class SubChildTest(Test, ChildTest): # 继承自两个父类
    def __init__(self): # 构造函数
        self.c = 2
       self.d=4 # 不规范的缩进3
         self.e=5 # 不规则的缩进5


"""
# 运行策略
# @param func
# @return wrapper
"""
def run_hold(func): # 独立测试函数
    # test begin 
    if True:        # 仅供测试
        a = 1
    elif False :    # 并无意义
        a = 0
    else:
        a = 2
    
    try:            # 测试try...except
        a = 1 + w
    except e:       # 不带 as 的异常
        print(e)
        pass
    except Exception as e:  # 带 as 的异常       
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

def fun_try():  # 测试用的函数
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
        self._pe = POS_EFFECT[d["pos_effect"]] if d["pos_effect"] else None
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
    def user_context(self): # 属性方法
        return self._user_context

    def init(self):
        if self._init:
            # with 语句, 没法转换
            with ExecutionContext(EXECUTION_PHASE.ON_INIT):
                with ModifyExceptionFromType(EXC_TYPE.USER_EXC):
                    self._init(self._user_context)
        
        # 分为多行的函数参数
        event_bus.publish_event(
            Event(EVENT.POST_USER_INIT),
            True
        )


