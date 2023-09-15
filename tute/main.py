import os
import string
import random
import shutil


import pandas
import pprint
from courseService import CourseService
from courseItemService import CourseItemService
from map import Map
from dbfService import DbfService
pp = pprint.PrettyPrinter(indent=4)


def random_str(length=6):
    return ''.join(random.choices(string.ascii_uppercase +
                           string.digits, k=length))


def start(task_filename='./task_wx.xls'):
    logs = ""
    suffix = random_str()
    symc_filename = './x_symc_' + suffix + '.dbf'
    syxm_filename = './x_syxm_' + suffix + '.dbf'
    shutil.copyfile('./x_symc.dbf', symc_filename)
    shutil.copyfile('./x_syxm.dbf', syxm_filename)

    symc_filename = os.path.abspath(symc_filename)
    syxm_filename = os.path.abspath(syxm_filename)
    files = [symc_filename, syxm_filename]

    # 读EXCEL
    courseService = CourseService()
    excel = pandas.ExcelFile(task_filename)
    sheet0 = pandas.read_excel(excel)
    courses = courseService.get_course_from_excel(sheet0)

    message = '-------------------------------  获取的实验课程数据 ------------------------------- '
    logs += message + '\n'
    print(message)
    logs += str(courses) + '\n'
    pp.pprint(courses)

    coursesItems = []
    courseItemService = CourseItemService()

    # 根据course读取实验项目
    for course in courses:
        message = '开始读取sheet:' + str(course.fileNo) + '-' + str(course.semester)
        logs += message + '\n'
        print(message)
        sheet = pandas.read_excel(excel, str(course.fileNo) + '-' + str(course.semester))
        coursesItems.extend(courseItemService.get_course_items_from_sheet(sheet, course))

    message = '-------------------------------  原始实验项目(' + str(len(coursesItems)) + ')数据如下 ------------------------------- '
    logs += message + '\n'
    print(message)
    for courseItem, index in enumerate(coursesItems):
        message = str(courseItem) + str(index)
        logs += message + '\n'
        print(message)

    # 合并数据
    course_result_items = courseItemService.merge_and_add_id(coursesItems)

    message = '-------------------------------  合并后的项目(' + str(len(course_result_items)) + ')数据如下 ------------------------------- '
    logs += message + '\n'
    print(message)
    for courseResultItem, index in enumerate(course_result_items):
        message = str(courseResultItem) + str(index)
        logs += message + '\n'
        print(message)

    # 映射数据
    maps = []
    for key in course_result_items:
        course_result_item = course_result_items[key]
        maps.append(Map(course_result_item))

    message = '准备写入dbf的项目数量为:' + str(len(maps))
    logs += message + '\n'
    print(message)
    dbf = DbfService(symc_filename)
    logs += dbf.clear()
    error = 0
    for m in maps:
        try:
            dbf.table.append(m.to_symc())
        except BaseException as exception:
            message = '将数据写库时发生错误:' + str(m.to_symc())
            logs += message + '\n'
            print(message)
            message = '错误信息:' + str(exception)
            logs += message + '\n'
            print(message)
            error = 1
            break
    if error == 1:
        dbf.close()
        return True, logs, files

    message = '------------------------------- 写入完成，实验名细信息如下： ---------------------------'
    logs += message + '\n'
    print(message)
    logs += dbf.print() + '\n'
    dbf.close()

    message = '------------------------------- 开始写入实验项目 ---------------------------'
    logs += message + '\n'
    print(message)
    dbf = DbfService(syxm_filename)
    logs += dbf.clear() + '\n'
    for m in maps:
        try:
            dbf.table.append(m.to_syxm())
        except BaseException as exception:
            message = '将数据写库时发生错误:' + str(m.to_syxm())
            logs += message + '\n'
            print(message)
            message = '错误信息:' + str(exception)
            logs += message + '\n'
            print(message)
            error = 1
            break
    message = '-------------------------------  写入完成，实验项目信息如下： ---------------------------'
    logs += message + '\n'
    print(message)
    if error == 1:
        return True, logs, files
    logs += dbf.print() + '\n'
    dbf.close()

    print('')
    message = '--- 操作 😀 😃 😄 😁 😆 😅 😂 🤣 ☺️ 😊 😇 🙂 🙃 😉 😌 成功 ---'
    logs += message + '\n'
    print(message)
    print('请复制' + symc_filename + '及' + syxm_filename + '两个数据库并进行下一步操作')
    return False, logs, [symc_filename, syxm_filename]


if __name__ == '__main__':
    start()