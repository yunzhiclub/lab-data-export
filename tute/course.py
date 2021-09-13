

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
    property = 0
    # 实验学时
    classHour = 0
    # 学生人数
    testerNumber = 0
    # 课程分类
    type = 0

    def __repr__(self):
        return self.name


