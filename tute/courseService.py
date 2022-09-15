from course import Course


class CourseService:
    # 由excel表中获取所有课程信息
    def get_course_from_excel(self, excel) -> list:
        courses = []
        for i in excel.index:
            row = excel.loc[i]
            courseobject = Course()
            courseobject.fileNo = row[0]
            courseobject.id = str(row[1])
            # 课程编号固定为6位
            while len(courseobject.id) < 6:
                courseobject.id = '0' + courseobject.id
            courseobject.name = row[2]
            courseobject.semester = row[3]
            courseobject.property = row[4]
            courseobject.classHour = row[6]
            courseobject.testerNumber = row[9]
            courseobject.type = row[12]

            if str(row[14]).strip() == '是':
                courseobject.netTest = '是'
            if str(row[15]).strip() in ['基础', '专业基础', '专业', '科研']:
                courseobject.courseType = str(row[15]).strip()
            if len(str(row[16]).strip()) > 0 and str(row[16]).strip() != 'nan':
                courseobject.unitName = str(row[16]).strip()
            courses.append(courseobject)
        return courses
