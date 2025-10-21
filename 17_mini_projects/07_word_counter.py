
text = input("Enter a paragraph: ")

words = text.lower().split()


word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1


print("\nWord Counts:")
for word, count in word_count.items():
    print(f"{word}: {count}")
