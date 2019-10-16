'''
This is the test for Capsulation.
'''

import Capsulation

p = Capsulation.Person('Liu', Capsulation.Gender.Female)

print('{0} is {1}'.format(p.GetName(), p.GetGender()))

print('{0} is {1}'.format(p.GetName(), p.GetGender().name))

from Capsulation import *

p = Person('Zhang', Gender.Male)

print('{0} is {1}'.format(p.GetName(), p.GetGender().name))
