#Beginner-level Python project:
#Simple calculator program that performs basic arithmetic operations (+, -, *, /) based on user input:
#Asks the user how many values they want to use  

def add(numbers): #Function to perform addition
    return sum(numbers)

def subtract(numbers):  #Function to perform subtraction
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiply(numbers): #Function to perform multiplication
    result = 1
    for num in numbers:
        result *= num
    return result
def divide(numbers): #Function to perform division
    result = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            return "Cannot divide by zero!"
        result /= num
    return result

while True:
    print("\n--- Multi-Value Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("0. Exit")

    choice = input("Enter your choice: ")
    if choice == '0':
        print("Exiting calculator...")
        break
    n = int(input("How many values? "))
    numbers = []
    for i in range(n):
        val = float(input(f"Enter value {i+1}: "))
        numbers.append(val)

    if choice == '1':
        print("Result:", add(numbers))
    elif choice == '2':
        print("Result:", subtract(numbers))
    elif choice == '3':
        print("Result:", multiply(numbers))
    elif choice == '4':
        print("Result:", divide(numbers))
    else:
        print("Invalid choice. Please try again.")
