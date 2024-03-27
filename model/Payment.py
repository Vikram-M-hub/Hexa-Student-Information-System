class Payment:
    def __init__(self, student_id, amount, payment_date):
        self.payment_id = hash((student_id, amount, payment_date))
        self.student_id = student_id
        self.amount = amount
        self.payment_date = payment_date
