'''
This is basic definition of class.

* Class.
* Field.
* Method.

'''

class Person:
    Name = None
    Gender = None
    def __init__(self):
        pass
    def GetName(self):
        return self.Name
    def GetGender(self):
        return self.Gender

p = Person()
p.Name = "Liu"
p.Gender = "Male"

print('{0} is {1}'.format(p.GetName(), p.GetGender()))

print('{0} is {1}'.format(p.Name, p.Gender))

class Chinese:
    def __init__(self):
        self.Name = None
        self.Gender = None
    def GetName(self):
        return self.Name
    def GetGender(self):
        return self.Gender

c = Chinese()
c.Name = '刘'
c.Gender = '女'

print('{0} is {1}'.format(c.GetName(), c.GetGender()))

print('{0} is {1}'.format(c.Name, c.Gender))


'''
There are some weird things.
'''

p.Name = 'Zhang'
p.Gender = 'Female'

print('{0} is {1}'.format(p.Name, p.Gender))

'''
* p is 'Liu' or 'Zhang'?
* p is 'Male' or 'Female'?
* Can we print 'Liu' by p again? 
'''
