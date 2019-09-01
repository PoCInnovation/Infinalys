#! /bin/env python3
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 

import pandas as pd
import numpy as np
import yfinance as yf
from tensorflow import keras
import plotly.graph_objects as go

# Number of time units to predict
PREDICT  = 100
# AI predicts stocks at t with data from t-LOOKBACK to t-1
LOOKBACK = 30
# Number of epochs for training
EPOCHS   = 20

def plot_stocks_pandas(df):
    fig = go.Figure(data=[go.Candlestick(x=df.index,
                                         open=df['Open'],
                                         high=df['High'],
                                         low=df['Low'],
                                         close=df['Close'])])
    fig.show()

def plot_stocks_numpy(nparr):
    arr = np.swapaxes(nparr, 0,1)
    fig = go.Figure(data=[go.Candlestick(x=list(range(len(arr))),
                                         open=arr[0],
                                         high=arr[1],
                                         low=arr[2],
                                         close=arr[3])])
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
    model.add(keras.layers.LSTM(128, input_shape=(LOOKBACK, 5), return_sequences=True))
    model.add(keras.layers.Dropout(0.3))
    model.add(keras.layers.LSTM(64, input_shape=(LOOKBACK, 5), return_sequences=True))
    model.add(keras.layers.Dropout(0.3))
    model.add(keras.layers.Dense(5, activation='relu'))
    return model

def compile_model(model):
    '''
        defines model optimizer and loss function
    '''
    model.compile(optimizer='adam',loss='mse')
    model.summary()
    return model

def test_model(model, x_test, y_test):
    output = model.predict(np.array([x_test]))
    error = []
    for i in range(len(output)):
        error.append(abs(100 - output[i] * 100 / y_test[i]))
    error = np.array(error)
    return np.mean(error)

SAVE = True
LOAD = False
MODEL_PATH = './model_saves/first_try.h5'

if __name__ == "__main__":
    # dataset = yf.download('TSLA').to_numpy()
    dataset = pd.read_csv('./tesla_stocks.csv').to_numpy()
    dataset = normalize_data(dataset)
    x_train, y_train = split_dataset(dataset)
    x_test = x_train[int(len(x_train) - PREDICT):]
    x_train = x_train[:int(len(x_train) - PREDICT)]
    y_test = y_train[int(len(y_train) - PREDICT):]
    y_train = y_train[:int(len(y_train) - PREDICT)]
    plot_stocks_numpy(x_train)
    exit()
    model = get_model()

    if LOAD:
        model.load_weights(MODEL_PATH)

    compile_model(model)
    model.fit(x=x_train, y=y_train, validation_split=0.2, epochs=EPOCHS)
    errors_means = []
    for i in range(PREDICT):
        errors_means.append(test_model(model, x_test[i], y_test[i]))
    for mean in errors_means:
        print('#' + str(errors_means.index(mean)), "\tAverage error", int(mean), "%")
    print("\nAVERAGE ERROR", np.mean(np.array(errors_means)), "% (calculated on the", PREDICT, "last time units of the dataset)")
    print("Evaluated loss: ", model.evaluate(x=x_test, y=y_test))
    if SAVE:
        model.save_weights(MODEL_PATH)