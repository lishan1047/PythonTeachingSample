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

## 上述做法没有对齐数据
## 现在需要对齐数据

konbu = data[data.ProductName == 'Konbu'].groupby( \
    [data.OrderYear, data.OrderMonth])['Quantity'].sum().reset_index()
print(konbu)

tofu = data[data.ProductName == 'Tofu'].groupby( \
    [data.OrderYear, data.OrderMonth])['Quantity'].sum().reset_index()
print(tofu)

joined = pd.merge(konbu, tofu, on=['OrderYear','OrderMonth'], suffixes=['_konbu','_tofu'])
print(joined)

print(joined['Quantity_konbu'].corr(joined['Quantity_tofu']))
