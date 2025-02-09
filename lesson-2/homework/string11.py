# 11. Write a program to check if a string contains any digits.

main_str = input('Enter something: ')
contains_digit = any(i.isdigit() for i in main_str)
if contains_digit == True :
    print('Your string contains digits')
else : 
    print('Your string doesn\'t contains digits')