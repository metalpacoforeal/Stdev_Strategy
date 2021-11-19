import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Get historical data from Yahoo! Finance
symbol = 'OCGN'
time_period = '1y'
ticker = yf.Ticker(symbol)
bars = ticker.history(period='max')

bars['Returns'] = bars['Close'].pct_change()
bars['50 DMA'] = bars['Close'].rolling(50, min_periods=1).mean()
bars['Std Dev'] = bars['Close'].rolling(50, min_periods=1).std()
bars['Z Score'] = (bars['Close'] - bars['50 DMA']) / bars['Std Dev']

bars['Close'].plot()
plt.show()

