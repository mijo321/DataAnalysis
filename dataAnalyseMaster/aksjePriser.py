import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime


api_key = 'RHITLuYNUAcdgDpRbRF1BkHbsgtnF2tU'
url = 'https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/hour/2023-01-09/2023-01-09?adjusted=true&sort=asc&limit=500&apiKey=' + api_key


response = requests.get(url)
data = response.json()


df = pd.DataFrame(data['results'])


df['timestamp'] = pd.to_datetime(df['t'], unit='ms')


closing = df['c']
opening = df['o']
high = df['h']
low = df['l']
volume = df['v']


sns.set_theme()


plt.figure(figsize=(10, 6))


plt.plot(df['timestamp'], closing, label='Closing Price', color='k')
plt.plot(df['timestamp'], opening, label='Opening Price', color='g')
plt.plot(df['timestamp'], high, label='High Price', color='r')
plt.plot(df['timestamp'], low, label='Low Price', color='b')

ax2 = plt.twinx()
ax2.bar(df['timestamp'], volume, color='gray', alpha=0.5, width=0.01)
ax2.set_ylabel('Volume', color='gray')

plt.xlabel('Date')
plt.title('AAPL Stock Prices (Jan 9, 2023)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
