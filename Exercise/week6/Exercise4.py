employees = {
    101: {
        "name": "Passang",
        "department": "IT",
        "salary": 50000,
        "username": "passang",
        "password": "passang123"
    },
    102: {
        "name": "Sonam",
        "department": "HR",
        "salary": 45000,
        "username": "sonam",
        "password": "sonam123"
    }
}

current_user = None

def login():
    global current_user

    username = input("Enter username: ")
    password = input("Enter password: ")

    for user_id, employee in employees.items():

        if employee["username"] == username and employee["password"] == password:
            current_user = user_id
            print(f"Login successful! Welcome {employee['name']}.")
            return

    print("Access Denied.")


def logout():
    global current_user

    current_user = None
    print("Logged out successfully.")


def login_required(func):

    def wrapper(*args, **kwargs):

        if current_user is None:
            print("User must be logged in to access this function.")
            return None

        return func(*args, **kwargs)

    return wrapper


@login_required
def view_salary():
    employee = employees[current_user]

    print(f"Salary: ${employee['salary']}")


@login_required
def view_personal_details():
    employee = employees[current_user]

    print(f"Name: {employee['name']}")
    print(f"Department: {employee['department']}")


@login_required
def download_report():
    employee = employees[current_user]

    print(f"Downloading report for {employee['name']}...")

view_salary()

login()

view_personal_details()

logout()

download_report()
