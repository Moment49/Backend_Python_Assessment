from .salary import Employee
def main():
    """This is the main program file that will be excuted and 
    serves as the entry point to the application script
    """
    # Dictionary containing employee names and salaries
    employees_salaries = {
    "Alice": 85000,
    "Bob": 72000,
    "Charlie": 90000,
    "David": 95000,
    "Eva": 80000,
    "Frank": 67000,
    "Grace": 77000
}

    while True:
        prompt = "1 - See all Employees and Salary \n"
        prompt += "2 - See employee new salaries after '10%' increment\n"
        prompt += "Select an action to perform (1 or 2): "
        user_select = input(prompt)
        if user_select == '1':
            for employee_name, employee_salary in employees_salaries.items():
                print(f"{employee_name}: {employee_salary}")
                break
            
        elif user_select == '2':
            print("Employee names and salaries before Increment: ")
            for employee_name, employee_salary in employees_salaries.items():
                print(f"{employee_name}: {employee_salary}")
                employee = Employee(employee_name, employee_salary)
                updated_employee_salary = employee.salary_increment()
            print(f"\nEmployee names and salaries after increment are: ")
            for employee_name, new_salary in updated_employee_salary.items():
                print(f"{employee_name}: {new_salary}")
            break
        





if __name__ == "__main__":
    main()