# MGS314 Finance Project

import pandas_datareader as web
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

# Social Media Companies
# Google, Facebook, Twitter
companies = ['GOOGL','FB','TWTR']

# Five year period
start = dt.datetime(2018,1,1)
end = dt.datetime(2019,1,1)

#Create CSV file for each company
for i in companies:
    df = web.DataReader(i, 'yahoo', start, end)
    data = df.to_csv(i + '.csv')

style.use('dark_background')

# Create graphs for each company
for i in companies:
    df = pd.read_csv(i + '.csv', parse_dates = True, index_col = 0)
    df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
    df.dropna(inplace=True)


    df['Adj Close'].plot(color = 'red')
    plt.title(i + ' Adjusted Close')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.show()
    
    df['100ma'].plot(color = 'green')
    plt.title(i + ' 100-Day Moving Average')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.show()
    
    df['Volume'].plot(color = 'blue')
    plt.title(i + ' Volume')
    plt.xlabel('Date')
    plt.ylabel('Volume')
    plt.show()
    
    print(df[['High', 'Low', 'Adj Close']].tail(20))
    


