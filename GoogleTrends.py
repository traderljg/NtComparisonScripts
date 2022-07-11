# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 13:51:50 2022

@author: Lucas Gibson
@Description: Simple program to pull data into excel from Google Trends for specific search terms
@Date: 07/11/2022
"""
from pytrends.request import TrendReq
import pandas as pd


pt = TrendReq(hl="en-US", tz=360)
date_start = '1/1/2021'
pytrend = TrendReq()


#Search words
KEYWORDS=['Northern Trust','BlackRock','Goldman Sachs','BNY Mellon','State Street'] 

#Get the specific search term code for each company
KEYWORDS_CODES=[pytrend.suggestions(keyword=i)[0] for i in KEYWORDS] 
df_CODES= pd.DataFrame(KEYWORDS_CODES)
df_CODES



pt.build_payload([df_CODES['mid'].iloc[0],df_CODES['mid'].iloc[1],
                  df_CODES['mid'].iloc[2],
                  df_CODES['mid'].iloc[3], df_CODES['mid'].iloc[4]], 
                  timeframe='2022-01-01 2022-07-01')

# get the interest over time
df = pt.interest_over_time()

df = df.drop('isPartial', axis = 1)

#Name columns
df.columns = ['Northern Trust','BlackRock','Goldman Sachs','BNY Mellon','State Street']

#Make first column date column
data = pd.date_range(date_start, periods = len(df) , freq ='d')
df['Date'] = data
first_column = df.pop('Date')
df.insert(0, 'Date', first_column)

#Remove time from date
df['Date'] = pd.to_datetime(df['Date']).dt.date

#Export to Excel
df.to_excel(r'D:\Lucas\N Trust\GoogTrends.xlsx', index = False)



