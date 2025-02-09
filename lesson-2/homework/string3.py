# 3. Write a Python program to:
#    Take a string input from the user.
#    Print the length of the string.
#    Convert the string to uppercase and lowercase.

message = input('Please enter something in string type: ')
to_lower = message.lower()
to_upper = message.upper()
print(f"Your string length = {len(message)}")
print(f"LowerCase: {to_lower}")
print(f"UpperCase: {to_upper}")