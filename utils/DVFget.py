from inspect import currentframe, getframeinfo


class DVF():

    @staticmethod
    def get_by_column(file, indexes=None, is_valid=None, max=-1):
        """ file: raw dataset
            indexes: a set which describes the columns to extract from the file
            is_valid: functions which takes a splited line as parameter and
                      outputs a boolean at True if the line should be taken

            Extracts the indexes columns from the dataset file
        """

        if type(indexes) != set:
            frameinfo = getframeinfo(currentframe())
            print(
                f"./{__file__}:{frameinfo.lineno} :Expected a set, received a {type(indexes)}.")
            exit(1)

        indexes = sorted(indexes)

        result = []
        count = 0
        with open(file, "r") as f:
            for line in f:
                if max >= 0 and count == max:
                    break
                line = line[:-1]
                line = line.split('|')
                if is_valid != None and not is_valid(line, indexes):
                    continue
                count += 1
                if indexes != None:
                    result.append([line[i] for i in indexes])
                else:
                    result.append(line)
        return result


def no_null_real_price(line, indexes):

    for i in indexes:
        if line[i] == '':
            return False

    line[10] = line[10][:-3]
    if int(line[10]) < 10000:
        return False
    if int(line[10]) > 2000000:
        return False
    if line[17] != 'BORDEAUX':
        return False
    if int(line[42]) >= 10000:
        return False
    return True
