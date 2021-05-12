import numpy as np
import pandas as pd



data = pd.read_table('C:/MyFiles/eIvy/Teaching/PythonTeachingSample/DataAnalysis/Northwind.txt', sep=',')

#print(data.head())

t = pd.DataFrame()

#（1）	查询出 Konbu 产品数据
konbu = data[data.ProductName == 'Konbu']
print(konbu)

#（3）	求解上述两个产品的平均售价、销售量
print(konbu.Quantity.mean())

# （4）	计算 Konbu 和 Tofu 两个产品的相关系数。
years = [1996,1997,1998]
months = range(1,13)

times = []
for y in years:
    for m in months:
        times.append({'OrderYear':y,'OrderMonth':m})

for ym in times:
    temp = konbu[(konbu.OrderYear == ym['OrderYear']) & (konbu.OrderMonth == ym['OrderMonth'])]
    if temp.empty:
        continue
    item = {'OrderYear':[temp.iloc[0].OrderYear], \
        'OrderMonth':[temp.iloc[0].OrderMonth], \
        'CategoryName':[temp.iloc[0].CategoryName], \
        'ProductName':[temp.iloc[0].ProductName], \
        'Quantity':[temp['Quantity'].sum()], \
        'Sales':[temp['Sales'].sum()]}
    if t.empty:
        t = pd.DataFrame(item)
    else:
        t = t.append(pd.DataFrame(item), ignore_index=True)

konbu = t

t = pd.DataFrame()

tofu = data[data.ProductName == 'Tofu']

for ym in times:
    temp = tofu[(tofu.OrderYear == ym['OrderYear']) & (tofu.OrderMonth == ym['OrderMonth'])]
    if temp.empty:
        continue
    item = {'OrderYear':[temp.iloc[0].OrderYear], \
        'OrderMonth':[temp.iloc[0].OrderMonth], \
        'CategoryName':[temp.iloc[0].CategoryName], \
        'ProductName':[temp.iloc[0].ProductName], \
        'Quantity':[temp['Quantity'].sum()], \
        'Sales':[temp['Sales'].sum()]}
    if t.empty:
        t = pd.DataFrame(item)
    else:
        t = t.append(pd.DataFrame(item), ignore_index=True)

tofu = t

prod = konbu.merge(tofu, left_on=['OrderYear','OrderMonth'], \
    right_on=['OrderYear','OrderMonth'])

prod = prod.loc[:,['OrderYear','OrderMonth','Quantity_x','Quantity_y']]

print(prod)

print(prod['Quantity_x'].corr(prod['Quantity_y']))
print(prod.loc[:,['Quantity_x','Quantity_y']].corr())
print(prod['Quantity_x'].cov(prod['Quantity_y']))
print(prod.loc[:,['Quantity_x','Quantity_y']].cov())

#（1）	查询出在1997年3月份销售过的产品名称。
prodName = data[(data.OrderYear == 1997) & (data.OrderMonth == 3)].ProductName.unique()
print(prodName)

#（2）	求解销售相关性最强的两个产品。
def getAlignProducts(data, pname):
    years = [1996,1997,1998]
    months = range(1,13)
    times = []
    for y in years:
        for m in months:
            times.append({'OrderYear':y,'OrderMonth':m})    
    t = pd.DataFrame()
    p = data[(data.ProductName == pname)]
    for ym in times:
        temp = p[(p.OrderYear == ym['OrderYear']) & (p.OrderMonth == ym['OrderMonth'])]
        if temp.empty:
            continue
        item = {'OrderYear':[temp.iloc[0].OrderYear], \
            'OrderMonth':[temp.iloc[0].OrderMonth], \
            'CategoryName':[temp.iloc[0].CategoryName], \
            'ProductName':[temp.iloc[0].ProductName], \
            'Quantity':[temp['Quantity'].sum()], \
            'Sales':[temp['Sales'].sum()]}
        if t.empty:
            t = pd.DataFrame(item)
        else:
            t = t.append(pd.DataFrame(item), ignore_index=True)
    return t

def productCorr(data, pname1, pname2):
    p1 = getAlignProducts(data, pname1)
    p2 = getAlignProducts(data, pname2)
    prod = p1.merge(p2, left_on=['OrderYear','OrderMonth'], \
        right_on=['OrderYear','OrderMonth'])
    prod = prod.loc[:,['OrderYear','OrderMonth','Quantity_x','Quantity_y']]
    return prod['Quantity_x'].corr(prod['Quantity_y'])

r = pd.DataFrame()

for pname1 in prodName:
    for pname2 in prodName:
        if pname1 != pname2:
            item = {'p1':[pname1], 'p2':[pname2], 'corr':[productCorr(data, pname1, pname2)]}
            if r.empty:
                r = pd.DataFrame(item)
            else:
                if  r[(r.p1 == pname1) & (r.p2 == pname2)].empty and \
                    r[(r.p1 == pname2) & (r.p2 == pname1)].empty :
                    r = r.append(pd.DataFrame(item), ignore_index = True)

print(r.sort_values(by = 'corr', ascending=False).iloc[0])