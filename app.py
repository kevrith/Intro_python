def sum_numbers(a=2, b=5):
    result = a + b
    print(f"The sum of two numbers {a} and {b} is: {result}")
            
# sum_numbers(5, 10)

name = "Kelvin"
def greet_user(name):
    print(f"Hello, {name}! Welcome to our application.")
    pass
 # greet_user()


def get_user():
       print(f"Fetching user name {name}")

# get_user()

def calculate_area(length, width):
        area = length * width
        if area > 50 and area < 100:
            print("Large area.")
        elif area  != 50:
            print("Small area.")
        print(f"The area of a rectangle with length {length} and width {width} is: {area}")
# calculate_area(4, 6)

def display_message(message="Hello, welcome to my Application."):
     message_data = {
          "sender": "Admin",
          "content": message,
          "timestamp": "2024-10-01 10:00:00",
          "receipient": "User"
     }
     print(f"sender:" , message_data["sender"])

# display_message()

# lists comprehension
def square_numbers(numbers):
    squared = [x**2 for x in numbers]
    print(f"Squared numbers: {squared}")

# square_numbers([1, 2, 3, 4, 5])

# generator expression
def generate_squares(n):
     squares = (x**2 for x in range(n))
     for square in squares:
          print(f"Square: {square}")

# generate_squares(5)

# decorators
def decorator_function(original_function):
     def wrapper_function(*args, **kwargs):
          print("Wrapper executed before {}".format(original_function.__name__))
          return original_function(*args, **kwargs)
     return wrapper_function    

@decorator_function
def display_info(name, age):
     print(f"Name: {name}, Age: {age}")
display_info("Alice", 30)