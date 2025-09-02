import json

# Load employee data from JSON file
def load_employees(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

# Print all employees
def print_employees(employees):
    print("Employee List:")
    for emp_id, info in employees.items():
        print(f"ID: {emp_id}")
        print(f"  Name: {info['name']}")
        print(f"  Department: {info['department']}")
        print(f"  Age: {info['age']}")
        print(f"  Salary: {info['salary']}")
        print("-" * 20)

if __name__ == "__main__":
    employees = load_employees("employee.json")
    print_employees(employees)