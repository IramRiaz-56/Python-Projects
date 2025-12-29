# Python program for Palindrome Checker
# check if a given string is a palindrome

def is_palindrome(s):
    # Remove spaces and convert to lowercase for accurate comparison
    s = s.replace(" ", "").lower()
    # Check if string is same forwards and backwards
    return s == s[::-1]

user_input = input("Enter a string to check if it's a palindrome: ") #Take input from user

if is_palindrome(user_input):   #Check and display result
    print(f'"{user_input}" is a palindrome.')
else:
    print(f'"{user_input}" is not a palindrome.')
