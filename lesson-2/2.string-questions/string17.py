# 17. Ask the user for a string and replace all the vowels with a symbol (e.g., *).

main_str = input('Enter the string: ').lower()
vowels = "aeiou"
for n in vowels :
    main_str = main_str.replace(n, "*")
print(main_str)