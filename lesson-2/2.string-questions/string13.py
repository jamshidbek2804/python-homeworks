# 13. Ask the user for a string and remove all spaces from it.

main_str = input('Enter something with space: ')
remove_space = main_str.replace(" ", "") # strip() does not remove spaces inside the string.
print(f"Output: {remove_space}")