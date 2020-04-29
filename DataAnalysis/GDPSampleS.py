# -*- coding: utf-8 -*-

import lxml.html
import urllib.request

#http://www.8pu.com/country/USA/

r = urllib.request.urlopen('http://www.8pu.com/gdp/ranking_2017.html')

p = lxml.html.parse(r)

doc = p.getroot()

rows = doc.findall('.//table')[0].findall('.//tr')

header = [v.text_content() for v in rows[0].findall('.//th')]

data=[[v.text_content().replace('\xa0','').replace('￥','').replace('亿元','')
         for v in r.findall('.//td')] for r in rows[1:]]

print(data[0:10])

from pandas.io.parsers import TextParser

df = TextParser(data, names=header).get_chunk()

print(df[0:10])

df.to_csv('gdp.csv', encoding='gb2312')

import matplotlib
import matplotlib.pyplot as plt

matplotlib.rc('font', **{'family' : 'SimHei'})

df[0:10].plot(x='国家名称', y='GDP总量(人民币亿元)', kind='bar')

plt.show()


