import datetime
from model.Student import Student
from model.Course import Course
from model.Enrollments import Enrollment
from model.Payment import Payment
from model.Teacher import Teacher


student1 = Student(1, "John", "Doe", datetime.datetime(1995, 8, 15), "john.doe@example.com", "123-456-7890")
course1 = Course(101, "Introduction to Programming", "CS101", "Dr. Smith")
teacher1 = Teacher(1, "Dr.", "Smith", "dr.smith@example.com")
payment1 = Payment(1, 500.00, datetime.datetime(2023, 4, 10))

student1.enroll_in_course(course1)
print(student1.get_enrolled_courses())

student1.update_student_info("John", "Doe", datetime.datetime(1995, 8, 15), "john.doe@example.com", "123-456-7890")
student1.display_student_info()

student1.make_payment(500.00, datetime.datetime(2023, 4, 10))
print(student1.get_payment_history())

course1.assign_teacher(teacher1)
print(course1.get_teacher())