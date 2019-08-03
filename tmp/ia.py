import keras
import re, sys
import numpy as np
from keras.layers import Dense, Dropout

CITY_COLUMN = 17
PRICE_COLUMN = 10
NO_INFO_TRANSACTION = 'None'


def get_transactions_raw_by_city(filename, city):
    with open(filename, 'r') as file:
        return [line for line in file if line.split('|')[CITY_COLUMN] == city]


def get_key_tab(tab):
    line_len = len(tab[0])
    key_tab = []
    new = []
    for i in range(line_len):
        key_tab.append([])
    for line in tab:
        i = 0
        new.append([])
        for column in line:
            if not (column in key_tab[i]):
                key_tab[i].append(column)
            new[len(new) - 1].append(key_tab[i].index(column))
            i += 1
        i = 0
    return new


def format_transactions(transactions_raw):
    transactions = []
    for line in transactions_raw:
        line = line.split('|')
        if line[PRICE_COLUMN] == '':
            continue
        for i in range(len(line)):
            line[i] = NO_INFO_TRANSACTION if line[i] == '' else line[i]
            line[i] = re.sub(r'\W+', '', line[i])
        transactions.append(line)
    return transactions


def remove_price(transactions):
    prices = []
    for line in transactions:
        prices.append(line[PRICE_COLUMN])
        del line[PRICE_COLUMN]
    prices = list(map(lambda x: float(x) / 100, prices))
    return transactions, prices


def norm(nparr):
    return (nparr - nparr.mean()) / nparr.std()


def get_transactions(filename):
    with open(filename, 'r') as file:
        transactions_raw = [line for line in file]
    print(f'[*] Read {filename}')
    transactions = format_transactions(transactions_raw)
    print('[*] Formatted transactions')
    transactions, prices = remove_price(transactions)
    print('[*] Removed prices')
    hashed_transactions = get_key_tab(transactions)
    print('[*] Hashed transactions')
    return norm(np.array(hashed_transactions)), norm(np.array(prices))


def run_ai(train, test):
    model = keras.models.Sequential()
    model.add(Dense(512, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(512, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(1, activation='softmax'))
    model.compile(loss='cosine_proximity',
                  optimizer=keras.optimizers.adam(lr=0.1),
                  metrics=['accuracy'])
    model.fit(x=np.array(train[0]), y=np.array(train[1]), epochs=10)
    # score = model.evaluate(test[0], test[1], verbose=0)
    # print('Test loss:', score[0])
    # print('Test accuracy:', score[1])


if __name__ == '__main__':
    train = get_transactions('train.txt')
    test = get_transactions('test.txt')
    run_ai(train, test)
