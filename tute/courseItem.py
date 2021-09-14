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
    # 实验类型 (演示型1, 验证性2、综合性3）
    testType = ''
    # 实验要求 2选修 1必修 3其它
    testRequirements = ''

    def set_course(self, course):
        self.__course = course
        self.testerTotalCount = course.testerNumber

    def get_course(self):
        return self.__course
