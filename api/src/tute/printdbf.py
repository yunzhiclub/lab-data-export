from dbfService import DbfService

# 在此输入要打印的dbf文件
filepaths = ['./x_symc(1).DBF', './x_syxm(1).DBF']
for filepath in filepaths:
    dbf = DbfService(filepath)
    dbf.print()
    dbf.close()