import pandas
import dbf
from courseService import CourseService
from courseItemService import CourseItemService
import numpy as np


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
    # 读EXCEL
    courseService = CourseService()
    filename = '/Users/panjie/sync/work/task.xls'
    excel = pandas.ExcelFile(filename)
    sheet0 = pandas.read_excel(excel)
    courses = courseService.get_course_from_excel(sheet0)

    coursesItems = []
    courseItemService = CourseItemService()

    # 根据course读取实验项目
    for course in courses:
        sheet = pandas.read_excel(excel, str(course.fileNo))
        coursesItems.extend(courseItemService.get_course_items_from_sheet(sheet, course))
        print(len(coursesItems))

    # 合并去重，计算总实现人数

