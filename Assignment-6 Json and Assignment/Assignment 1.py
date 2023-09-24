import json

# Part 1: Reading Employee Data from JSON File


class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

# Function to read employee data from "employee.json" file


def read_employee_data(filename):
    employee_list = []
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            for employee_data in data:
                employee = Employee(**employee_data)
                employee_list.append(employee)
        return employee_list
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []

# Function to print the list of Employee objects


def print_employee_list(employee_list):
    for i, employee in enumerate(employee_list, start=1):
        print(f"Employee {i}:")
        print(f"Name: {employee.name}")
        print(f"DOB: {employee.dob}")
        print(f"Height: {employee.height}")
        print(f"City: {employee.city}")
        print(f"State: {employee.state}")
        print()

# Part 2: Creating a JSON File for Indian States and Capitals


# Dictionary of Indian states and capitals
indian_states_dict = {
    "Andhra Pradesh": "Amaravati",
    "Arunachal Pradesh": "Itanagar",
    "Assam": "Dispur",
    "Bihar": "Patna",
    "Chhattisgarh": "Raipur",
    "Goa": "Panaji",
    "Gujarat": "Gandhinagar",
    "Haryana": "Chandigarh",
    "Himachal Pradesh": "Shimla",
    "Jharkhand": "Ranchi",
    "Karnataka": "Bengaluru",
    "Kerala": "Thiruvananthapuram",
    "Madhya Pradesh": "Bhopal",
    "Maharashtra": "Mumbai",
    "Manipur": "Imphal",
    "Meghalaya": "Shillong",
    "Mizoram": "Aizawl",
    "Nagaland": "Kohima",
    "Odisha": "Bhubaneswar",
    "Punjab": "Chandigarh",
    "Rajasthan": "Jaipur",
    "Sikkim": "Gangtok",
    "Tamil Nadu": "Chennai",
    "Telangana": "Hyderabad",
    "Tripura": "Agartala",
    "Uttar Pradesh": "Lucknow",
    "Uttarakhand": "Dehradun",
    "West Bengal": "Kolkata"
}

# Function to write Indian states and capitals to "indian_states.json" file


def write_indian_states(filename, data):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Data written to '{filename}' successfully.")
    except Exception as e:
        print(f"An error occurred while writing to '{filename}': {str(e)}")


if __name__ == "__main__":
    # Part 1: Read and print employee data
    employee_data_file = "employee.json"
    employees = read_employee_data(employee_data_file)
    if employees:
        print("Employee Information:")
        print_employee_list(employees)

    # Part 2: Write Indian states and capitals to a JSON file
    indian_states_file = "indian_states.json"
    write_indian_states(indian_states_file, indian_states_dict)
