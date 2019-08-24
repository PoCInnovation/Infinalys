import numpy as np


class Stock():

    def __init__(self, filename, verbose=False, name=None):

        self.verbose = verbose
        self.filename = filename

        self.stocks = dict()
        self.header = None
        self._get_stocks()
        self._normalize()

    def _get_stocks(self):
        with open(self.filename, 'r') as f:
            self.header = f.readline().strip('\n').split(',')

            for column_type in self.header:
                self.stocks[column_type] = []

            for line in f:
                line = line.strip('\n')
                line = line.split(',')
                for column_type, value in zip(self.header, line):
                    self.stocks[column_type].append(value)
            for key in self.stocks:
                try:
                    self.stocks[key] = np.array(
                        list(map(float, self.stocks[key])))
                except Exception as e:
                    if self.verbose:
                        print(f"Using key [{key}], {e}")
                    pass

    def _normalize(self):
        for key in self.stocks:
            if type(self.stocks[key]) is np.ndarray:
                minimum = min(self.stocks[key])
                frame = max(self.stocks[key]) - minimum
                self.stocks[key] = (self.stocks[key] - minimum) / frame
                print(self.stocks[key].sum())

    def __getitem__(self, arg):
        return self.stocks[arg]


tesla = Stock("../dataset/tesla_stocks.csv")
print(tesla['High'])
