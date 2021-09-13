from courseItem import CourseItem


# 实验项目
class CourseItemService:
    def get_course_items_from_sheet(self, sheet, course):
        course_items = []
        for i in sheet.index:
            row = sheet.loc[i]
            course_item = CourseItem()
            course_item.set_course(course)
            course_item.id = row[0]
            course_item.name = row[1]
            course_item.classHours = row[3]
            course_item.testerLengthPerGroup = row[4]
            if row[5] == '验证型':
                course_item.testType = 2
            else:
                course_item.testType = 1
            if row[6] == '必做':
                course_item.testRequirements = 2
            course_items.append(course_item)
        return course_items
