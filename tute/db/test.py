import datetime


# 实验项目
class Test:
    # 实验序号
    id = ''
    # 实验名称
    name = ''
    # 课程编号
    courseId = ''
    # 课程名称
    courseName = ''
    # 实验类别
    courseType = ''
    # 计划学时数
    classHour = 0.0
    # 每组人数
    peopleLengthPerGroup = 1
    # 实验要求
    testRequirements = '2'
    # 实验类型
    testType = '2'
    # 网络实验
    netTest = '0'
    # 设课方式
    teachingMode = '0'
    # 专业分类号
    majorId = '0809'
    # 专业名称
    majorName = '计算机类'
    # 实验套数
    suiteCount = 0
    # 单位编号
    unitId = '042012'
    # 单位名称(软件应用实验室)
    unitName = '软件应用实验室'
    # 实验数字1
    testNumber1 = 0.0
    # 实验数字2
    testNumber2 = 0.0
    # 校区
    schoolNumber = '0'
    # 输入日期
    inputDate = datetime.datetime(2021, 9, 11, 0, 0)
    # 审核
    checked = '0'
    # 审核日期
    checkDate = datetime.date(2021, 9, 11)

    # @param course_item CourseItem
    def __init__(self, course_item):
        self.id = course_item.id
        self.name = course_item.name
        course = course_item.get_course()
        self.courseId = str(course.id)
        self.courseName = str(course.name)
        print(course.type)
        # self.courseType = str(course.type)
        self.classHour = course_item.classHour
        self.peopleLengthPerGroup = course_item.testerLengthPerGroup
        self.testRequirements = str(course_item.testRequirements)
        self.testType = str(course_item.testType)
        self.suiteCount = course_item.testerTotalCount

    def to_record(self):
        return {
            '实验序号': self.id,
            '实验名称': self.name,
            '课程编号': self.courseId,
            '课程名称': self.courseName,
            '实验类别': self.courseType,
            '计划学时数': self.classHour,
            '每组人数': self.peopleLengthPerGroup,
            '实验要求': self.testRequirements,
            '实验类型': self.testType,
            '网络实验': self.netTest,
            '设课方式': self.teachingMode,
            '专业分类号': self.majorId,
            '专业名称': self.majorName,
            '实验套数': self.suiteCount,
            '一次性材料': 0,
            '非一次材料': 0,
            '材料费合计': 0,
            '专用设备费': 0,
            '公用设备费': 0,
            '单位编号': self.unitId,
            '单位名称': self.unitName,
            '实验数字1': self.testNumber1,
            '实验数字2': self.testNumber2,
            '校区': self.schoolNumber,
            '输入日期': self.inputDate,
            '审核': self.checked,
            '审核日期': self.checkDate
        }
