# 7. Ask the user to input a sentence and a word to replace. Replace that word with another word provided by the user.

# Example:
# Input sentence: "I love apples."
# Replace: "apples"
# With: "oranges"
# Output: "I love oranges."

main_string = input("Enter input sentence: ").lower()
old_substring = input("Enter old substring: ").lower()
new_substring = input("Enter new substring: ").lower()
new_string = main_string.replace(old_substring, new_substring, 1)
print(new_string)
