import csv
import matplotlib.pyplot as plt

if __name__ == "__main__":
    with open("../dataset/BORDEAUX_14-18.csv") as f:
        dataset = csv.reader(f)
        f.readline()
        points = [(int(line[2]), int(line[8])) for line in dataset]
        points.sort(key=lambda x: x[0])
    prices = [x[0] for x in points]
    surfaces = [x[1] for x in points]

    plt.xlabel("nombre pièces")
    plt.ylabel("prices")

    plt.scatter(surfaces, prices, s=0.1)
    plt.show()
