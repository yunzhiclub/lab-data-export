
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
    # 网络实验(0非，1是）
    netTest = '非'
    # 实验类型(1基础，2专业基础，3专业，4科研)
    courseType = '专业'
    # 实验室名称
    unitName = '软件应用实验室'

    def __repr__(self):
        return self.name + self.unitName
