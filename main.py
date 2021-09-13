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




def start():
    # 打开原始库
    table = dbf.Table(filename='/Users/panjie/sync/work/x_symc.DBF')
    table.open(dbf.READ_WRITE)
    clear(table)
    table.close()


# 清空原表
def clear(table):
    for record in table:
        print(record)
        dbf.delete(record)
    table.pack()


if __name__ == '__main__':
    test()
