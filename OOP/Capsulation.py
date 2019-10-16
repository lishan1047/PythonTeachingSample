"""
【面向对象】
1. 类、对象
2. 对象/类的属性、行为
3. 对象/类的关系：关联、继承、依赖
4. 特征：抽象性、封装性、多态性
"""
'''
First I will tell students what is Capsulational Definition of Class.
By the way, what is the enum data type will be introduced.

* Class code.
* Members of Class.
* Private members of Class.
* Public members of Class.
* Construct Method with parameters.
'''

from enum import Enum
class Gender(Enum):
    Male = 1
    Female = 2

class Person:
    __name = None
    __gender = Gender.Male
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender
    def GetName(self):
        return self.__name
    def GetGender(self):
        return self.__gender

p = Person('Liu', Gender.Male)

print('{0} is {1}'.format(p.GetName(), p.GetGender()))

'''
* Can we access p.__name or p.__gender ?
'''

p.__name = 'Zhang'
p.__gender = Gender.Female

print('{0} is {1}'.format(p.GetName(), p.GetGender()))
