import csv
import operator
import os


def get_data(file='comtrade_trade_data.csv'):
    with open(file) as f:  # 'comtrade_trade_data.csv'
        reader = csv.DictReader(f)
        data = [[row['Year'], row['Reporter Code'], row['Partner Code'], row['Trade Flow Code']] for row in reader]
    return data


def remove_invalid_data(data):
    i = 0
    while i < len(data):
        if data[i][3] == '3' or data[i][3] == '4' or date[i][1] == '0' or date[i][2] == '0':
            del data[i]
        else:
            i += 1
    return data


def transfer_data(data):
    i = 0
    while i < len(data):
        if data[i][3] == '1':
            data[i][3] = '2'
            data[i][1], data[i][2] = data[i][2], data[i][1]
        i += 1
    return data


def merge_data(data):
    data.sort(key=lambda x: (int(x[0]), int(x[1]), int(x[2])))  # lambda x: (int(x[0]), int(x[1]), int(x[2])) operator.itemgetter(0, 1, 2)
    i = 0
    while i < (len(date) - 1):
        if date[i] == date[i + 1]:
            del date[i + 1]
        else:
            i += 1
    return date


def save_date(data, filename='result'):
    basefile = os.path.curdir
    filepath = os.path.join(basefile, filename)
    temp = '0000'
    for each in date:
        perfile = each[0]
        if perfile != temp:
            if temp == '0000':
                pass
            else:
                f.close()
            filede = os.path.join(filepath, perfile)
            f = open(filede, 'a')
            f.write(each[1] + ' ' + each[2] + ' {\'weight\':' + each[3] + '}\n')
        else:
            f.write(each[1] + ' ' + each[2] + ' {\'weight\':' + each[3] + '}\n')
            temp = perfile
    f.close()


if __name__ == '__main__':
    date = get_data()
    remove_invalid_data(date)
    transfer_data(date)
    merge_data(date)
    save_date(date)
