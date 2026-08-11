word = "pineapple"
print(word)

# Strings are 0 indexed (first character is at index 0)
print("First letter:", word[0])  # Output: 'p'
print("Second letter:", word[1])  # Output: 'i'

# Negative indexing starts from the end of the string
print("Last letter:", word[-1])  # Output: 'e'
print("Second to last letter:", word[-2])  # Output: 'l'

# Slicing: word[start:end] gives a substring from index start to end-1
print(word[0:4])  # Output: 'pine'
print(word[4:9])  # Output: 'apple'

# Shortcuts: you can leave start or stop blank
print(word[:4])  # Output: 'pine'
print(word[4:])  # Output: 'apple' 

word[::-1] # This will reverse the string