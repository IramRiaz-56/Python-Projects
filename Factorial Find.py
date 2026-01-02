# Python program for Factorial Calculator using recursion 

def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n * factorial of (n-1)
        return n * factorial(n - 1)

while True:
    try:
        num = int(input("Enter a non-negative integer to find factorial (or negative to exit): "))
        if num < 0:
            print("Exiting program.")
            break
        else:
            print(f"Factorial of {num} is {factorial(num)}")
    except ValueError:
        print("Please enter a valid integer.")
