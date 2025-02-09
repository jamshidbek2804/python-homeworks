# 4. Write a program that takes two numbers and prints out the result of integer division and theremainder.

num1 = (input("Add first number: "))
num2 = (input("Add second number: "))
integer_part = str(float(num1) // float(num2)).split('.')[0]
remainder_part = str(float(num1) % float(num2)).split('.')[0]
print("The integer part of the first number divided by the second one:", integer_part)
print("The remainder part of the first number divided by the second one:", remainder_part)