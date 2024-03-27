# student.py
from datetime import datetime
from model.Enrollments import Enrollment
from model.Payment import Payment

class Student:
    def __init__(self, student_id, first_name, last_name, dob, email, phone_number):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.email = email
        self.phone_number = phone_number
        self.enrollments = []
        self.payments = []
    
    def enroll_in_course(self, course):
        enrollment = Enrollment(self.student_id, course.course_id, datetime.now())
        self.enrollments.append(enrollment)
    
    def update_student_info(self, first_name, last_name, dob, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.email = email
        self.phone_number = phone_number
    
    def make_payment(self, amount, payment_date):
        payment = Payment(self.student_id, amount, payment_date)
        self.payments.append(payment)
    
    def display_student_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Date of Birth: {self.dob}")
        print(f"Email: {self.email}")
        print(f"Phone Number: {self.phone_number}")
    
    def get_enrolled_courses(self):
        return [enrollment.course_id for enrollment in self.enrollments]
    
    def get_payment_history(self):
        return [(payment.amount, payment.payment_date) for payment in self.payments]