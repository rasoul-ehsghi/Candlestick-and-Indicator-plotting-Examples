#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd

df = pd.read_csv('C:/Users/AFRAA/OneDrive/Desktop/Datasets/GBPUSD_Candlestick_15_M_BID_02.01.2023-30.12.2023.csv')
df


# In[12]:


df=df[df["Volume"]!=0]
df


# In[17]:


import pandas_ta as ta


df["EMA"] = ta.ema(df.Close, length=10)
df["RSI"] = ta.rsi(df.Close, length=10)


# In[18]:


dfpl = df[1000:1500]

import plotly.graph_objects as go

fig = go.Figure(data=[go.Candlestick(x=dfpl.index, 
                open=dfpl['Open'],
                high=dfpl['High'],
                low=dfpl['Low'],
                close=dfpl['Close']),
                go.Scatter(x=dfpl.index, y=dfpl.EMA, line=dict(color='black', width=2), name="EMA")])

fig.show()


# In[9]:


df


# In[ ]:




