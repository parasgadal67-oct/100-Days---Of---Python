# Using .upper() in dict.comprehension capitalising the words 
words = ["dehradun", "dictionary", "python", "engineering", "machine", "learning"]
upper_map = {word: word.upper() for word in words}
print(upper_map)