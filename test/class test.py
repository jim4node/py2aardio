#!/usr/bin/python3
import util.Parser as parser
from pandas import DataFrame

#类定义
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        assert a > 0, "年龄不能是负数"
        assert n > '', '姓名不能为空'
        assert w > 0    # 没有错误信息
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))
 
#单继承示例
class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        #调用父类的构函
        people.__init__(self,n,a,w)
        assert g > 0
        self.grade = g  # 子类的新增成员: 年级
    #覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))
    #带有类型注解的函数声明
    def age(self, b:bool, c:pd.UInt_16) -> int:
        # do something...
        return self.age
        
if __name__ == "__main__":
    print("单元测试(Unit Test) in main module")
    # 测试 del 语句
    a = 0
    b = 1
    try:
        del a   # 删除变量
        del b
        del a_df["file"]   # 删除元素
        del df[2]
    except e:
        print(e)
        
    """
    创建类的实例,并调用类的方法
    """
    s = student('Ken', 10, 60, 3)
    s.speak()
    # 测试 getattr, setattr, hasattr
    n = getattr(s, 'name')  # 不带默认属性
    n = getattr(s, 'name', 'default')  # 带默认属性
    n = getattr(s, 'name', '(test)')   # 带默认属性
    getattr(s, "age", setattr(s, "age", 18)) # 若age属性不存在，则设置该属性
    ag = 'age'
    if hasattr(s, ag):
        setattr(s, ag, 20)
    
    print("main module end")