import datetime
from config import Config


# 实验项目
class Map:
    # 实验序号
    id = ''
    # 实验名称
    name = ''
    # 课程编号
    courseId = ''
    # 课程名称
    courseName = ''
    # 实验类别(1基础，2专业基础，3专业，4科研）
    courseType = '3'
    # 计划学时数
    classHour = 0.0
    # 实际学时数
    actualClassHour = 0.0
    # 每组人数
    peopleLengthPerGroup = 1
    # 实验要求(2选修，1必修）
    testRequirements = '1'
    # 实验类型(1演示型、2验证型、3综合型）
    testType = '3'
    # 网络实验(0非，1是）
    netTest = '0'
    # 设课方式(0非独立授课，1独立授课）
    teachingMode = '0'
    # 专业分类号
    majorId = '0809'

    # 材料消耗费
    material = 0.0
    # 实验要求
    testRequirement = '0'
    # 获奖等级(0未获奖)
    awardLevel = '0'

    # 实验者人数
    testerCount = 0
    # 实验者类别（3本科生）
    testerType = '3'
    # 实验者对象(1校内）
    testerObject = '1'
    # 循环次数
    cycleIndex = 1

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
    datetime_now = datetime.datetime.now()
    # 审核
    checked = '1'
    # 审核日期
    date_now = datetime.datetime.now().date()

    # @param course_item CourseItem
    def __init__(self, course_item):
        self.id = course_item.id
        self.name = course_item.name
        course = course_item.get_course()
        self.courseId = str(course.id)
        # 课程编号的长度固定为6位
        while len(self.courseId) < 6:
            self.courseId = '0' + self.courseId

        self.courseName = str(course.name)
        self.actualClassHour = course_item.classHour
        self.peopleLengthPerGroup = course_item.testerLengthPerGroup

        if course_item.testRequirements in ['必修', '必做']:
            self.testRequirements = '1'
        elif course_item.testRequirements == ['选修', '选做']:
            self.testRequirements = '2'
        else:
            self.testRequirements = '3'

        if course_item.testType == '演示型' or course_item.testType == '演示性' or course_item.testType == '演示':
            self.testType = '1'
        elif course_item.testType == '验证型' or course_item.testType == '验证性' or course_item.testType == '验证':
            self.testType = '2'
        elif course_item.testType == '综合型' or course_item.testType == '综合性' or course_item.testType == '综合':
            self.testType = '3'
        elif course_item.testType == '设计研究' or course_item.testType == '设计性' or course_item.testType == '设计性'\
                or course_item.testType == '设计':
            self.testType = '4'
        else:
            self.testType = '5'


        # 是否网络实验
        if course_item.get_course().netTest == '是':
            self.netTest = '1'

        # 实验类别(1基础，2专业基础，3专业，4科研）
        courseType = course_item.get_course().courseType
        if courseType == '基础':
            self.courseType = '1'
        elif courseType == '专业基础':
            self.courseType = '2'
        elif courseType == '科研':
            self.courseType = '4'



        self.testerCount = course_item.testerTotalCount
        

        conf = Config()
        # 设课方式(0非独立授课，1独立授课）
        self.teachingMode = conf.teachingMode
        # 专业分类号
        self.majorId = conf.majorId
        # 专业名称
        self.majorName = conf.majorName
        # 单位名称
        self.unitName = course_item.get_course().unitName
        # 单位编号
        if self.unitName not in list(conf.units.values()):
            raise RuntimeError('实验室名称:' + self.unitName + '未找到')
        self.unitId = list(conf.units.keys())[list(conf.units.values()).index(self.unitName)]

        # 实验套数
        self.suiteCount = conf.suiteCount
        # 循环次数
        self.cycleIndex = -(self.testerCount // -self.suiteCount)

    # 转化为symc库
    def to_symc(self):
        return {
            '实验序号': self.id,
            '实验名称': self.name,
            '课程编号': self.courseId,
            '课程名称': self.courseName,
            '实验类别': self.courseType,
            '计划学时数': self.actualClassHour,
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
            '输入日期': self.datetime_now,
            '审核': self.checked,
            '审核日期': self.date_now
        }

    # 转化为实验项目
    def to_syxm(self):
        return {
            '实验序号': self.id,
            '实验名称': self.name,
            '课程编号': self.courseId,
            '课程名称': self.courseName,
            '设课方式': self.teachingMode,
            '实验类别': self.courseType,
            '实验者人数': self.testerCount,
            '实验者类别': self.testerType,
            '实验者对象': self.testerObject,
            '每组人数': self.peopleLengthPerGroup,
            '计划学时数': self.actualClassHour,
            '实际学时数': self.actualClassHour,
            '材料消耗费': self.material,
            '实验要求': self.testRequirements,
            '获奖等级': self.awardLevel,
            '实验类型': self.testType,
            '网络实验': self.netTest,
            '变动状况': '0',
            '单位编号': self.unitId,
            '单位名称': self.unitName,
            '专业分类号': self.majorId,
            '专业名称': self.majorName,
            '教师编号': '',
            '任课教师': '',
            '授课班级': '',
            '授课专业': '',
            '实验地编号': '',
            '实验地名称': '',
            '循环次数': self.cycleIndex,
            '项目数字1': self.testNumber1,
            '项目数字2': self.testNumber2,
            '项目字符1': '',
            '项目字符2': '',
            '项目字符3': '',
            '备注': '',
            '校区': self.schoolNumber,
            '标志': '',
            '内部编号': '',
            '输入人': '',
            '输入日期': self.datetime_now,
            '审核人': '',
            '审核日期': self.datetime_now,
            '审核': self.checked,
        }
