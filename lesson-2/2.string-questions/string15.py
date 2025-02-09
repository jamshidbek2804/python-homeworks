# 15. Ask the user for a sentence and create an acronym from the first letters of each word.

# Example:
# Input: "World Health Organization"
# Output: "WHO"

main_str = "National Bank of Uzbekistan"
acronym_str = ""
for char in main_str :
    if char == char.upper() :
        acronym_str += char
print(acronym_str.replace(" ", ""))