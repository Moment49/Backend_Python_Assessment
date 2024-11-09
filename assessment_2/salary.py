
class Employee:
    """"This is a class that models an employee with attributes such as employee and salary"""
    employees_salaries = {}
    increment_percent = 0.1  #Equivalent to 10%
    def __init__(self, employee_name, salary):
        """Instatiate the employee with attributes """
        self.employee_name = employee_name
        self.salary = salary
        # Store the employee object
        Employee.employees_salaries[self.employee_name] = self.salary

    def __repr__(self):
        return f"{self.employee_name} {self.salary}"
    
    @classmethod
    def salary_increment(cls):
        for employee_key, salary_val in cls.employees_salaries.items():
            salary_val  += salary_val * cls.increment_percent
            cls.employees_salaries[employee_key] = salary_val

        return cls.employees_salaries




