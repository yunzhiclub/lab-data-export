import pandas
import dbf

from tute.dbfService import DbfService


if __name__ == '__main__':
    x_xymc = '/Users/panjie/sync/work/x_syxm.DBF'
    # 写入实验项目
    dbf = DbfService(x_xymc)
    dbf.print()
    dbf.close()
