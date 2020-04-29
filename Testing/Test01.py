#给定数据文件 Northwind.txt，请编程输出1997年销售量环比增长最大的前10名产品信息。

import numpy as np
import pandas as pd

data = pd.read_table('Northwind.txt', sep=',')

data1996 = data[data['OrderYear'] == 1996].loc[:,['ProductName','Quantity']]

g1996 = data1996.groupby(data1996.ProductName).sum()

data1997 = data[data['OrderYear'] == 1997].loc[:,['ProductName','Quantity']]

g1997 = data1996.groupby(data1996.ProductName).sum()

