#encoding: utf-8
#定义父类
class Parent:
    parentAttr=100
    def __init__(self):
        print "调用父类构造函数"
        
    def parentMethod(self):
        print "调用父类方法"
        
    def setAttr(self,attr):
        Parent.parentAttr=attr
        
    def getAttr(self):
        print "父类属性 :", Parent.parentAttr
        
#定义子类
class Child(Parent):
    def __init__(self):
        print "调用子类构造方法"
        
    def childMethod(self):
        print "调用子类方法"
        
c=Child()       # 实例化子类
c.childMethod() # 调用子类的方法
c.parentMethod()# 调用父类方法
c.setAttr(200)  # 再次调用父类的方法
c.getAttr()     # 再次调用父类的方法


#重载运算符，__str__功能
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)
   
    def __add__(self,other):
        return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print v1 + v2

#类的私有成员
#私有成员的定义方法：两个下划线开头，声明该方法为私有方法，不能在类地外部调用，在类的内部调用
class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0    # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print self.__secretCount

counter = JustCounter()
counter.count()
counter.count()
print counter.publicCount
#print counter.__secretCount  # 报错，实例不能访问私有变量