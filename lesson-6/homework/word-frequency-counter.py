from collections import Counter
import string
FILENAME = "sample.txt"

try:
    with open(FILENAME, 'r', encoding='utf-8') as file:
        content = file.read()
except FileNotFoundError:
    print(f"{FILENAME} not found!")
    content = input("Please enter sth:\n")
    with open(FILENAME, 'w', encoding='utf-8') as file:
        file.write(content)

content = content.lower()
for p in string.punctuation:
    content = content.replace(p, '')

words = content.split()
word_count = Counter(words)
total_words = sum(word_count.values())

top_n = int(input("How many of the most common words would you like to see? (for example: 5): "))

sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
most_common = sorted_words[:top_n]

print(f"\nTotal words: {total_words}")
print(f"Top {top_n} most common words: ")
for word, count in most_common:
    print(f"{word} - {count} {'time' if count == 1 else 'times'}")

with open("word_count_report.txt", 'w', encoding='utf-8') as report:
    report.write("Word count report\n")
    report.write(f"Total words: {total_words}\n")
    report.write(f"Top {top_n} words:\n")
    for word, count in most_common:
        report.write(f"{word} - {count}\n")