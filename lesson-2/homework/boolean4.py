# 4.Write a program that takes three numbers and checks if all of them are different.

num1 = input('Enter the first number: ')
num2 = input('Enter the second number: ')
num3 = input('Enter the third number: ')
if num1 != num2 and num1 != num3 and num2 != num3 :
    print("All of them different numbers")
else : 
    print("There are the same numbers")