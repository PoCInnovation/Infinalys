import yfinance as yf
from tensorflow import keras
import plotly.graph_objects as go


def plot_stocks_pandas(df):
    fig = go.Figure(data=[go.Candlestick(x=df.index,
                                         open=df['Open'],
                                         high=df['High'],
                                         low=df['Low'],
                                         close=df['Close'])])
    fig.show()


def get_model():
    model = keras.Sequential()
    return model


if __name__ == "__main__":
    df = yf.download('AAPL')
    model = get_model()
    model.fit()
    print(df.to_numpy())
