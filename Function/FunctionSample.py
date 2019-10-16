"""
函数是将需要重复使用的代码包装成为一个整体。基本上所有的编程语言都需要支持函数这个概念。起始编程中的函数概念就是来自数学语言中函数的概念。
函数分为：定义、调用。
函数定义：函数名、函数参数、函数返回值、函数体四要素。
函数调用：普通调用、嵌套调用、递归调用。
函数参数：函数形参、函数实参、参数值传递、参数引用传递、参数默认值、位置参数、关键字参数、参数柯里化、不定长参数。
函数返回值：单一返回值、元组型多个返回值、迭代返回值。
"""

"""
1. Definition of Function.
"""
def addList(list1, list2):
    if len(list1) != len(list2):
        print('list1\'s count is not equaling to list2\'s')
        return
    nl = []
    i = 0
    for x in list1:
        nl.append(x + list2[i])
        i += 1
    return nl

"""
2. Invoking of Function.
"""
x = addList([1,2,3],[4,5,6])
print(x)

"""
3. Nested Invoking of Function.
"""
def catList(list1, list2):
    """Cat two list into one new list.

    Args:
        list1: the first list, it will be the header part in the new list.
        list2: the second list, it will be the tail part in the new list.

    Returns:
        The new one list containing list1 and list2.
    """
    nl = []
    for x in list1:
        nl.append(x)
    for x in list2:
        nl.append(x)
    return nl

x = catList([1,2,3], [4,5,6,7])
print(x)
x = catList(x, [8,9,10])
print(x)
x = catList(catList([1,2,3],[4,5,6]),[7,8,9])
print(x)
print(catList(catList([1,2,3],[4,5,6]),[7,8,9]))

"""
3. Recursive Invoking of Function.
"""
def Factorial(x):
    if x < 0:
        return 'Factorial is not less than 0.'
    elif x == 0 or x == 1:
        return 1
    else:
        return Factorial(x-1) * x

print("{0}".format(Factorial(-1)))
print("0's Factorial is {0}".format(Factorial(0)))
print("1's Factorial is {0}".format(Factorial(1)))
print("6's Factorial is {0}".format(Factorial(6)))

"""
4. Lambda Expression and Anonymous Function.
"""
square = lambda x : x * x

print(square(3))
print(square(float(input('Input a number:'))))

"""
5. Parameters & Arguments of Function.
"""
def addByTwo(x, y):
    return x + y

print("1 + 2 = {0}".format(addByTwo(1,2)))

"""
6. Value and Reference Tranform of Function Parameters.
"""
def addFirstValueToSecondValue(firstValue, secondValue):
    secondValue = secondValue + firstValue
    return secondValue

firstValue = 1
secondValue = 2

print("first + second = {0}".format(addFirstValueToSecondValue(firstValue, secondValue)))
print("first is {0}, second is {1}".format(firstValue, secondValue))

def addFirstToSecond(firstList, secondList):
    i = 0
    for x in firstList:
        secondList[i] = secondList[i] + x
        i = i + 1
    return secondList

firstList = [1,2,3]
secondList = [4,5,6]

print("add first to second: {0}".format(addFirstToSecond(firstList, secondList)))
print("first list is {0}, second list is {1}".format(firstList, secondList))

"""
7. Positional & KeyWord & Variable-Length Parameters of Function.
"""
def add(x, y, z=0.0):
    return x + y + z

print("相加结果：{0}".format(add(1,2,3)))
print("相加结果：{0}".format(add(1,2)))
print("相加结果：{0}".format(add(x=1,y=2,z=3)))

def addAll(*nums):
    s = 0
    for x in nums:
        s = s + x
    return s

print("add from 1 to 5 is {0}".format(addAll(1,2,3,4,5)))

def getFullName(**names):
    '''Get Full Name by FirstName and SecondName.
    Arg:
        firstName: the first name.
        secondName: the second name.
    Returns:
        firstName secondName
    '''
    return names["firstName"] + " " + names["secondName"]

print("full name is {0}".format(getFullName(firstName='Shan',secondName='Li')))

"""
8. Parameters' curry of Function.
"""
addTwo = lambda x : addByTwo(x, 2)

print("1 add 2 is {0}".format(addTwo(1)))

"""
9. Multiple Returns of Function.
"""
def getComplexValue(real, imaginary):
    return (real, imaginary)

print("complex value is {0}".format(getComplexValue(1,2)))

def getComplexDict(real, imaginary):
    return {'real': real, 'imaginary': imaginary}

print("complex dict is {0}".format(getComplexDict(1,2)))

"""
10. Yield Returns of Function.
"""
def getListSquare(list):
    for x in list:
        yield x * x

print("[1,2,3]'s square is {0}".format(getListSquare([1,2,3])))
for x in getListSquare([1,2,3]):
    print("yield {0}".format(x))

"""
以下内容为编写功能函数的代码。
"""

def IsPrimeNumber(x):
    """ Adjust a number is or not a prime.
    Args:
        x: the designated number for adjust.
    Returns:
        if x is prime then True, else False.
    """
    if x <= 0:
        return 'x should be more than 0.'
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

print("7 is prime number? {0}".format(IsPrimeNumber(7)))
print("8 is prime number? {0}".format(IsPrimeNumber(8)))
print("0 is prime number? {0}".format(IsPrimeNumber(0)))

def GetTringleArea(a, b, c):
    """Get a tringle area.
    Args:
        a: an edge length.
        b: an edge length.
        c: an edge length.
    Returns:
        the area of the tringle.
    """
    s = (a + b + c) / 2.0
    return (s*(s-a)*(s-b)*(s-c)) ** 0.5

print("the area is {0:0.2f}".format(GetTringleArea(2,3,2)))

def GetCircleArea(r):
    """Get a circle area.
    Args:
        r: the radius.
    Returns:
        the area of the circle.
    """
    return 3.14 * r * r

print("the area is {0:0.2f}".format(GetCircleArea(3)))

def GetMaxValue(list):
    """Get the max value in a list.
    Args:
        list: a value list.
    Returns:
        the max value in the list.
    """
    maxv = list[0]
    for x in list:
        if x > maxv:
            maxv = x
    return maxv

print("the max value is {0}".format(GetMaxValue([3,4,3,6,5,6])))

def GetMinValue(list):
    """Get the min value in a list.
    Args:
        list: a value list.
    Returns:
        the min value in the list.
    """
    minv = list[0]
    for x in list:
        if x < minv:
            minv = x
    return minv

print("the min value is {0}".format(GetMinValue([3,4,3,6,5,6])))

def IsLeapYear(someyear):
    """Adjust soome year is or not a leap year.
    Args:
        someyear: for adjust year.
    Returns:
        if it is a leap year, then True, else False.
    """
    if (someyear % 4) == 0:
        if (someyear % 100) == 0:
            if (someyear % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
print("2019 is a leap year? {0}".format(IsLeapYear(2019)))

def GetPrimeNumbers(start, end):
    """Get all prime numbers from start value to end value.
    Args:
        start: the start value of the range.
        end: the end value of the range.
    Returns:
        all the prime numbers in the range of start to end.
    """
    for x in range(start, end + 1):
        if IsPrimeNumber(x):
            yield x

print(GetPrimeNumbers(3, 19))
for x in GetPrimeNumbers(3, 19):
    print("{0} is prime number".format(x))
