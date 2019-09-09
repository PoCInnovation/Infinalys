from tqdm import trange
import pandas as pd
import yfinance as yf
from os import path
from random import choice as rchoice


def _get_proxies(path: str) -> list:
    with open(path, 'r') as f:
        proxies = [row.strip('\n') for row in f]
        return proxies


def download_stocks(companies_path: str, dl_path: str, proxies_path: str = None, max_dl: int = 0):
    """
    Args:
        companies_path: Represents the filepath to the file listing the
            companies name (ticker name). It's waiting for a csv, and
            will read the first column.
        dl_path: Filepath to indicate where to store the downloaded stocks.
        proxies_path: Filepath to indicate the proxies to take
        max_dl: Maximun number of files to download, 0 if there is no limit
    """
    assert max_dl >= 0, 'Argument max_dl must be >= 0.'

    if proxies_path != None:
        proxies = _get_proxies(proxies_path)

    downloads = 0
    with open(companies_path, 'r') as f:
        f.readline()
        for i, row in enumerate(f):

            symbol = row.split(',')[0].strip('\n')

            if proxies_path is not None:
                proxy = rchoice(proxies)
                print(f'{i} - Downloading {symbol} on proxy {proxy} ...')
                stock = yf.download(symbol, proxy=proxy)
            else:
                print(f'{i} - Downloading {symbol} on proxy 0.0.0.0 ...')
                stock = yf.download(symbol)

            if stock.shape[0] > 2:
                stock_name = path.join(dl_path, symbol + '.csv')
                stock.to_csv(stock_name)
                downloads += 1
            else:
                print(f'Couldn\'t download stock {symbol}')

            if max_dl != 0 and downloads - 1 == max_dl:
                break

        print(f'Downloaded {downloads} stocks.')
