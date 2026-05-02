#creating unique word counter
text = input("Enter text:")
words = text.split()
unique = set(words)
print(f"Total words: {len(words)}")
print(f"Unique words: {len(unique)}")
for word in words:
    print(word)
