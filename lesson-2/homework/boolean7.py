# 7. Write a program that checks if the sum of two numbers is greater than 50.8. Create a program that checks if a given number is between 10 and 20 (inclusive)

# first task
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 + num2 > 50.8 :
    print(True)
else :
    print(False)
    
# second task 
given_num = float(input("Enter the number: "))
if given_num >= 10 and given_num <= 20 :
    print(True)
else :
    print(False)