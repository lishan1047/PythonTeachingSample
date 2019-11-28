##################################
#   Pandas for Northwind.
##################################

import numpy as np
import pandas as pd

data = pd.read_table('Northwind.txt', sep=',')

print(data)

konbu = data[data.ProductName == 'Konbu'].copy()

print(konbu)

konbu['SaleTime'] = konbu.apply( \
    lambda x: '{}.{:0>2d}'.format(x['OrderYear'], x['OrderMonth']), \
    axis = 1)
konbu = pd.Series(konbu['Quantity'].tolist(), index=konbu['SaleTime'])

print(konbu)

tofu = data[data.ProductName == 'Tofu'].copy()

tofu['SaleTime'] = tofu.apply( \
    lambda x: '{}.{:0>2d}'.format(x['OrderYear'], x['OrderMonth']), \
    axis = 1)
tofu = pd.Series(tofu['Quantity'].tolist(), index=tofu['SaleTime'])

print(tofu)

print(konbu.corr(tofu))

