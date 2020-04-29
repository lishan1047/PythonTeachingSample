class Chinese:
    def __init__(self):
        self.Name = None
        self.Gender = None
    def GetName(self):
        return self.Name
    def GetGender(self):
        return self.Gender
c = Chinese()
c.Name = '刘'
c.Gender = '女'
print('{0} is {1}'.format(c.GetName(), c.GetGender()))
print('{0} is {1}'.format(c.Name, c.Gender))
