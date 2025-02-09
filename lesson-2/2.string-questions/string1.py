# 1. Create a program to ask name and year of birth from user and tell them their age.

user_name = input('Please enter your name: ')
user_birth = input('Please enter your year of birth: ')
user_age = str(2025 - float(user_birth)).split('.')[0]
print(f"{user_name} you are {user_age} years old!")