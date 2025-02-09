# 5. Write a program that counts the number of vowels and consonants in a given string.

given_str = input('Please enter string: ').lower()
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
vowelsIn_givenStr = 0
consonantsIn_givenStr = 0

for i in given_str:
    for n in vowels:
        if (i == n) :
            vowelsIn_givenStr += 1
print(f"The number of vowels = {vowelsIn_givenStr}")
            
for i in given_str:
    for k in consonants:
        if (i == k) :
            consonantsIn_givenStr += 1
print(f"The number of consonants = {consonantsIn_givenStr}")