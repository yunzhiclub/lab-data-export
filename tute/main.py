import pandas
from courseService import CourseService
from courseItemService import CourseItemService
from tute.db.test import Test
from tute.dbfService import DbfService

if __name__ == '__main__':
    filename = '/Users/panjie/sync/work/task.xls'
    x_xymc = '/Users/panjie/sync/work/x_symc.DBF'

    # 读EXCEL
    courseService = CourseService()
    excel = pandas.ExcelFile(filename)
    sheet0 = pandas.read_excel(excel)
    courses = courseService.get_course_from_excel(sheet0)

    coursesItems = []
    courseItemService = CourseItemService()

    # 根据course读取实验项目
    for course in courses:
        sheet = pandas.read_excel(excel, str(course.fileNo))
        coursesItems.extend(courseItemService.get_course_items_from_sheet(sheet, course))

    print('共有实验项目数量:' + str(len(coursesItems)))

    # 合并数据
    course_result_items = courseItemService.merge_and_add_id(coursesItems)

    print('合并后的项目数量:' + str(len(course_result_items)))

    # 映射数据
    tests = []
    for key in course_result_items:
        course_result_item = course_result_items[key]
        tests.append(Test(course_result_item))

    print('整理成可写入dbf的项目数量:' + str(len(tests)))

    # 写入实验项目
    dbf = DbfService(x_xymc)
    for test in tests:
        dbf.table.append(test.to_record())
    # dbf.print()
    dbf.close()
