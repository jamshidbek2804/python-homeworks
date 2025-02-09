# 6. Create a program that accepts a number and checks if it’s divisible by both 3 and 5.

num = float(input("Enter the number: "))
if num % 3 == 0 and num % 5 == 0 :
    print("It is divided into two")
elif num % 3 == 0 or num % 5 == 0 :
    print("Divides into only one")
else :
    print("It cannot be divided into two")