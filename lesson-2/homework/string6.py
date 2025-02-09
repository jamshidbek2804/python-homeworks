# 6. Write a Python program to check if one string contains another.

main_string = "Write a Python program".lower()
substring = "python"
if (substring in main_string) :
    print(f"'{substring}' is found!")
else :
    print(f"'{substring}' is not found!")