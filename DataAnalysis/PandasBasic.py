import numpy as np
import pandas as pd

years = [1996,1997,1998]
months = range(1,13)

times = []
for y in years:
    for m in months:
        times.append({'OrderYear':y,'OrderMonth':m})

data = pd.read_table('C:/MyFiles/eIvy/Teaching/PythonTeachingSample/DataAnalysis/Northwind.txt', sep=',')

#print(data.head())

t = pd.DataFrame()

konbu = data[data.ProductName == 'Konbu']
print(konbu)

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

#print(konbu.sort_values(by=['OrderYear','OrderMonth']))

t = pd.DataFrame()

tofu = data[data.ProductName == 'Tofu']
print(tofu)

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

#print(tofu.sort_values(by=['OrderYear','OrderMonth']))

prod = konbu.merge(tofu, left_on=['OrderYear','OrderMonth'], \
    right_on=['OrderYear','OrderMonth'])

#print(prod.head())

prod = prod.loc[:,['OrderYear','OrderMonth','Quantity_x','Quantity_y']]

print(prod)

print(prod['Quantity_x'].corr(prod['Quantity_y']))
print(prod.loc[:,['Quantity_x','Quantity_y']].corr())
print(prod['Quantity_x'].cov(prod['Quantity_y']))
print(prod.loc[:,['Quantity_x','Quantity_y']].cov())

