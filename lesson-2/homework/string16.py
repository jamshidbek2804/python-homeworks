# 16. Write a program that asks the user for a string and a character, then removes all occurrences of that character from the string.

main_str = input('Enter the string: ').lower()
char_forStr = input('Enter the character: ').lower()
if char_forStr in main_str :
    new_str = main_str.replace(char_forStr, "")
    print(f"input: {main_str}")
    print(f"output: {new_str}")
else :
    print("Replaced char is not found in your string!")