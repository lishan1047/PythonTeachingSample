import math

# 编写一个代表圆形的类，其具备：
# (1)半径属性
# (2)求面积行为

class Circle:
    def __init__(self, radius):
        self.Radius = radius
    def GetArea(self):
        return 3.14 * self.Radius * self.Radius

c = Circle(3)
print("The circle's radius is {0}. It's area is {1:.2f}."
    .format(c.Radius, c.GetArea()))

# 编写一个代表矩形的类，其具备：
# （1）长、宽属性
# （2）求面积行为

class Rect:
    def __init__(self, width, height):
        self.Width = width
        self.Height = height
    def GetArea(self):
        return self.Width * self.Height

r = Rect(10, 8)
print("The rect's width is {0}, height is {1}, area is {2}"
    .format(r.Width, r.Height, r.GetArea()))

# 编写一个代表球体的类，其具备：
# （1）半径属性
# （2）求表面积行为
# （3）求体积行为

class Ball:
    def __init__(self, radius):
        self.Radius = radius
    def GetSurfaceArea(self):
        return 4 * 3.14 * self.Radius * self.Radius
    def GetVolume(self):
        return (4.0/3.0) * 3.14 * math.pow(self.Radius, 3)

b = Ball(3.5)
print("The ball's radius is {0}, surface area is {1:.2f}, volume is {2:.2f}"
    .format(b.Radius, b.GetSurfaceArea(), b.GetVolume()))


# 编写一个代表小狗的类，其具备：
# （1） 名字、毛色、性别属性
# （2） 吠的行为
# （3）跑的行为

class Dog:
    def __init__(self, name, furtherColor, gender):
        self.Name = name
        self.FurtherColor = furtherColor
        self.Gender = gender
    def Bark(self):
        print("A {gender} {name} dog with {further} is barking."
            .format(gender = self.Gender, name = self.Name, further = self.FurtherColor))
    def Run(self):
        print("A {gender} {name} dog with {further} is running."
            .format(gender = self.Gender, name = self.Name, further = self.FurtherColor))

dog = Dog('Wangcai', 'Gold', 'male')
dog.Bark()
dog.Run()

# 编写一个代表小猫的类，其具备：
# （1）名字、品种、眼睛颜色、性别属性
# （2）叫的行为
# （3）奔跑的行为

class Cat:
    def __init__(self, name, category, eyeColor, gender):
        self.Name = name
        self.Category = category
        self.EyeColor = eyeColor
        self.Gender = gender
    def Shout(self):
        print("A {name} {gender} {category} cat with {color} eyes is miao..."
            .format(name = self.Name, gender = self.Gender, color = self.EyeColor, category = self.Category))
    def Run(self):
        print("A {name} {gender} {category} cat with {color} eyes is running..."
            .format(name = self.Name, gender = self.Gender, color = self.EyeColor, category = self.Category))

cat = Cat('Xiaohua', 'Bosi', 'Blue', 'female')
cat.Shout()
cat.Run()


# 编写一个代表二维表格的类，其具备：
# （1）       名称
# （2）       标题属性
# （3）       表格数据属性
# （4）       求解每列数据和、均值、最大值、最小值、标准差的行为
# （5）       求解每行数据和、均值、最大值、最小值、标准差的行为

class DataTable:
    def __init__(self, titles):
        self.Titles = titles
        self.Rows = []
    def GetSumOnColumn(self, index):
        x = 0
        for r in self.Rows:
            x += r[index]
        return x
    def GetAverageOnColumn(self, index):
        return self.GetSumOnColumn(index) / len(self.Rows)
    def GetMaxOnColumn(self, index):
        x = self.Rows[0][index]
        for r in self.Rows:
            if r[index] > x:
                x = r[index]
        return x
    def GetMinOnColumn(self, index):
        x = self.Rows[0][index]
        for r in self.Rows:
            if r[index] < x:
                x = r[index]
        return x
    def GetStdDevOnColumn(self, index):
        avg = self.GetAverageOnColumn(index)
        x = 0
        for r in self.Rows:
            x += (r[index]-avg)**2
        return math.sqrt(1.0*x/len(self.Rows))
    def __str__(self):
        s = ''
        s += '-'*len(self.Titles)*10 + '\n'
        for title in self.Titles:
            s += '{0:10s}'.format(title)
        s += '\n' + '-'*len(self.Titles)*10
        for r in self.Rows:
            s += '\n'
            for i in range(0, len(self.Titles)):
                s += '{0}'.format(repr(r[i]).ljust(10))
        s += '\n' + '-'*len(self.Titles)*10
        s += '\n'
        for i in range(0, len(self.Titles)):
            s += '{0}'.format(repr(self.GetSumOnColumn(i)).ljust(10))
        s += '\n'
        for i in range(0, len(self.Titles)):
            s += '{0:<10.2f}'.format(self.GetAverageOnColumn(i))
        s += '\n'
        for i in range(0, len(self.Titles)):
            s += '{0}'.format(repr(self.GetMaxOnColumn(i)).ljust(10)) 
        s += '\n'
        for i in range(0, len(self.Titles)):
            s += '{0}'.format(repr(self.GetMinOnColumn(i)).ljust(10)) 
        s += '\n'
        for i in range(0, len(self.Titles)):
            s += '{0:<10.2f}'.format(self.GetStdDevOnColumn(i))
        s += '\n'
        s += '-'*len(self.Titles)*10
        return s

dt = DataTable(('No', 'Gender', 'Age', 'Score'))
dt.Rows.append((1,1,23,4))
dt.Rows.append((2,2,43,2))
dt.Rows.append((3,2,34,3))
dt.Rows.append((4,1,25,3))

print(dt.GetSumOnColumn(3))
print(dt.GetAverageOnColumn(3))
print(dt.GetMaxOnColumn(3))
print(dt.GetMinOnColumn(3))
print(dt.GetStdDevOnColumn(3))
print(dt)
