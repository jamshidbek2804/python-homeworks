# 12. Write a program that takes a list of words and joins them into a single string, separated by a character (e.g., - or ,).

main_list = ['Welcome', 'Python', 'World']
main_str = ''
for elem in main_list :
    main_str += elem
output_str = "-".join(main_str)
print(output_str)