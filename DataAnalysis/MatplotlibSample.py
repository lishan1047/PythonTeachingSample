import matplotlib.pyplot as plt
import numpy as np

'''
data = np.arange(10)
plt.plot(data)
plt.show()

fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)

plt.plot(np.random.randn(50).cumsum(), 'k--')
_ = ax1.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)
ax2.scatter(np.arange(30),np.arange(30)+3*np.random.randn(30))
plt.show()

fig, axes = plt.subplots(2,2,sharex=True,sharey=True)
for i in range(2):
    for j in range(2):
        axes[i,j].hist(np.random.randn(500),bins=50,color='k',alpha=0.5)
plt.subplots_adjust(wspace=0,hspace=0)
plt.show()

from numpy.random import randn
plt.plot(randn(30).cumsum(),'ko--')
plt.plot(randn(30), color='g', linestyle='dashed', marker='o')
plt.show()

data = np.random.randn(30).cumsum()
plt.plot(data,'k--',label='Default')
plt.plot(data,'k--',drawstyle='steps-post',label='steps-post')
plt.legend(loc='best')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(np.random.randn(1000).cumsum())
ticks = ax.set_xticks([0,250,500,750,1000])
labels = ax.set_xticklabels(['one','two','three','four','five'], \
    rotation=30,fontsize='small')
ax.set_title('My first matplotlib plot')
ax.set_xlabel('Stages')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(randn(1000).cumsum(),'k',label='one')
ax.plot(randn(1000).cumsum(),'g--',label='two')
ax.plot(randn(1000).cumsum(),'r.',label='three')
ax.legend(loc='best')
plt.show()
'''

import pandas as pd

data = pd.read_table('Northwind.txt',sep=',')

#绘制所有产品月度平均销售额折线图
data.Sales.groupby( \
    [data.OrderYear,data.OrderMonth]).mean().plot()
plt.show()

#绘制所有产品月度平均销售额与销售量对比图
#销售额为柱状图、销售量为折线图
g0 = data.Sales.groupby( \
    [data.OrderYear,data.OrderMonth]).agg( \
        lambda x: x.sum() / len(x))
g0.plot.bar(rot=90)
g1 = data.Quantity.groupby( \
    [data.OrderYear,data.OrderMonth]).sum()
g1.plot(rot=90)
plt.show()

# 绘制Konbu和Tofu两个产品月度销售额汇总对比图
# Konbu为黑色折线图、Tofu为绿色折线图
# 并且分布在不同子图上
fig, axes = plt.subplots(2,1)
g0 = data[data.ProductName == 'Konbu'].Sales.groupby( \
    [data.OrderYear,data.OrderMonth]).sum()
g1 = data[data.ProductName == 'Tofu'].Sales.groupby( \
    [data.OrderYear,data.OrderMonth]).sum()
g0.plot(ax=axes[0],style='k--',label='Konbu')
axes[0].legend(loc='best')
g1.plot(ax=axes[1],style='g--',label='Tofu')
axes[1].legend(loc='best')
plt.show()

# 绘制Konbu和Tofu的销售额对比柱状图
g0 = pd.DataFrame(g0)
g1 = pd.DataFrame(g1)
prod = g0.merge(g1, left_index=True, right_index=True)
prod.rename(columns={ \
    'Sales_x':'Konbu','Sales_y':'Tofu'},inplace=True)
prod.plot.bar()
plt.show()

import seaborn as sns

#绘制Konbu月度不分年度的销售额散点回归图
konbu = data[data.ProductName == 'Konbu']
sns.regplot(x='OrderMonth',y='Sales',data=konbu)
plt.show()
