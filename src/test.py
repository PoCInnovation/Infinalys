import yfinance as yf
import plotly.graph_objects as go

df = yf.download('AAPL')

fig = go.Figure(data=[go.Candlestick(x=df.index,
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])
fig.show()