import sys

import pandas
import pprint
from courseService import CourseService
from courseItemService import CourseItemService
from map import Map
from dbfService import DbfService
pp = pprint.PrettyPrinter(indent=4)

if __name__ == '__main__':
    task_filename = './task.xls'
    symc_filename = './x_symc.dbf'
    syxm_filename = './x_syxm.dbf'


    # 读EXCEL
    courseService = CourseService()
    excel = pandas.ExcelFile(task_filename)
    sheet0 = pandas.read_excel(excel)
    courses = courseService.get_course_from_excel(sheet0)

    print('-------------------------------  获取的实验课程数据 ------------------------------- ')
    pp.pprint(courses)

    coursesItems = []
    courseItemService = CourseItemService()

    # 根据course读取实验项目
    for course in courses:
        sheet = pandas.read_excel(excel, str(course.fileNo) + '-' + str(course.semester))
        coursesItems.extend(courseItemService.get_course_items_from_sheet(sheet, course))

    print('-------------------------------  原始实验项目(' + str(len(coursesItems)) + ')数据如下 ------------------------------- ')
    for courseItem, index in enumerate(coursesItems):
        print(courseItem, index)

    # 合并数据
    course_result_items = courseItemService.merge_and_add_id(coursesItems)

    print('-------------------------------  合并后的项目(' + str(len(course_result_items)) + ')数据如下 ------------------------------- ')
    for courseResultItem, index in enumerate(course_result_items):
        print(courseResultItem, index)

    # 映射数据
    maps = []
    for key in course_result_items:
        course_result_item = course_result_items[key]
        maps.append(Map(course_result_item))

    print('准备写入dbf的项目数量为:' + str(len(maps)))
    print('------------------------------- 开始写入实验明细 ---------------------------')
    dbf = DbfService(symc_filename)
    dbf.clear()
    error = 0
    for m in maps:
        try:
            dbf.table.append(m.to_symc())
        except BaseException as exception:
            print('将数据写库时发生错误:', m.to_symc())
            print('错误信息:', exception)
            error = 1
            break
    if error == 1:
        dbf.close()
        sys.exit()

    print('------------------------------- 写入完成，实验名细信息如下： ---------------------------')
    dbf.print()
    dbf.close()

    print('------------------------------- 开始写入实验项目 ---------------------------')
    dbf = DbfService(syxm_filename)
    dbf.clear()
    for m in maps:
        dbf.table.append(m.to_syxm())
    print('-------------------------------  写入完成，实验项目信息如下： ---------------------------')
    dbf.print()
    dbf.close()

    print('')
    print('--- 操作 😀 😃 😄 😁 😆 😅 😂 🤣 ☺️ 😊 😇 🙂 🙃 😉 😌 成功 ---')
    print('请复制x_symc.dbf及x_syxm.dbf两个数据库并进行下一步操作')