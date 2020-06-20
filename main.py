from package.application import salary
from package.application.db import people
import datetime


if __name__ == "__main__":
    def main():
        date = datetime.datetime.now()
        print(date.strftime('%Y %b %W %Hh:%Mm'))
        employee = people.Employees('Bill')
        employee_salary = salary.Salary(250000)
        print(f'годовая зарплата сотрудника: {people.Employees.get_employees(employee)} составляет {salary.Salary.calculate_salary(employee_salary)} руб')  
    
    main()