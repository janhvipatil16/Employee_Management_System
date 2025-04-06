#STEP - 1
employees = {
    101: {'Name': 'Satya', 'Age': 27, 'Department': 'HR', 'Salary': 50000},
    102: {'Name': 'John', 'Age': 35, 'Department': 'Finance', 'Salary': 60000},
    103: {'Name': 'Alice', 'Age': 36, 'Department': 'IT', 'Salary': 45000},
    104: {'Name': 'Bob', 'Age': 45, 'Department': 'Marketing', 'Salary': 60000}
}

#STEP - 2
def main_menu():
    while True:
        print("\n---- Employee Management System ----")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            print("Thank you for using the Employee Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose a valid option.")

#STEP - 3
def add_employee():
    emp_id = int(input("Enter Employee ID: "))
    if emp_id in employees:
        print(f"Employee ID {emp_id} already exists. Please enter a unique ID.")
        return
    
    Name = input("Enter Employee Name: ")
    Age = int(input("Enter Employee Age: "))
    Department = input("Enter Employee Department: ")
    Salary = float(input("Enter Employee Salary: "))

    employees[emp_id] = {
        'Name': Name,
        'Age': Age,
        'Department': Department,
        'Salary': Salary
    }
    
    print(f"Employee {Name} added successfully!")

#STEP - 4
def view_employees():
    if not employees:
        print("No employees available.")
    else:
        print("\nID\tName\t\tAge\tDepartment\tSalary")
        print("-" * 50)
        for emp_id, data in employees.items():
            print(f"{emp_id}\t{data['Name']}\t\t{data['Age']}\t{data['Department']}\t\t{data['Salary']}")

#STEP - 5
def search_employee():
    emp_id = int(input("Enter Employee ID to search: "))
    
    if emp_id in employees:
        data = employees[emp_id]
        print(f"\nEmployee ID: {emp_id}")
        print(f"Name: {data['Name']}")
        print(f"Age: {data['Age']}")
        print(f"Department: {data['Department']}")
        print(f"Salary: {data['Salary']}")
    else:
        print("Employee not found.")

#STEP - 6
if __name__ == "__main__":
    main_menu()