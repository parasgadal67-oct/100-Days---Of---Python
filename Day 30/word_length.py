# Dictionary Comprehension : Creatig the word length analyzer using dictionary comprehension.
words = ['Dehradun', 'Python', 'Cold', 'Warm', 'Dictionary', 'Comprehension', 'Code']
word_length = {word: len(word) for word in words if len(word) > 4}
print(word_length)