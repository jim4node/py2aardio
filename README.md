# Py2Aardio 转换助手(python to [aardio](http://www.aardio.com) conversion helper)
这是一个将 Python 语言源文件转换为 [aardio](http://www.aardio.com) 语言源文件的辅助工具, 主要功能是进行源代码格式转换的前期工作, 可较大程度地减少开发者的劳动强度. 
目前, 本工具只转换源代码格式(将缩进转为缩进+花括号)和替换部分关键字, 并未实现语言语义和功能层面的精准翻译. 所以:
#### 不保证源代码的格式转换完全正确, 也不保证生成的 aardio 源代码能正确运行! 开发者仍需对生成的源代码进行必要的手工修改!
------
本工具主要使用了 aardio 语言的模式匹配(pattern)和字符串替换(string.replace)功能, 能给初学者提供一定的参考.
> Python 和 aardio 语言的语法比较, 可参阅 aardio IDE 内置的[代码段]-[范例程序]-[Python 语言]-[py,aardio语法比较]下的各篇介绍
    
### 特性
1. 支持单个 python 源文件转换, 转换后在 Edit 窗口中即时产生目标 aardio 代码
2. 支持文件夹转换, 可批量转换文件夹内所有 python 源文件
3. 转换后将在 python 源文件的同一目录内, 生成同名 .aardio 源文件
4. 提供"复制其它格式文件"选项, 方便进行项目的整体转换 
5. 提供: 行尾加分号, 下划线形式的变量名转换为驼峰式, 多级文件夹等转换选项
6. 自动识别写成多行的 python 注释,列表[],元组(),字典{}和函数参数()等格式

### 样例
本助手能将所示 Python 源代码:
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
```
转换为如下所示 aardio 源代码:
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
        this.grade = g;  // 子类的新增成员: 年级
    }
    //覆写父类的方法
    speak = function() {
        print(string.format("%s 说: 我 %d 岁了，我在读 %d 年级", this.name,this.age,this.grade));
    }
    //带有类型注解的函数声明
    age = function(b/*:bool*/, c/*:pd.UInt_16*/)/*-> int*/ {
        // do something...
        return this.age;
    }
}

if (owner == null) {
    print("单元测试(Unit Test) in main module");
    /*
    创建类的实例,并调用类的方法
    */
    s = student('Ken', 10, 60, 3);
    s.speak();

    print("main module end");
}
```

### 更新记录:
1. 2021-04-28 v0.9  初始版本发布: 基本实现源代码格式转化和关键字替换
2. 2021-04-30 v1.0  版本发布, 增加对写成多行的列表[],元组(),字典{}和函数参数()等的支持
3. 2021-05-01 v1.1  新增: 转换 except 和 finally;
                    完善: 替换保留字和加括号的欠缺;
                    修复: 'pass' 转换的 bug; 
                    修复: 单个文件转换时不保存目标文件的 bug;
                    其它: 细节优化
4. 2021-05-02 v1.2  新增: 按钮弹出菜单选择单个文件或文件夹
5. 2021-05-04 v1.3  修复和优化
6. 2021-05-06 v1.4  新增: 选项:复制其它非'.py'格式文件, 以便进行项目的整体转换
7. 2021-05-07 v1.5  新增: 替换全局性的特定词句(例如: name == main)
8. 2021-05-07 v1.6  新增: 支持带类型注解的函数声明
9. 2021-05-07 v1.6.1 新增: 保留字 print 和导入别名(import as)
10. 2021-05-07 v1.6.2 新增: 转换保留字 assert
11. 2021-05-07 v1.6.3 新增: 行尾注释先去除再恢复; 新增转换保留字 del; 修复若干 bugs
12. 2021-05-07 v1.6.4 新增: 转换对象属性相关方法 hasattr, getattr, setattr; 界面上增加"文件名改驼峰式"
13. 2021-05-08 v1.6.5 新增:实现文件名驼峰化选项;非py文件提示确认
14. 2021-05-09 v1.7 优化:改用Win7以上的新版[选择文件夹]对话框; 废弃core.pad改用string.repeat; 修复:去除行尾注释时的bug
15. 2021-05-09 v1.8 新增:转换过程进度和文件数量的提示
16. 2021-05-10 v1.8.1 新增: 显示转换过程状态(是否已完成)
17. 2021-05-11 v1.8.2 修复: 转换导入(from . import)时的bug

### TODO 待办事宜
1. Python 语言的列表推导式转换
2. ~~Python 语言的多行列表[]的转换(目前转换较混乱)~~ 已完成√
3. ~~行尾分号的精确添加到句尾(需考虑行尾带注释的情况)~~ 已完成√
4. ~~Python 语言的 finally 语句处理~~ 已完成√
5. ~~Python 语言的 except as 语句处理~~ 已完成√
6. Python 语言的 class 内部私有变量的处理
7. 保存历史文件/项目到配置文件

### 建议和改进
1. github 提 issue
2. 欢迎 fork and pull request
3. 发送邮件到 jimone@qq.com




