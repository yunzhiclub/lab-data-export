import pandas
import dbf


def test():
    filename = '/Users/panjie/sync/work/task.xls'
    excel = pandas.read_excel(filename)
    print(excel.index)
    print(excel.columns)
    print(excel.shape)

    courses = []
    for i in excel.index:
        row = excel.loc[i]
        print(row[0])


if __name__ == '__main__':
    test()
