
class Salary:

    def __init__(self, month_salary):
        self.month_salary = month_salary

    def calculate_salary(self):
        return int(self.month_salary * 12)