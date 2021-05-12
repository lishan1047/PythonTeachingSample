import numpy as np
import pandas as pd

data = pd.read_table('Northwind.txt', sep=',')

# （2）      求解销售相关性最强的两个产品。（解法二）
data = data.where(data.OrderYear != 2008)

products = pd.DataFrame(data.ProductName.unique()).dropna()
products = products.to_numpy().reshape(1, len(products))[0]

pg = [data[data.ProductName == p].groupby( \
    by = [data.OrderYear, data.OrderMonth])['Quantity'].sum() \
    for p in products]

join = pd.concat(pg, axis = 1, keys = products).fillna(0).corr()
max_arr = join[join != 1.0].max()
maxv = max_arr.max()
print(max_arr[max_arr == maxv])
