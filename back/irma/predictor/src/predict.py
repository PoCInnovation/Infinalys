import os
import sys
import numpy as np
import pandas as pd
from tensorflow import keras

EPOCHS = 1
LOOKBACK = 20
PREDICT = 20
LOADING = (',-\'', '---', '\'-,', ' | ')
LEN_LOADING = len(LOADING)


def print_advancement(file: str, curr: int, total: int):
    """Prints an advancement info of the predict_on_stocks function"""

    print('\r\x1b[2K', end='')
    print(f'[{LOADING[curr % LEN_LOADING]}]', end='')
    current_percent = round((curr / total) * 20)
    advancement = '\033[0;37;44m \033[0;0;0m' * \
        current_percent + '_' * (20 - current_percent)
    print(f'{advancement}| ', end='')
    print(f'Predicting on file {file} ...', end='', flush=True)


class PrintLogs(keras.callbacks.Callback):
    def __init__(self, epochs):
        self.epochs = epochs

    def set_params(self, params):
        params['epochs'] = 0

    def on_epoch_begin(self, epoch, logs=None):
        print(' Epoch %d/%d' % (epoch + 1, self.epochs), end='', flush=True)


def filter_data(raw_data: np.ndarray) -> np.ndarray:
    """Filters a stocks np array to keep wanted parameters"""

    # shape[0] is the mean of [open, high, low, close, adj_close]
    # and shape[1] is the volumes
    shape = (len(raw_data), 2)
    data = np.ndarray(shape)

    for i in range(len(raw_data)):
        row = raw_data[i]
        mean = (row[1] + row[2] + row[3] + row[4] + row[5]) / 5
        data[i] = np.array((mean, row[6]))

    return data


def normalize_data(data: np.ndarray) -> np.ndarray:
    """Normalizes the stocks data."""

    data = np.swapaxes(data, 0, 1)
    for i in range(len(data)):
        data[i] = (data[i] - min(data[i])) / (max(data[i]) - min(data[i]))
    data = np.swapaxes(data, 0, 1)
    return data


def split_data(data) -> (np.ndarray, np.ndarray):
    """Split dataset and format it for the lstm model"""

    x, y = [], []
    for i in range(LOOKBACK, len(data)):
        x.append(data[i-LOOKBACK:i])
        y.append(data[i])
    return np.array(x), np.array(y)


def get_model():
    """Defines LSTM model"""

    model = keras.Sequential()
    model = keras.models.Sequential([
        keras.layers.LSTM(128, input_shape=(
            LOOKBACK, 2), return_sequences=True),
        keras.layers.Dropout(0.3),
        keras.layers.LSTM(64, input_shape=(LOOKBACK, 2),
                          return_sequences=False),
        keras.layers.Dropout(0.3),
        keras.layers.Dense(2, activation='relu')])
    return model


def predict_on_stocks(stocks_path: str, store_path: str, models_path: str):
    """Write predictions of stocks_path files to store_path

    Args:
        stocks_path: Path where the known stocks are stored (dataset)
        store_path: Path where to store the predictions
        models_path: Path where to store the trained models

    Example:
        >>> predict_on_stocks('./stocks', './predictions', './models')
    """

    import logging
    logging.disable(logging.WARNING)
    os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

    dirs = os.listdir(stocks_path)
    nb_predictions = len(dirs)

    for i, file in enumerate(dirs):
        print_advancement(os.path.join(stocks_path, file), i, nb_predictions)

        data = pd.read_csv(os.path.join(stocks_path, file)).to_numpy()
        data = filter_data(data)
        data = normalize_data(data)

        model = get_model()
        model.compile(optimizer='adam', loss='mse')

        x_train, y_train = split_data(data)
        model.fit(x=x_train, y=y_train,
                  epochs=EPOCHS,
                  verbose=0,
                  batch_size=32,
                  callbacks=[PrintLogs(EPOCHS)])

        model_name = os.path.join(
            models_path, os.path.splitext(file)[0] + '.h5')
        model.save(model_name)

        if i == len(dirs):
            print_advancement(os.path.join(
                stocks_path, file), i, nb_predictions)
