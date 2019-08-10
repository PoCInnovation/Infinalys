from dvf import DVF


def create_new_dataset(newfile, filenames, columns, condition_func, desc=None):

    with open(newfile, "w") as f:
        if desc is not None:
            f.write(f"{desc}\n")
        for file in filenames:
            data = DVF.get_by_column(file, columns, condition_func)
            block = [f"{line[0]},{line[1]},{line[2]},{line[3]},{line[4]},{line[5]},{line[6]},{line[7]},{line[8]},{line[9]}\n"[6:] for line in data]
            f.writelines(block)


def condition_func(line, indexes):

    for i in indexes:
        if line[i] == '':
            return False

    line[10] = line[10][:-3]
    price = int(line[10])
    if price < 10000:
        return False
    if line[17] != 'BORDEAUX':
        return False
    if int(line[42]) >= 5000:
        return False
    return True

if __name__ == "__main__":
    desc = "Date de Vente, Nature de la vente, Prix, Numero de voie, Type de voie, Nom de voie, Code postal, Code type local, Surface réelle bati, Surface terrain"
    new_filename = "BORDEAUX_14-18.csv"
    cols = {8, 9, 10, 11, 13, 15, 16, 35, 38, 42}
    filenames = ["../../../data/sample/prices_2014",
                 "../../../data/sample/prices_2015",
                 "../../../data/sample/prices_2016",
                 "../../../data/sample/prices_2017",
                 "../../../data/sample/prices_2018"]

    create_new_dataset(new_filename, filenames, cols, condition_func, desc)
