# Python program for FizzBuzz
# to print numbers from 1 to 100 with FizzBuzz rules

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")   # Multiples of both 3 and 5
    elif num % 3 == 0:
        print("Fizz")       # Multiples of 3
    elif num % 5 == 0:
        print("Buzz")       # Multiples of 5
    else:
        print(num)          # Other number