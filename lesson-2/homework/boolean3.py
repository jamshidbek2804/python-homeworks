# 3. Write a program that checks if a number is positive and even.

num = float(input('Enter the number: '))
if num >= 0 and num % 2 == 0 :
    print(f"{num} is positive and even number")
elif num >= 0 and num % 2 != 0 :
    print(f"{num} is positive, but not even number")
elif num < 0 and num % 2 == 0 :
    print(f"{num} is not positive, but even number")
else : 
    print(f"{num} is neither positive nor even")