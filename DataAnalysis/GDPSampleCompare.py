# -*- coding: utf-8 -*-

import lxml.html
import urllib.request
import pandas as pd

from bs4 import BeautifulSoup
from pandas.io.parsers import TextParser

def GetGDP(year, table):
    r = urllib.request.urlopen('http://www.8pu.com/gdp/ranking_{0}.html'.format(year))
    c = r.read()
    soup = BeautifulSoup(c,'lxml')
    header = [v.get_text() for v in soup.table.find_all('th')]
    data=[[v.get_text().replace('\xa0','').replace('￥','').replace('亿元','')
        for v in r.find_all('td')] for r in soup.table.find_all('tr')[1:]]
    df = TextParser(data, names=header).get_chunk()
    table[year] = df

start = 2010
table = {}
for year in range(start, 2020):
    GetGDP(year, table)

years = []
diff = []
for year in range(start, 2020):
    years.append(year)
    diff.append(table[year][table[year]['国家/地区'] == '美国']['GDP总量(人民币亿元)'].iloc[0] - \
        table[year][table[year]['国家/地区'] == '中国']['GDP总量(人民币亿元)'].iloc[0])

table = pd.DataFrame({'year':years, 'diff':diff})

print(table)

import matplotlib
import matplotlib.pyplot as plt

matplotlib.rc('font', **{'family' : 'SimHei'})

table.plot(x='year', y='diff', kind='bar')

plt.show()
