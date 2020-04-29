
# 读取 Northwind.txt 文本数据到 DataFrame。
# （1）      查询出在1997年3月份销售过的产品名称。
# （2）      求解销售相关性最强的两个产品。
# （3）      求解销售业绩波动最小的产品。

import numpy as np
import pandas as pd

data = pd.read_table('Northwind.txt', sep=',')

# （1）      查询出在1997年3月份销售过的产品名称。
data1 = data[((data.OrderYear == 1997) & \
    (data.OrderMonth == 3))]
print(data1.ProductName.sort_values().unique())

# （2）      求解销售相关性最强的两个产品。
grouped = data.loc[:,\
    ['OrderYear','OrderMonth','Quantity']].groupby( \
        data.ProductName)

carr = []

for (pn1), group1 in grouped:
    g1 = pd.DataFrame(group1, \
        columns=['OrderYear','OrderMonth','Quantity'])
    g1 = g1.Quantity.groupby( \
        [g1.OrderYear,g1.OrderMonth]).sum()
    g1 = pd.DataFrame(g1)
    for (pn2), group2 in grouped:
        if pn1 == pn2:
            continue
        g2 = pd.DataFrame(group2, \
            columns=['OrderYear','OrderMonth','Quantity'])
        g2 = g2.Quantity.groupby(\
            [g2.OrderYear,g2.OrderMonth]).sum()
        g2 = pd.DataFrame(g2)
        prod = g1.merge(g2, \
            left_index=True,right_index=True)
        c = prod.loc[:,'Quantity_x'].corr(prod.loc[:,'Quantity_y'])
        carr.append({'p':(pn1,pn2),'c':c})

carr = pd.DataFrame(carr)
print(carr.head())
print(carr.sort_values(by=['c'], ascending=False).head())

# （3）      求解销售业绩波动最小的产品。
carr = []
for pn, group in grouped:
    g = pd.DataFrame(group, \
        columns=['OrderYear','OrderMonth','Quantity'])
    g = g.Quantity.groupby( \
        [g.OrderYear,g.OrderMonth]).sum()
    g = pd.DataFrame(g)
    v = g.Quantity.std()
    carr.append({'p':pn,'v':v})

carr = pd.DataFrame(carr)
print(carr.sort_values(by=['v']))
