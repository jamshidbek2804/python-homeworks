# 18. Write a program that checks if a string starts with one word and ends with another.

# Example:
# Input: "Python is fun!"
# Starts with: "Python"
# Ends with: "fun!"

main_str = input("Enter the sentence: ")
first_word = main_str.split(" ")[0]
last_word = main_str.split(" ")[-1]
print(f"Starts with: {first_word}")
print(f"Ends with: {last_word}")