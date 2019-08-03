from DVFget import DVF, no_null_real_price
from trainIA import trainIA

import numpy as np

datasetPath = "./data/sample/prices_2018"


def getData():
    # 17, 18, 36, literals to process
    cols = {10, 16, 34, 35, 38, 39, 42}
    data = DVF.get_by_column(datasetPath, cols, no_null_real_price)
    normalize(data)

    nbHouses = len(data)
    nbTrain = round(0.8 * nbHouses)
# TODO shuffle all data
    xTrain = np.array([line[1:] for line in data[:nbTrain]])
    yTrain = np.array([line[0] for line in data[:nbTrain]])

    xTest = np.array([line[1:] for line in data[nbTrain:]])
    yTest = np.array([line[0] for line in data[nbTrain:]])

    return (xTrain, yTrain), (xTest, yTest)


def normalize(data):
    nbRow = len(data)

    for i in range(len(data[0])):
        col = np.array([float(elem[i]) for elem in data])
        mean = float(np.mean(col))
        std = float(np.std(col))
        if std == 0:
            std = 1
        for j in range(nbRow):
            data[j][i] = (float(data[j][i]) - mean) / std


if __name__ == "__main__":
    train, test = getData()
    trainIA(train, test)
