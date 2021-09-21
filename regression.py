pip install pandas_datareader

import pandas_datareader.data as dtr

tickers = ['fb','aapl','amzn','nflx','goog','^gspc']

D = dtr.DataReader(tickers,'yahoo')

type(D)

D.tail()

P = D['Adj Close']

P.tail()

Returns = P / P.shift(1) - 1

Returns.head()

R = P.pct_change()

R.head()

R2 = R.tail(100)

R2.columns

R2 = R2.rename(columns = {'^gspc':'SnP'})

R2.tail()

import numpy as np

import pandas as pd

pip install statsmodels

import statsmodels.formula.api as sm

results = sm.ols(formula = 'fb ~ SnP',data = R2).fit()

results.params

mystocks = R.columns[:5]

mystocks

type(mystocks)

betalist = []

for mystock in mystocks:
    myformula = mystock + ' ~ SnP'
    print(myformula)
    results = sm.ols(formula = myformula,data = R2).fit()
    print(results.params['SnP'])
    betalist.append(results.params['SnP'])

betalist

betavec = np.array(betalist)

notional = 100
notional * betavec

sum(notional * betavec)
