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
            courses.append(courseobject)
        return courses
