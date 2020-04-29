# -*- coding: utf-8 -*-

import lxml.html
import urllib.request
import numpy as np
import pandas as pd

def GetGDPDoc(year):
    r = urllib.request.urlopen( \
        'http://www.8pu.com/gdp/ranking_{0}.html'.format(year))
    p = lxml.html.parse(r)
    doc = p.getroot()
    return doc

def GetGDPData(doc):
    rows = doc.findall('.//table')[0].findall('.//tr')
    header = [v.text_content() for v in \
        rows[0].findall('.//th')]
    data=[[v.text_content().replace('\xa0',''). \
        replace('￥','').replace('亿元','')
            for v in r.findall('.//td')] for r in rows[1:]]
    return (header,data)

from pandas.io.parsers import TextParser

def GetGDPDataFrame(header, data):
    df = TextParser(data, names=header).get_chunk()
    return df

import matplotlib
import matplotlib.pyplot as plt

def DrawTop10GDP():
    for year in range(2008, 2019):
        header, data = GetGDPData(GetGDPDoc(year))
        df = GetGDPDataFrame(header, data)[0:10]
        matplotlib.rc('font', **{'family' : 'SimHei'})
        df[0:10].plot(x='国家名称', y='GDP总量(人民币亿元)', kind='bar', title=year)
        plt.show()

DrawTop10GDP()

def DrawCountryGDP(country):
    gdp = None
    years = range(2008, 2019)
    for year in years:
        header, data = GetGDPData(GetGDPDoc(year))
        df = GetGDPDataFrame(header, data)
        df = df.ix[df['国家名称']==country,:]
        if(gdp is None):
            gdp = df
            gdp['年份'] = year
        else:
            df['年份'] = year
            gdp = gdp.append(df)
    matplotlib.rc('font', **{'family' : 'SimHei'})
    gdp.plot(x='年份', y='GDP总量(人民币亿元)', kind='bar', title=country)
    plt.show()
    
DrawCountryGDP('俄罗斯')
