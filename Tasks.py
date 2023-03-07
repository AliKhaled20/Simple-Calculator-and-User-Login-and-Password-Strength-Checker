# Simple Calculator
# The objective of this task is to create a simple calculator that can perform addition,
# subtraction, multiplication, and division. The program should prompt the user to enter two numbers
# and an operator (+, -, *, /). The program should then perform the requested operation and print out the result.
# However, if the user enters an invalid operator, the program should display an error message and prompt the user
# to enter a valid operator.
def myCal(n1, n2, o):
    operations = ["+", "-", "*", "/"]

    if o not in operations:
        print("Error: Invalid operator")
        return None

    if o == operations[0]:
        result = n1 + n2
    elif o == operations[1]:
        result = n1 - n2
    elif o == operations[2]:
        result = n1 * n2
    elif o == operations[3]:
        result = n1 / n2

    return result

print("The is the task one, is a calculator task included just '+', '-', '*' and '/' \n")
# [Ali - ToDo : uncomment the below lines ]
print("The result of 2 + 5 is: ",myCal(2, 5, "+"))  # 7
print("The result of 10 - 3 is: ",myCal(10, 3, "-"))  # 7
print("The result of 4 * 6 is: ",myCal(4, 6, "*"))  # 24
print("The result of 20 / 5 is: ",myCal(20, 5, "/"))  # 4.0
print("The result of 7 % 8 is: ",myCal(7, 8, "%"))  # Error: Invalid operator, None

# User Login
# The objective of this task is to create a simple user login system using Python.
# The program should prompt the user to enter their username and password, and then
# check if the entered credentials are valid. If the credentials are valid, the program
# should display a welcome message. If the credentials are invalid, the program should display
# an error message and prompt the user to try again.

print("___________________________________________________________________________________")
print("The is the task two, is a login task contenue just when Name = Ali and password = 123")
# [Ali - ToDo : comment the next two rows and uncomment the next two]
# Name = "Ali"
# pas = 123
Name = input("Pleas enter your name: ")
pas = input("Pleas enter your PIN: ")
pas = int(pas)

while Name.lower() != "ali" or pas != 123:
    print("incorrect info \n pleas try again: ")
    Name = input("Pleas enter your name: ")
    pas = input("Pleas enter your PIN: ")
    pas = int(pas)

print("Welcome")


# Password Strength Checker
# The objective of this task is to create a program that checks the strength of a given password.
# The program should prompt the user to enter a password, and then check if the password meets
# certain criteria. If the password meets all of the criteria, the program should display a message
# indicating that the password is strong. If the password does not meet all of the criteria, the
# program should display a message indicating that the password is weak and provide specific feedback
# to the user about which criteria the password failed to meet.
#
# Example Criteria:
#
# lenght = 9
# Uppercase letters allowed
# lower case letters allowed
# digits allowed
# special characters allowed
# If a password meets all of them, it passes, otherwise, your program should specify what criteria i
# s missing and refuse the suggested password.

import re

print("___________________________________________________________________________________")
print("The is the task three , is a Password Strength Checker task: ")

criteria = "The criteria to genarate the password is as follows: \n" \
           "○  The minimume bits is 8\n" \
           "○  The password must be mixed of Uppercase and small later\n" \
           "○  The password must contain at least one digit\n "
print(criteria)

new_pass  = input("Enter the password, pleas: ")
item_pass = []
for i in range(len(new_pass)):
    item_pass.append(new_pass[i])
# print(len(item_pass))
while len(item_pass) < 7 or not re.search(r"[\d]+", new_pass) or not re.search(r"[A-Z]+", new_pass) or not re.search(r"[a-z]+", new_pass):
    if len(item_pass) < 7:
        print("The password length must be at least 8")
    if not re.search(r"[\d]+", new_pass):
        print("The password must contain at least one digit")
    if not re.search(r"[A-Z]+", new_pass):
        print("The password must contain at least one Uppercase")
    if not re.search(r"[a-z]+", new_pass):
        print("The password must contain at least one small letter")
    # else:
    #     print("The password is Valid")
    new_pass = input("pleas try again: ")
    item_pass = []
    for i in range(len(new_pass)):
        item_pass.append(new_pass[i])
print("The password is Valid")



