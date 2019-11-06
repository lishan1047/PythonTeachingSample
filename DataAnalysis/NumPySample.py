# This is numpy sample.

import numpy as np

# 矩阵运算
a = np.random.randn(12).reshape(3, 4)
print(a)

b = np.random.randn(12).reshape(3, 4)
print(b)

print(a + b)
print(a - b)
print(a * b)
print(a * 2)
print(a.T)
print(a.T.dot(a))
print('------------------------------------------------')
print(np.abs(a))
print('------------------------------------------------')
print(np.cos(a))
print('------------------------------------------------')

c = np.arange(-9, 9).reshape(3,6)
c[c > 0] = 1
c[c < 0] = -1
print(c)

n = np.array(['张','李','张','王','王','李','张'])
d =np.array(
    [[80, 34, 78, 92],
    [67, 54, 72, 88],
    [89, 32, 56, 93],
    [77, 46, 79, 82],
    [74, 42, 65, 89],
    [78, 38, 66, 86],
    [69, 32, 58, 95]])
print(d)

#（1）	获取’张’采集到的所有数据
print('------------------------------------------------')
print(d[n == '张'])

#（2）	获取’李’和’王’采集到的所有数据
print('------------------------------------------------')
print(d[(n == '李') | (n == '王')])

#（3）	获取三人采集到A1~A4的最大数据
print('------------------------------------------------')
x = np.concatenate((
    d[n == '张'].max(0).reshape(1, 4), 
    d[n == '李'].max(0).reshape(1, 4), 
    d[n == '王'].max(0).reshape(1, 4)))
print(x)

#（4）	获取A1~A4最大数据的采集人
print('------------------------------------------------')
x = d.max(0)
t = np.where(d == x, True, False).T
print(np.concatenate((n[t[0]], n[t[1]], n[t[2]], n[t[3]])))
