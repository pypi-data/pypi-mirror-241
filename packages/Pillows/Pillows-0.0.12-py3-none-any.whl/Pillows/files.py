def factorial(): 
    factorial = """
def factorial(n):
    result = 1
    while n > 0:
        result = result * n
        n =  n - 1
    return result

number = int(input("Enter any number :"))
print(f"Factorial of {number} is {factorial(number)}")
"""
    print(factorial)


def aplha_e(): 
    alpha_e = """
def print_E_pattern():
    for i in range(7):
        if i == 0 or i == 6:
            print("*****")
        elif i == 3:
            print("****")
        else:
            print("*")

print_E_pattern()
"""
    print(alpha_e)


def palindrome(): 
    palindrome = """
def is_palindrome(n):
    number_str = str(n)
    
    return number_str == number_str[::-1]

n = int(input("Enter any number:"))
if is_palindrome(n):
    print(f"{n} is a palindrome.")
else:
    print(f"{n} is not a palindrome.")
"""
    print(palindrome)


def palf(): 
    palf = """
def is_palindrome(n):
    number_str = str(n)
    return number_str == number_str[::-1]

def main():
    n = int(input("Enter any number: "))
    
    if is_palindrome(n):
        print(f"{n} is a palindrome.")
    else:
        print(f"{n} is not a palindrome.")

if __name__ == "__main__":
    main()

"""
    print(palf)


def armstrong():
    armstrong = """
def is_armstrong(number):
    num_digits = len(str(number))
    temp = number
    armstrong_sum = 0
    while temp > 0:
        digit = temp % 10
        armstrong_sum += digit ** num_digits
        temp //= 10
    return armstrong_sum == number

def main():
    n = int(input("Enter a number: "))
    
    if is_armstrong(n):
        print(f"{n} is an Armstrong number.")
    else:
        print(f"{n} is not an Armstrong number.")

if __name__ == "__main__":
    main()
"""
    print(armstrong)


def ULW_spaces():
    ULW_spaces = """
def count_uppercase(text):
    return sum(1 for char in text if char.isupper())

def count_lowercase(text):
    return sum(1 for char in text if char.islower())

def count_whitespaces(text):
    return sum(1 for char in text if char.isspace())

def main():
    user_input = input("Enter any string: ")
    
    uppercase_count = count_uppercase(user_input)
    lowercase_count = count_lowercase(user_input)
    whitespace_count = count_whitespaces(user_input)

    print(f"Uppercase: {uppercase_count}")
    print(f"Lowercase: {lowercase_count}")
    print(f"Whitespaces: {whitespace_count}")

if __name__ == "__main__":
    main()
"""
    print(ULW_spaces)

def alphabetic_order():
    alphabetic_order = """
def unique_sorted_words(input_string):
    # Split the input string into a list of words
    words = [word.strip() for word in input_string.split(',')]

    # Get unique words and sort them alphanumerically
    unique_sorted = sorted(set(words))

    return unique_sorted

def main():
    # Prompt the user to enter a comma-separated sequence of words
    user_input = input("Enter a comma-separated sequence of words: ")

    # Get the unique and sorted words
    result = unique_sorted_words(user_input)

    # Print the result
    print("Sample Output:", ', '.join(result))

if __name__ == "__main__":
    main()
"""
    print(alphabetic_order) 


def count(): 
    count = """
def characters_count(s, char_list):
    count_dict = {}

    for char in char_list:
        count_dict[char] = s.count(char)

    return count_dict

if __name__ == '__main__':
    St = "hello welcome"
    lst = ["l", "w", "m", "e"]

    result = characters_count(St, lst)

    for char, count in result.items():
        print(f"{char} {count}")

"""
    print(count)


def replace(): 
    replace = """
def replace_not_bad(input_str):
    # Find the indices of 'not' and 'bad'
    index_not = input_str.find('not')
    index_bad = input_str.find('bad')

    # Check if 'not' comes before 'bad'
    if index_not != -1 and index_bad != -1 and index_not < index_bad:
        # Replace the 'not'...'bad' substring with 'good'
        result = input_str[:index_not] + 'good' + input_str[index_bad + 3:]
    else:
        # If 'not' doesn't come before 'bad' or either of them is not found, return the original string
        result = input_str

    return result

if __name__ == '__main__':
    # Sample Input
    input_str1 = "The song is not that bad!"
    input_str2 = "The song is poor!"

    print("Input1:",input_str1)
    print("Input2:",input_str2)


    # Sample Output
    output_str1 = replace_not_bad(input_str1)
    output_str2 = replace_not_bad(input_str2)

    
    print("Output1:",output_str1)
    print("Output2:",output_str2)
"""
    print(replace)


def largest(): 
    largest = """
def second_smallest_largest(numbers):
    unique_numbers = list(set(numbers))

    if len(unique_numbers) < 2:
        return "List should have at least two distinct elements."

    sorted_numbers = sorted(unique_numbers)

    second_smallest = sorted_numbers[1]
    second_largest = sorted_numbers[-2]

    return second_smallest, second_largest

if __name__ == '__main__':
    # Sample Input
    num_list = [12, 45, 2, 41, 31, 10, 8, 6, 4]
    print(num_list)
    # Function Call
    result = second_smallest_largest(num_list)

    # Print Output
    print(f"The second smallest element is: {result[0]}")
    print(f"The second largest element is: {result[1]}")
"""
    print(largest)


def frequency(): 
    frequency = """
def element_frequency(input_list):
    frequency_dict = {}

    for element in input_list:
        if element in frequency_dict:
            frequency_dict[element] += 1
        else:
            frequency_dict[element] = 1

    return frequency_dict

if __name__ == '__main__':
    # Sample Input
    input_list = [1, 2, 8, 3, 2, 2, 2, 5, 1]

    # Function Call
    result = element_frequency(input_list)

    # Print Output Header
    print("Element | Frequency")

    # Print Output
    for element, frequency in result.items():
        print(f"{element} | {frequency}")
"""
    print(frequency)

def duplicates(): 
    duplicates = """
def remove_duplicates(input_list):
    unique_elements = list(set(input_list))
    return unique_elements

if __name__ == '__main__':
    # Sample Input
    a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

    # Function Call
    result = remove_duplicates(a)

    # Print Output
    print(set(result))
"""
    print(duplicates)


def random_list():
    random_list = """
import random

def generate_random_numbers(num_elements):
    random_numbers = [random.randint(1, 50) for _ in range(num_elements)]
    return random_numbers

if __name__ == '__main__':
    # Input
    num_elements = int(input("Enter the number of elements: "))

    # Function Call
    result = generate_random_numbers(num_elements)

    # Print Output
    print(f"Randomized list is: {result}")
"""
    print(random_list)


def reverse_list(): 
    reverse_list = """
def reverse_list_elements(input_list):
    reversed_list = input_list[::-1]
    return reversed_list

if __name__ == '__main__':
    # User Input
    user_input = input("Enter elements separated by spaces: ")
    
    # Convert user input to a list of integers
    my_list = [int(x) for x in user_input.split()]

    # Function Call
    result = reverse_list_elements(my_list)

    # Print Output
    print(f"Output: {result}")
"""
    print(reverse_list)


def dict_1():
    dict_1 = """
# Given dictionary
inventory = {
    'gold': 500,
    'pouch': ['flint', 'twine', 'gemstone'],
    'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

# Add a key 'pocket' and set its value to a list
inventory['pocket'] = ['seashell', 'strange berry', 'lint']

# Sort the items in the list under the 'backpack' key
inventory['backpack'].sort()

# Remove 'dagger' from the list under the 'backpack' key
inventory['backpack'].remove('dagger')

# Add 50 to the number stored under the 'gold' key
inventory['gold'] += 50

# Print the updated inventory
print("Updated Inventory:")
print(inventory)

"""
    print(dict_1)

def dict_2():
    dict_2 = """
# Create a new dictionary called prices
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Loop through each key in prices
for key in prices:
    print(key)
    print(f"price: {prices[key]}")
    print("stock: 0")

# Determine the total value if all food is sold
total = 0
for key in prices:
    total_value = prices[key] * 0  # Assuming stock is 0 for each item
    print(f"Value if {key} is sold: {total_value}")
    total += total_value

# Print the total value
print(f"Total value if all food is sold: {total}")

"""
    print(dict_2)

def dict_3():
    dict_3 = """
# Step 1: Make a list called groceries
groceries = ["banana", "orange", "apple"]

# Step 2: Define dictionaries
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Step 3: Define a function compute_bill
def compute_bill(food):
    total = 0
    for item in food:
        if stock[item] > 0:
            total += prices[item]
            stock[item] -= 1
    return total

# Example Usage
total_cost = compute_bill(groceries)
print(f"Total cost of groceries: {total_cost}")
print("Updated stock:")
print(stock)


"""
    print(dict_3)

def dict_4():
    dict_4 = """
# Step 1: Create three dictionaries
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}

alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}

tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Step 2: Create a list called students
students = [lloyd, alice, tyler]

# Step 3: Print out each student's data
for student in students:
    print("Name:", student["name"])
    print("Homework:", student["homework"])
    print("Quizzes:", student["quizzes"])
    print("Tests:", student["tests"])
    print()

# Step 4: Write a function average
def average(numbers):
    total = sum(numbers)
    total = float(total)
    return total / len(numbers)

# Step 5: Write a function get_average
def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    return 0.1 * homework + 0.3 * quizzes + 0.6 * tests

# Step 6: Write a function get_letter_grade
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Step 7: Write a function get_class_average
def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
    return average(results)

# Step 8: Print the class average and letter grade
class_average = get_class_average(students)
print("Class Average:", class_average)
print("Letter Grade:", get_letter_grade(class_average))


"""
    print(dict_4)

def cp_reverse():
    cp_reverse = """
def reverse_file_content(input_filename, output_filename):
    try:
        # Read the content of the input file
        with open(input_filename, 'r') as input_file:
            content = input_file.read()

        # Reverse the content
        reversed_content = ' '.join(content.split()[::-1])

        # Write the reversed content to the output file
        with open(output_filename, 'w') as output_file:
            output_file.write(reversed_content)

        print("File content reversed successfully.")

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_file_name = "input.txt"
output_file_name = "output.txt"

reverse_file_content(input_file_name, output_file_name)

"""
    print(cp_reverse)

def cp_new():
    cp_new = """
def copy_file(source_filename, destination_filename):
    try:
        # Read the content of the source file
        with open(source_filename, 'r') as source_file:
            content = source_file.read()

        # Write the content to the destination file
        with open(destination_filename, 'w') as destination_file:
            destination_file.write(content)

        print("File content copied successfully.")

    except FileNotFoundError:
        print("Source file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
source_file_name = "source.txt"
destination_file_name = "destination.txt"

copy_file(source_file_name, destination_file_name)


"""
    print(cp_new)

def vowels_extract():
    vowels_extract = """
def extract_words_with_vowels(input_filename):
    try:
        # Open the input file in read mode
        with open(input_filename, 'r') as input_file:
            # Read the content of the file
            content = input_file.read()

            # Split the content into words
            words = content.split()

            # Extract words starting with vowels
            vowels_starting_words = [word for word in words if word[0].lower() in 'aeiou']

            # Print the extracted words
            print("Words starting with vowels:")
            for word in vowels_starting_words:
                print(word)

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_file_name = "text_file.txt"

extract_words_with_vowels(input_file_name)


"""
    print(vowels_extract)

def rectangle():
    rectangle = """
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def __add__(self, other):
        new_length = self.length + other.length
        new_breadth = self.breadth + other.breadth
        return Rectangle(new_length, new_breadth)

    def __str__(self):
        return f"Length is {self.length} and Breadth is {self.breadth}"

    def __eq__(self, other):
        return self.length == other.length and self.breadth == other.breadth

    def __lt__(self, other):
        return (self.length * self.breadth) < (other.length * other.breadth)

    def __gt__(self, other):
        return (self.length * self.breadth) > (other.length * other.breadth)

    def __ge__(self, other):
        return (self.length * self.breadth) >= (other.length * other.breadth)

    def __le__(self, other):
        return (self.length * self.breadth) <= (other.length * other.breadth)

# Taking user input for rectangle dimensions
length1 = int(input("Enter length for r1: "))
breadth1 = int(input("Enter breadth for r1: "))
r1 = Rectangle(length1, breadth1)

length2 = int(input("Enter length for r2: "))
breadth2 = int(input("Enter breadth for r2: "))
r2 = Rectangle(length2, breadth2)

# Performing addition
r3 = r1 + r2

# Printing the user-friendly string representation
print(r3)

# Comparing dimensions
print(f"r1 == r2: {r1 == r2}")
print(f"r1 < r2: {r1 < r2}")
print(f"r1 > r2: {r1 > r2}")
print(f"r1 >= r2: {r1 >= r2}")
print(f"r1 <= r2: {r1 <= r2}")


"""
    print(rectangle)

def payroll():
    payroll = """
class Employee:
    def __init__(self, empid, name, department, designation, experience, basicPay):
        self.empid = empid
        self.name = name
        self.department = department
        self.designation = designation
        self.experience = experience
        self.basicPay = basicPay
        self.DA = 0.10 * basicPay
        self.HRA = 0.05 * basicPay
        self.EPF = 0.05 * basicPay
        self.tax = 0.10 * basicPay

    def calculate_net_salary(self):
        net_salary = self.basicPay + self.DA + self.HRA - self.EPF - self.tax
        return net_salary

    # Getter and Setter methods for employee details
    def get_empid(self):
        return self.empid

    def set_empid(self, empid):
        self.empid = empid

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_department(self):
        return self.department

    def set_department(self, department):
        self.department = department

    def get_designation(self):
        return self.designation

    def set_designation(self, designation):
        self.designation = designation

    def get_experience(self):
        return self.experience

    def set_experience(self, experience):
        self.experience = experience

    def get_basicPay(self):
        return self.basicPay

    def set_basicPay(self, basicPay):
        self.basicPay = basicPay
        self.DA = 0.10 * basicPay
        self.HRA = 0.05 * basicPay
        self.EPF = 0.05 * basicPay
        self.tax = 0.10 * basicPay


# Function to display employee details
def display_employee(employee):
    print("Employee ID:", employee.get_empid())
    print("Name:", employee.get_name())
    print("Department:", employee.get_department())
    print("Designation:", employee.get_designation())
    print("Experience:", employee.get_experience(), "years")
    print("Basic Pay:", employee.get_basicPay())
    print("Net Salary:", employee.calculate_net_salary())
    print("\n")


# Function to add a new employee
def add_employee():
    empid = int(input("Enter Employee ID: "))
    name = input("Enter Name: ")
    department = input("Enter Department: ")
    designation = input("Enter Designation: ")
    experience = int(input("Enter Experience (in years): "))
    basicPay = float(input("Enter Basic Pay: "))

    new_employee = Employee(empid, name, department, designation, experience, basicPay)
    employees.append(new_employee)
    print("Employee added successfully!\n")


# Function to edit employee details
def edit_employee():
    empid = int(input("Enter Employee ID to edit: "))
    for employee in employees:
        if employee.get_empid() == empid:
            print("Editing Employee Details:")
            new_name = input(f"Enter new Name for {employee.get_name()}: ")
            new_department = input(f"Enter new Department for {employee.get_department()}: ")
            new_designation = input(f"Enter new Designation for {employee.get_designation()}: ")
            new_experience = int(input(f"Enter new Experience (in years) for {employee.get_experience()}: "))
            new_basicPay = float(input(f"Enter new Basic Pay for {employee.get_basicPay()}: "))

            employee.set_name(new_name)
            employee.set_department(new_department)
            employee.set_designation(new_designation)
            employee.set_experience(new_experience)
            employee.set_basicPay(new_basicPay)

            print("Employee details updated successfully!\n")
            return

    print("Employee not found!\n")


# Function to delete an employee
def delete_employee():
    empid = int(input("Enter Employee ID to delete: "))
    for employee in employees:
        if employee.get_empid() == empid:
            employees.remove(employee)
            print("Employee deleted successfully!\n")
            return

    print("Employee not found!\n")


# Function to display all employees
def display_all_employees():
    if not employees:
        print("No employees to display.")
    else:
        print("Employee Details:")
        for employee in employees:
            display_employee(employee)


# Main menu loop
employees = []

while True:
    print("\nEmployee Payroll Management System")
    print("1. Add Employee")
    print("2. Edit Employee")
    print("3. Delete Employee")
    print("4. Display All Employees")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        edit_employee()
    elif choice == "3":
        delete_employee()
    elif choice == "4":
        display_all_employees()
    elif choice == "5":
        print("Exiting the application. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

"""
    print(payroll)

def salary_calculate():
    salary_calculate = """
class Employee:
    def __init__(self, empid, name, designation, basic_salary):
        self.empid = empid
        self.name = name
        self.designation = designation
        self.basic_salary = basic_salary

    def calculate_gross_salary(self):
        return self.basic_salary

    def calculate_net_salary(self):
        raise NotImplementedError("Subclasses must implement this method")

    def calculate_tax(self):
        raise NotImplementedError("Subclasses must implement this method")

    def print_pay_details(self):
        print("\nPay Details:")
        print(f"Employee ID: {self.empid}")
        print(f"Name: {self.name}")
        print(f"Designation: {self.designation}")
        print(f"Basic Salary: {self.basic_salary}")
        print(f"Gross Salary: {self.calculate_gross_salary()}")
        print(f"Net Salary: {self.calculate_net_salary()}")
        print(f"Tax: {self.calculate_tax()}")


class Manager(Employee):
    def __init__(self, empid, name, basic_salary):
        super().__init__(empid, name, "Manager", basic_salary)

    def calculate_gross_salary(self):
        return self.basic_salary + 0.95 * self.basic_salary + 0.20 * self.basic_salary

    def calculate_net_salary(self):
        return self.calculate_gross_salary() - 3000

    def calculate_tax(self):
        return 0.25 * self.basic_salary


class Engineer(Employee):
    def __init__(self, empid, name, basic_salary):
        super().__init__(empid, name, "Engineer", basic_salary)

    def calculate_gross_salary(self):
        return self.basic_salary + 0.80 * self.basic_salary + 0.15 * self.basic_salary

    def calculate_net_salary(self):
        return self.calculate_gross_salary() - 2000

    def calculate_tax(self):
        return 0.15 * self.basic_salary


# Menu-driven interface
while True:
    print("\nEmployee Salary Calculation System")
    print("1. Manager")
    print("2. Engineer")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        empid = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        basic_salary = float(input("Enter Basic Salary: "))
        manager = Manager(empid, name, basic_salary)
        manager.print_pay_details()

    elif choice == "2":
        empid = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        basic_salary = float(input("Enter Basic Salary: "))
        engineer = Engineer(empid, name, basic_salary)
        engineer.print_pay_details()

    elif choice == "3":
        print("Exiting the application. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 3.")


"""
    print(salary_calculate)

def daily_week_worker():
    daily_week_worker = """
class Worker:
    def __init__(self, name, salary_rate):
        self.name = name
        self.salary_rate = salary_rate

    def compute_pay(self, hours):
        raise NotImplementedError("Subclasses must implement this method")


class DailyWorker(Worker):
    def compute_pay(self, days_worked):
        return self.salary_rate * days_worked


class SalariedWorker(Worker):
    def compute_pay(self, hours_worked):
        return self.salary_rate * 40


# Example of using the classes
daily_worker = DailyWorker("John", 20.0)
salaried_worker = SalariedWorker("Alice", 25.0)

# Calculate and print the pay for both workers
days_worked = int(input("Enter the number of days worked for the daily worker: "))
print(f"{daily_worker.name}'s weekly pay: ${daily_worker.compute_pay(days_worked)}")

hours_worked = int(input("Enter the number of hours worked for the salaried worker: "))
print(f"{salaried_worker.name}'s weekly pay: ${salaried_worker.compute_pay(hours_worked)}")


"""
    print(daily_week_worker)

def image_play():
    image_play = """
from PIL import Image, ImageOps, ImageFilter

try:
    # Load the image
    image_path = "sample.jpg"  # Provide the full path to your image
    original_image = Image.open(image_path)

    # Display the image
    original_image.show()

    # Plot the image in the console window
    print(original_image)

    # Display the image size (width and height)
    image_size = original_image.size
    print(f"Image Size: {image_size}")

    # Reduce the image size to half
    half_size_image = original_image.resize((int(image_size[0] / 2), int(image_size[1] / 2)))
    half_size_image.show()

    # Rotate the image 145 degrees
    rotated_image = original_image.rotate(145)
    rotated_image.show()

    # Resize the image in x and y directions
    resized_image = original_image.resize((image_size[0] + 50, image_size[1] + 70))
    resized_image.show()

    # Flip the image (Left to Right, Top to Bottom)
    flipped_lr_image = ImageOps.mirror(original_image)
    flipped_tb_image = ImageOps.flip(original_image)
    flipped_lr_image.show()
    flipped_tb_image.show()

    # Crop the image
    crop_box = (50, 50, 300, 300)  # Define the crop box (left, top, right, bottom)
    cropped_image = original_image.crop(crop_box)
    cropped_image.show()

    # Convert the color image to GrayScale and Black and White
    grayscale_image = original_image.convert("L")
    bw_image = original_image.convert("1")
    grayscale_image.show()
    bw_image.show()

    # Apply blur effect on the image
    blurred_image = original_image.filter(ImageFilter.BLUR)
    blurred_image.show()

except Exception as e:
    print(f"An error occurred: {e}")


"""
    print(image_play)

def turtle_indian():
    turtle_indian = """
import turtle

def draw_rectangle(color, width, height, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def draw_circle(color, radius, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_indian_flag(width, height):
    turtle.speed(2)

    saffron_height = height // 3
    white_height = height // 3
    green_height = height // 3

    # Draw saffron rectangle
    draw_rectangle("#FF9933", width, saffron_height, -width/2, height/2)

    # Draw white rectangle
    draw_rectangle("white", width, white_height, -width/2, height/2 - saffron_height)

    # Draw green rectangle
    draw_rectangle("#138808", width, green_height, -width/2, height/2 - saffron_height - white_height)

    # Draw the Ashoka Chakra in the center of the white rectangle
    chakra_radius = max(width, white_height) // 8
    draw_circle("navy", chakra_radius, 0, height/2 - saffron_height - white_height/2)

    turtle.hideturtle()
    turtle.done()

# Set the dimensions for the compact flag
flag_width = 600
flag_height = 400

# Create and display the compact Indian flag using Turtle
draw_indian_flag(flag_width, flag_height)

"""
    print(turtle_indian)

def turtle_house():
    turtle_house = """
import turtle

# Set the background color to white
screen = turtle.Screen()
screen.bgcolor("white")

# Create our turtle
t = turtle.Turtle()
t.color("black")
t.shape("turtle")
t.speed(5)

# Define a function to draw and fill a rectangle with the given
# dimensions and color
def drawRectangle(t, width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

# Define a function to draw and fill an equilateral right
# triangle with the given hypotenuse length and color.
def drawTriangle(t, length, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(3):
        t.forward(length)
        t.left(120)
    t.end_fill()

# Draw and fill the front of the house in dark blue
t.penup()
t.goto(-150, -120)
t.pendown()
drawRectangle(t, 100, 110, "darkblue")

# Draw and fill the front door in white
t.penup()
t.goto(-120, -120)
t.pendown()
drawRectangle(t, 40, 60, "white")

# Front roof in yellow
t.penup()
t.goto(-150, -10)
t.pendown()
drawTriangle(t, 100, "yellow")

# Hide the turtle
t.hideturtle()

# Display the window
turtle.done()


"""
    print(turtle_house)
    
def gui_calc():
    gui_calc = """

import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.value1_label = tk.Label(root, text="Type Value 1:")
        self.value1_label.grid(row=0, column=0)
        self.value1_entry = tk.Entry(root)
        self.value1_entry.grid(row=0, column=1)

        self.value2_label = tk.Label(root, text="Type Value 2:")
        self.value2_label.grid(row=1, column=0)
        self.value2_entry = tk.Entry(root)
        self.value2_entry.grid(row=1, column=1)

        self.operation_label = tk.Label(root, text="Operation:")
        self.operation_label.grid(row=2, column=0)

        self.result_label = tk.Label(root, text="Result")
        self.result_label.grid(row=3, column=0)

        self.add_button = tk.Button(root, text="+", command=lambda: self.calculate("+"))
        self.add_button.grid(row=2, column=1, padx=5)
        
        self.subtract_button = tk.Button(root, text="-", command=lambda: self.calculate("-"))
        self.subtract_button.grid(row=2, column=2, padx=5)
        
        self.multiply_button = tk.Button(root, text="*", command=lambda: self.calculate("*"))
        self.multiply_button.grid(row=2, column=3, padx=5)
        
        self.divide_button = tk.Button(root, text="/", command=lambda: self.calculate("/"))
        self.divide_button.grid(row=2, column=4, padx=5)

    def calculate(self, operation):
        try:
            value1 = float(self.value1_entry.get())
            value2 = float(self.value2_entry.get())
            
            if operation == "+":
                result = value1 + value2
            elif operation == "-":
                result = value1 - value2
            elif operation == "*":
                result = value1 * value2
            elif operation == "/":
                result = value1 / value2
            else:
                result = "Invalid operation"
            
            self.result_label.config(text=f"Result: {result}")
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter numeric values.")
        except ZeroDivisionError:
            self.result_label.config(text="Cannot divide by zero.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

"""
    print(gui_calc)

def gui_reg():
    gui_reg = """

import tkinter as tk
from tkinter import ttk

class RegistrationForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Form")

        # Full Name
        self.full_name_label = tk.Label(root, text="Full Name:")
        self.full_name_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.full_name_entry = tk.Entry(root)
        self.full_name_entry.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

        # Email
        self.email_label = tk.Label(root, text="Email:")
        self.email_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

        # Gender
        self.gender_label = tk.Label(root, text="Gender:")
        self.gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.gender_var = tk.StringVar()
        self.gender_var.set("Male")
        self.gender_radio_male = tk.Radiobutton(root, text="Male", variable=self.gender_var, value="Male")
        self.gender_radio_male.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)
        self.gender_radio_female = tk.Radiobutton(root, text="Female", variable=self.gender_var, value="Female")
        self.gender_radio_female.grid(row=2, column=2, padx=10, pady=5, sticky=tk.W)

        # Country
        self.country_label = tk.Label(root, text="Country:")
        self.country_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        self.countries = ["USA", "Canada", "UK", "India", "Australia"]
        self.country_var = tk.StringVar()
        self.country_var.set(self.countries[0])
        self.country_dropdown = ttk.Combobox(root, values=self.countries, textvariable=self.country_var)
        self.country_dropdown.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)

        # Programming
        self.programming_label = tk.Label(root, text="Programming:")
        self.programming_label.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
        self.python_var = tk.BooleanVar()
        self.python_checkbox = tk.Checkbutton(root, text="Python", variable=self.python_var)
        self.python_checkbox.grid(row=4, column=1, padx=10, pady=5, sticky=tk.W)
        self.java_var = tk.BooleanVar()
        self.java_checkbox = tk.Checkbutton(root, text="Java", variable=self.java_var)
        self.java_checkbox.grid(row=4, column=2, padx=10, pady=5, sticky=tk.W)

        # Submit Button
        self.submit_button = tk.Button(root, text="Submit", command=self.submit_form)
        self.submit_button.grid(row=5, column=0, columnspan=3, pady=10)

    def submit_form(self):
        full_name = self.full_name_entry.get()
        email = self.email_entry.get()
        gender = self.gender_var.get()
        country = self.country_var.get()
        programming_languages = []
        if self.python_var.get():
            programming_languages.append("Python")
        if self.java_var.get():
            programming_languages.append("Java")

        # Display the collected information (can be modified as needed)
        result_text = f"Full Name: {full_name}\nEmail: {email}\nGender: {gender}\nCountry: {country}\nProgramming: {', '.join(programming_languages)}"
        tk.messagebox.showinfo("Registration Form Submission", result_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = RegistrationForm(root)
    root.mainloop()

"""
    print(gui_reg)


def dir(): 
    print("factorial(), aplha_e(), palindrome(), palf()")
    print("armstrong(), ULW_spaces(), alphabetic_order(), count()")
    print("replace(), largest(), frequency(), duplicates(), random_list()")
    print("reverse_list(), dict_1(), dict_2(), dict_3(), dict_4()")
    print("cp_reverse(), cp_new(), vowels_extract(), rectangle(), payroll()")
    print("salary_calculate(), daily_week_worker(), image_play(), turtle_indian()")
    print("turtle_house(), gui_calc(), gui_reg()")
