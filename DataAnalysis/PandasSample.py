# This is a pandas sample.

import numpy as np
import pandas as pd

# Basic operation.

# Series
# A series is an 1-d array of key(label/index)-value pair.

# Create a series and index.
s = pd.Series([1,2,3,4,5])
print(s)
print(s.values)
print(s.index)
print(s[0])

print('----------------------------------')
s = pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
print(s)
print(s.values)
print(s.index)
print(s[0])
print(s['a'])

print('----------------------------------')
s = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
print(s)

print('----------------------------------')
#print(s[s > 2 & s < 5]) #Error
print(s[s > 2][s < 5])
print(2 in s)
print('c' in s)
print(2 in s.values)
print(np.exp(s))

print('----------------------------------')
# Can we put string into the values of series?
s = pd.Series(['a','b','c','d','e'])
print(s)
#np.exp(s)
s = pd.Series([[1,2,3],[4,5]])
print(s)
#np.exp(s)

print('----------------------------------')
print(pd.isnull(s))
s[0] = None
print(pd.isnull(s))

print('----------------------------------')
s1 = pd.Series({'a':1, 'b':2, 'c':3})
s2 = pd.Series({'a':2, 'c':3, 'd':4})
print(s1 + s2)
