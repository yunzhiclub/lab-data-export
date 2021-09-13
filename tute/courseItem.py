from tute.course import Course


# 实验项目
class CourseItem:
    id = ''
    name = ''
    __course = Course()
    classHour = 0
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

    def get_course(self):
        return self.__course
