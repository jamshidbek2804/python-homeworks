# 1. Write a program that accepts a username and password and checks if both are not empty.

user_name = input('Enter your name: ')
user_password = input('Enter your password: ')
if user_name and user_password != "" :
    print("Username: ", user_name)
    print("Password: ", user_password)
else :
    print("User's name and password are required!")