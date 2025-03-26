FILENAME = "employees.txt"
import sys


def add_employee():
    with open(FILENAME, 'a') as file:
        emp_id = input("Employee ID: ")
        name = input("Name: ")
        position = input("Position: ")
        salary = input("Salary: ")
        file.write(f"{emp_id}, {name}, {position}, {salary} \n")
        print("Employee successfully added...")


def view_employees():
    try:
        with open(FILENAME, 'r') as file:
            employees = file.readlines()
            if not employees:
                print("Employees list is empty...")
                return

            print("List of all employees: ")
            for emp in employees:
                emp_id, name, position, salary = emp.strip().split(",")
                print(f"ID: {emp_id}, Name: {name}, Position: {position}, Salary: $ {salary}")
    except FileNotFoundError:
        print("File not found! No employees have been added yet...")


def search_employee():
    emp_id_to_search = input("Enter the ID of the employee you are searching for: ")

    try:
        with open(FILENAME, 'r') as file:
            employees = file.readlines()
    except FileNotFoundError:
        print("File not found! No employees have been added yet...")
        return

    found = False
    for emp in employees:
        emp_id, name, position, salary = emp.strip().split(", ")
        if emp_id == emp_id_to_search:
            print("Employee found...")
            print(f"ID: {emp_id}")
            print(f"Name: {name}")
            print(f"Position: {position}")
            print(f"Salary: ${salary}")
            found = True
            break

    if not found:
        print("No employee found with this ID!...")


def update_employee():
    emp_id_to_update = input("Enter the ID of the employee you want to update: ")

    try:
        with open(FILENAME, 'r') as file:
            employees = file.readlines()
    except FileNotFoundError:
        print("File not found! No employees have been added yet...")
        return

    updated_employee = []
    found = False

    for emp in employees:
        emp_id, name, position, salary = emp.strip().split(', ')

        if emp_id == emp_id_to_update:
            print("Employee found! Update the information: ")

            new_name = input(f"New name ({name}): ").strip() or name
            new_position = input(f"New position ({position}): ").strip() or position
            new_salary = input(f"New salary ({salary}): ").strip() or salary

            updated_employee.append(f"{emp_id}, {new_name}, {new_position}, ${new_salary} \n")
            found = True
            break
        else:
            updated_employee.append(emp)

    if not found:
        print("No employee found with this ID!...")
        return

    try:
        with open(FILENAME, 'w') as file:
            file.writelines(updated_employee)
        print("Employee information successfully updated!...")
    except Exception as e:
        print(f"An error occurred: {e}")


def delete_employee():
    emp_id_to_delete = input("Enter the ID of the employee you want to delete: ")

    try:
        with open(FILENAME, 'r') as file:
            employees = file.readlines()
    except FileNotFoundError:
        print("File not found! No employees have been added yet...")
        return

    updated_employees = [
        emp for emp in employees if not emp.startswith(emp_id_to_delete + ',')
    ]

    if len(updated_employees) == len(employees):
        print("No employee found with this ID!...")
    else:
        with open(FILENAME, 'w') as file:
            file.writelines(updated_employees)
        print("Employee successfully deleted!...")


def exit_program():
    print("The program has exited. Goodbye!...")
    sys.exit()


def main():
    while True:
        print("Employee Management System...")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")

        choice = input("Choose (1-6): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            update_employee()
        elif choice == '5':
            delete_employee()
        elif choice == '6':
            exit_program()
            break
        else:
            print("Invalid choice! Please try again...")


if __name__ == "__main__":
    main()
