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
    """
    创建类的实例,并调用类的方法
    """
    s = student('Ken', 10, 60, 3)
    s.speak()
    
    print("main module end")