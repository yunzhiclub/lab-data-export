import datetime
import test


# 实现项目
class TestDetail:
    test = test()
    # 实验序号
    testId = ''
    # 实验名称
    testName = ''
    # 课程编号
    courseId = ''
    # 课程名称
    courseName = ''
    # 设课方式
    teachingMode = '0'
    # 实验类别
    courseType = ''
    # 实验者人数
    testerCount = 0
    # 实验者类别
    testerType = '0'
    # 实验者对象
    testerObject = '0'
    # 每组人数
    peopleLengthPerGroup = 1
    # 循环次数
    cycleCount = 2
    # 计划学时数
    plannedClassHour = 0.0
    # 实际学时数
    actualClassHour = 0.0
    # 材料消耗费
    material = 0.0
    # 实验要求
    testRequirement = '1'
    # 获奖等级
    awardLevel = '0'
    # 实验类型
    testType = '0'
    # 网络实验
    netTest = '0'
    # 变动状况
    changeType = '0'
    # 单位编号
    unitId = '042012'
    # 单位名称(软件应用实验室)
    unitName = ''
    # 专业分类号
    majorId = '0809'
    # 专业名称
    majorName = '计算机类'
    # 校区
    schoolNumber = '0'
    # 输入日期
    inputDate = datetime.datetime(2021, 9, 11, 0, 0)
    # 审核
    checked = '0'
    # 审核日期
    checkDate = datetime.date(2021, 9, 11)
