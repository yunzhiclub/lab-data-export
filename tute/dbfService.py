import dbf


# https://github.com/ethanfurman/dbf/tree/master/dbf
class DbfService:
    table = None

    # 清空原表
    def clear(self, table):
        for record in table:
            print(record)
            dbf.delete(record)
        table.pack()

    def __init__(self, filename: str):
        self.table = dbf.Table(filename)
        self.table.open(dbf.READ_WRITE)

    def print(self):
        for record in self.table:
            print(record)

    def close(self):
        self.table.close()
