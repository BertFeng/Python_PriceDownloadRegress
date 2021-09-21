#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pandas_datareader


# In[3]:


import pandas_datareader.data as dtr


# In[20]:


tickers = ['fb','aapl','amzn','nflx','goog','^gspc']


# In[21]:


D = dtr.DataReader(tickers,'yahoo')


# In[22]:


type(D)


# In[23]:


D.tail()


# In[24]:


P = D['Adj Close']


# In[25]:


P.tail()


# In[26]:


Returns = P / P.shift(1) - 1


# In[33]:


Returns.head()


# In[28]:


R = P.pct_change()


# In[35]:


R.head()


# In[32]:


R2 = R.tail(100)


# In[36]:


R2.columns


# In[43]:


R2 = R2.rename(columns = {'^gspc':'SnP'})


# In[44]:


R2.tail()


# In[52]:


import numpy as np


# In[55]:


import pandas as pd


# In[57]:


pip install statsmodels


# In[62]:


import statsmodels.formula.api as sm


# In[65]:


results = sm.ols(formula = 'fb ~ SnP',data = R2).fit()


# In[66]:


results.params


# In[68]:


mystocks = R.columns[:5]


# In[69]:


mystocks


# In[70]:


type(mystocks)


# In[75]:


betalist = []

for mystock in mystocks:
    myformula = mystock + ' ~ SnP'
    print(myformula)
    results = sm.ols(formula = myformula,data = R2).fit()
    print(results.params['SnP'])
    betalist.append(results.params['SnP'])


# In[76]:


betalist


# In[78]:


betavec = np.array(betalist)


# In[79]:


notional = 100
notional * betavec


# In[80]:


sum(notional * betavec)


# In[ ]:




