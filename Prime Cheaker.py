#Python program for Prime Number Cheaker
def is_prime(num):
    if num <= 1:
        return False
    # Check from 2 to sqrt(num)
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
while True:
    try:
        number = int(input("Enter a number to check if it is prime (negative to exit): "))
        if number < 0:
            print("Exiting program.")
            break
        if is_prime(number):
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")
    except ValueError:
        print("Please enter a valid integer.")
