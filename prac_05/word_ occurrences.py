"""
CP1404/CP5632 Practical
Do-from-scratch - Word Occurrences
"""

words = input("Input a phrase: ")
words = words.split(" ")
words.sort()
word_to_count = {}
for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1

max_length = 0
for word in words:
    if len(word) > max_length:
        max_length = len(word)

for word, count in word_to_count.items():
    print("{:{}} : {}".format(word, max_length, count))
