import dbf


# https://github.com/ethanfurman/dbf/tree/master/dbf
class DbfService:
    table = None

    # 清空原表
    def clear(self):
        message = '开始清空原表:' + self.table.filename
        logs = message
        print(message)
        for record in self.table:
            dbf.delete(record)
        self.table.pack()
        message = '清空原表完成'
        logs += message
        print(message)
        return logs

    def __init__(self, filename: str):
        self.table = dbf.Table(filename)
        self.table.open(dbf.READ_WRITE)

    def print(self):
        logs = ""
        for record in self.table:
            logs += str(record)
            print(record)
        return logs

    def close(self):
        self.table.close()
