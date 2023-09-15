from .courseItem import CourseItem


# 实验项目
class CourseItemService:

    # 将excel表中的数据映射为CourseItem[]
    def get_course_items_from_sheet(self, sheet, course):
        course_items = []
        for i in sheet.index:
            row = sheet.loc[i]
            course_item = CourseItem()
            course_item.set_course(course)
            course_item.id = row[0]
            course_item.name = str(row[1]).strip()
            course_item.classHour = row[2]
            course_item.testerLengthPerGroup = row[3]
            course_item.testType = str(row[4]).strip()
            course_item.testRequirements = str(row[5]).strip()
            course_items.append(course_item)

        return course_items

    # 合并课程相同且实验名称相同的实验项目
    # @param courses_items CourseItem[]
    # @return {课程号+实验项目名称: CourseItem}
    def merge_and_add_id(self, courses_items):
        # 合并去重，计算总实现人数
        result = {}
        for courses_item in courses_items:
            key = str(courses_item.get_course().id) + str(courses_item.name)
            if key in result:
                # 重复击中，则增加实验人数
                temp_course_item = result[key]
                temp_course_item.testerTotalCount += courses_item.testerTotalCount
            else:
                result[key] = courses_item
        return self.add_id(result)

    # 添加id
    # @params courses_items
    # {课程号+实验项目名称：CourseItem}
    # @return
    # {课程号+实验项目名称：CourseItem ->{id: 课程编号+2位序号} }
    def add_id(self, courses_items):
        ids = {}
        for key in courses_items:
            course_item = courses_items[key]
            course_id = course_item.get_course().id
            if course_id in ids:
                ids[course_id] = ids[course_id] + 1
            else:
                ids[course_id] = 1
            index = ids[course_id]
            if index >= 10:
                item_id = str(index)
            else:
                item_id = '0' + str(index)
            course_item.id = str(courses_items[key].get_course().id) + item_id
        return courses_items
