# Show the basic data type in Python.

'''
(1) 以下代码说明数值型：
    - 变量
    - 变量赋值
    - 数据类型
    - 运算
'''
x = 100
y = 101.1
z = x + y

print(z)

x = y = 3
z = x ** y

print(z)

x, y = 3, 8
z = x / y

print(z)

x, y = 17, 3
z = x % y

print(z)

x, y = 17, 3
z = x // y

print(z)

print(type(x))
print(type(y))
print(type(z))

x, y = 5+3j, 4+2j
z = x + y

print(z)

print(type(x))
print(type(y))
print(type(z))

'''
(2) 以下代码说明字符型：
    - 变量
    - 变量赋值
    - 操作
'''
name = 'Li Shan'
sayHello = 'Hello World!'

rs = sayHello + ', ' + name

print(rs)

rs = name * 3

print(rs)

print(name[0])
print(name[3:])
print(name[0:2])

print('Hello' in name)
print('World' not in sayHello)

print(name + '\t' + sayHello)
print(name + r'\t' + sayHello)

print("我的姓名：%s\n我的问候：%s\n" % (name, sayHello))

print(f"{1+3}")
