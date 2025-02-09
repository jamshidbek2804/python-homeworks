# 7. Create a program that takes a number and checks if it’s even or not.

num = input('Enter number: ')
str_to_num = float(num)
if (str_to_num % 2 == 0) :
	print(f"{num} is even")
else :
	print(f"{num} is odd")
