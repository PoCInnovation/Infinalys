import os
import sys
import numpy as np
import pandas as pd
from os.path import join as pjoin

EPOCHS = 1
LOOKBACK = 5
PREDICT = 5
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
    print(f'Predicting on file {file} ...', end='')
    sys.stdout.flush()


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


def predict_on_stocks(stocks_path: str, store_path: str, models_path: str):
    """Write predictions of stocks_path files to store_path

    Args:
        stocks_path: Path where the known stocks are stored (dataset)
        store_path: Path where to store the predictions
        models_path: Path where to store the trained models

    Example:
        >>> predict_on_stocks('./stocks', './predictions', './models')
    """

    dirs = os.listdir(stocks_path)
    nb_predictions = len(dirs)

    for i, file in enumerate(dirs):
        print_advancement(pjoin(stocks_path, file), i, nb_predictions)

        data = pd.read_csv(pjoin(stocks_path, file)).to_numpy()
        data = filter_data(data)
        data = normalize_data(data)

    # Generate a prediction (cf wiki Irma) in store_path

    # TODO Model:
    #   faire la moyene de open high low close -> [mean, volumes]
