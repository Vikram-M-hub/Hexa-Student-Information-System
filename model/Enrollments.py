class Enrollment:
    def __init__(self, student_id, course_id, enrollment_date):
        self.enrollment_id = hash((student_id, course_id, enrollment_date))
        self.student_id = student_id
        self.course_id = course_id
        self.enrollment_date = enrollment_date