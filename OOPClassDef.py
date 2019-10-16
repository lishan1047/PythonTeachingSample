"""
【面向对象】
1. 类、对象
2. 对象/类的属性、行为
3. 对象/类的关系：关联、继承、依赖
4. 特征：抽象性、封装性、多态性
"""
'''
    Definition of Class.
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
    def getName(self):
        return self.__name
    def getGender(self):
        return self.__gender

p = Person('Liu', Gender.Male)
print('{0} is a {1} person.'.format(p.getName(), p.getGender().name))
