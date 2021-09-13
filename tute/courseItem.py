# 实验项目
from tute.course import Course


class CourseItem:
    id = 0
    name = ''
    __course = Course()
    classHours = 0
    # 每组人数
    testerLengthPerGroup = 1
    # 实验人数
    testerTotalCount = 0
    # 实验类型 (验证性、综合性）
    testType = 1
    # 实验要求 2必做
    testRequirements = 2

    def set_course(self, course):
        self.__course = course
        self.testerTotalCount = course.testerNumber
