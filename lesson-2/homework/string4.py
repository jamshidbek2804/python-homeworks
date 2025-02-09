# 4. Write a Python program to check if a given string is palindrome or not.

given_str = input('Please enter string; I will check it is palindrom or not: ')
check_str = given_str[::-1] # Ikkinchi usuli (given_str)ni listga aylantirib .reverse() metodidan foydalansa bo'ladi
if (given_str == check_str) :
    print(f"{given_str} is polindrom")
else : 
    print(f"{given_str} is not polindrom")