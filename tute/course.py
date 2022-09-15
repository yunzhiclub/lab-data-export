from config import Config


class Course:
    # 原始档案编号
    fileNo = '0'
    # 课程编号
    id = '0'
    # 课程名
    name = ''
    # 学期
    semester = 0
    # 课程属性 1必修, 2选修, 3其它
    property = ''
    # 实验学时
    classHour = 0
    # 学生人数
    testerNumber = 0
    # 课程分类
    type = 0
    # 是否网络实验
    netTest = '0'
    # 实验类型(1基础，2专业基础，3专业，4科研)
    courseType = '3'
    # 实验室名称
    unitName = ''

    def __repr__(self):
        return self.name

    # default constructor
    def __init__(self):
        conf = Config()
        self.netTest = config.netTest
        self.courseType = config.courseType
        self.unitName = config.unitName
