import pandas
from courseService import CourseService
from courseItemService import CourseItemService
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
        print(len(coursesItems))

    # 合并数据
    course_result_items = courseItemService.merge(coursesItems)

    print(course_result_items)

    # 写入实验项目
    dbf = DbfService(x_xymc)
    for key in course_result_items:
        course_result_item = course_result_items[key]
        print(course_result_item)
    dbf.close()

