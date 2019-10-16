"""
【面向对象】
1. 类、对象
2. 对象/类的属性、行为
3. 对象/类的关系：关联、继承、依赖
4. 特征：抽象性、封装性、多态性
"""

'''
In this sample, I will show the basic features to students.
* What is the Class.
* What is the Object.
* What is the Property.
* What is the Behavious.
* What is the Construct Method.
* What is the Abstract Method.
* What is the Capsulation.
* What is the Inheritance.
* What is the Polymorphism.
'''

import abc

class Person(metaclass=abc.ABCMeta):
    def __init__(self, name):
        self.Name = name
    @abc.abstractmethod
    def SayHello(self):
        '''
        '''

class Chinese(Person):
    def __init__(self, name):
        Person.__init__(self, name)
    def SayHello(self):
        print('{0}，你好！'.format(self.Name))

class American(Person):
    def __init__(self, name):
        Person.__init__(self, name)
    def SayHello(self):
        print('Hello {0}!'.format(self.Name))

p = Chinese('张三')
p.SayHello()

p = American('Zhangsan')
p.SayHello()


