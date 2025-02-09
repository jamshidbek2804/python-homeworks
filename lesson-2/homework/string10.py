# 10. Write a program that asks the user for a sentence and prints the number of words in it.

make_sentence = input("Make a sentence, I will count its including words: ")
word_counter = len(make_sentence.split(" "))
print(word_counter)