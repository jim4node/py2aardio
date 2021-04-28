# Py2Aardio 转换助手
这是一个将 Python 语言源文件转换为 Aardio 语言源文件的辅助工具, 主要功能是进行源代码格式转化()的前期工作, 可较大程度地减少开发者的劳动强度. 
目前, 本工具只进行了源代码格式转换和部分关键字的替换, 并未进行语言语义层面的翻译. 所以:
## 作者不保证源代码的格式转换完全正确, 也不保证生成的 Aardio 源代码能正确运行, 开发者仍需对生成的源代码进行手工修改!

### 样例
Python 源代码:
```python
#!/usr/bin/python3
 
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
        self.grade = g
    #覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))
 
print "This is a demo class"
"""
创建类的实例,并调用类的方法
"""
s = student('ken', 10, 60, 3)
s.speak()
```
转换为 Aardio 源代码:
```js
//!/usr/bin/python3

//类定义
class people {
    //定义基本属性
    name = '';
    age = 0;
    //定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0;
    //定义构造方法
    ctor(n,a,w) {
        this.name = n;
        this.age = a;
        this.__weight = w;
    }
    speak = function() {
        print(string.format("%s 说: 我 %d 岁。", this.name,this.age));
    }
}

//单继承示例
class student {
    this = people(...);// 继承的父类 <--请把这行移入类的构造函数 ctor 内! {
    grade = '';
    ctor(n,a,w,g) {
        //调用父类的构函
        people.__init__(this,n,a,w);
        this.grade = g;
    }
    //覆写父类的方法
    speak = function() {
        print(string.format("%s 说: 我 %d 岁了，我在读 %d 年级", this.name,this.age,this.grade));
    }
}

print "This is a demo class";
/*
创建类的实例,并调用类的方法
*/
s = student('ken', 10, 60, 3);
s.speak();
```

### 更新记录:
1. 2021-04-28 v0.9 初始版本发布: 基本实现源代码格式转化和关键字替换
 
### TODO 待办事宜
1.Python 语言的列表推导式转换
2.Python 语言的多行列表[]的转换(目前转换较混乱)
3.行尾分号的精确添加到句尾(需考虑行尾带注释的情况)
4.Python 语言的 finally 语句处理
5.Python 语言的 except as 语句处理
6.其它

### 建议和改进
1. github 提 issue
2. 欢迎 fork and pull request
3. 发送邮件到 jimone@qq.com




