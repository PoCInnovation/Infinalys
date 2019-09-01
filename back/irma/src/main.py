#! /bin/env python3
import numpy as np
import yfinance as yf
from tensorflow import keras
import plotly.graph_objects as go

# Number of time units to predict
PREDICT  = 30
# AI predicts stocks at t with data from t-LOOKBACK to t-1
LOOKBACK = 30
# Number of epochs for training
EPOCHS   = 5


def plot_stocks_pandas(df):
    fig = go.Figure(data=[go.Candlestick(x=df.index,
                                         open=df['Open'],
                                         high=df['High'],
                                         low=df['Low'],
                                         close=df['Close'])])
    fig.show()


def normalize_data(dataset):
    '''
        normalize the given array (0 to 1)
    '''
    dataset = np.swapaxes(dataset,0,1)[1:]
    for i in range(len(dataset)):
        dataset[i] = (dataset[i] - min(dataset[i])) / (max(dataset[i]) - min(dataset[i]))
    dataset = np.swapaxes(dataset, 0, 1)
    return dataset


def split_dataset(dataset):
    '''
        creates two arrays
        x: t-LOOKBACK to t-1 time units stock values
        y: t stocks
    '''
    x, y = [], []
    for i in range(LOOKBACK, len(dataset)):
        x.append(dataset[i-LOOKBACK:i])
        y.append(dataset[i])
    return np.array(x), np.array(y)

def get_model():
    '''
        defines LSTM model
    '''
    model = keras.Sequential()
    model = keras.models.Sequential()
    model.add(keras.layers.LSTM(4, input_shape=(LOOKBACK, 5), return_sequences=False))
    model.add(keras.layers.Dropout(0.2))
    model.add(keras.layers.Dense(5, activation='relu'))
    return model

def compile_model(model):
    '''
        defines model optimizer and loss function
    '''
    model.compile(optimizer='adam',loss='mse')
    model.summary()
    return model

if __name__ == "__main__":
    dataset = yf.download('AAPL').to_numpy()
    dataset = normalize_data(dataset)
    x_train, y_train = split_dataset(dataset)
    x_test = x_train[int(len(x_train) - PREDICT):]
    x_train = x_train[:int(len(x_train) - PREDICT)]
    y_test = y_train[int(len(y_train) - PREDICT):]
    y_train = y_train[:int(len(y_train) - PREDICT)]

    model = get_model()
    compile_model(model)
    model.fit(x=x_train, y=y_train, epochs=EPOCHS)
