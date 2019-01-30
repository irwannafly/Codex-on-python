# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 11:35:52 2019

@author: Fujitsu
"""

import pandas as pd
url = 'https://raw.githubusercontent.com/pydata/pydata-book/master/ch09/stock_px.csv'
#df = pd.read_csv(url,index_col=0,parse_dates=[0])
df = pd.read_csv(url)
print (df.head(5))
