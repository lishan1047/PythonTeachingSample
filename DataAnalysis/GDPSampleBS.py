# -*- coding: utf-8 -*-

import lxml.html
import urllib.request

#http://www.8pu.com/country/USA/

r = urllib.request.urlopen('http://www.8pu.com/gdp/ranking_2017.html')

c = r.read()

## with beautifulsoap

from bs4 import BeautifulSoup
soup = BeautifulSoup(c,'lxml')

print(soup.prettify())

print(soup.table.find_all('th'))

##header = []
##for v in soup.table.find_all('th'):
##    h = ''
##    for s in v.stripped_strings:
##        h += s
##    header.append(h)

header = [v.get_text() for v in soup.table.find_all('th')]

print(header)

##data = []
##for tr in soup.table.find_all('tr')[1:]:
##    r = []
##    for td in tr.find_all('td'):
##        d = ''
##        for s in td.stripped_strings:
##            d += s.replace('\xa0', '').replace('￥', '').replace('亿元', '')
##        r.append(d)
##    data.append(r)

data=[[v.get_text().replace('\xa0','').replace('￥','').replace('亿元','')
         for v in r.find_all('td')] for r in soup.table.find_all('tr')[1:]]

from pandas.io.parsers import TextParser

df = TextParser(data, names=header).get_chunk()

print(df[0:10])

df.to_csv('gdp.csv', encoding='gb2312')

import matplotlib
import matplotlib.pyplot as plt

matplotlib.rc('font', **{'family' : 'SimHei'})

df[0:10].plot(x='国家名称', y='GDP总量(人民币亿元)', kind='bar')

plt.show()

