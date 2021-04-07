import pandas as pd
import matplotlib.pyplot as plt

t = pd.read_table('Northwind.txt', sep=',')

df1 = t[t['ProductName'] == 'Konbu']
df1 = df1.groupby(['OrderYear','OrderMonth']).agg(sum)
df2 = t[t['ProductName'] == 'Tofu']
df2 = df2.groupby(['OrderYear','OrderMonth']).agg(sum)

fig, axes = plt.subplots(2, 1, sharex = True, sharey = True)

df1['Sales'].plot(ax=axes[0], color='k')
df2['Sales'].plot(ax=axes[1], color='g')

plt.show()
