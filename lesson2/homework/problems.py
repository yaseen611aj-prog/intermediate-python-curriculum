# Problem 1
# Ask the user for a word.
# Print the word reversed using slicing.
word = input("Enter a word: ")
print(word[::-1])


# Problem 2
# Ask the user for a word and a letter.
# Print how many times the letter appears in the word (case-insensitive).
word = input("Enter a word: ")
letter = input("Enter a letter: ")
print(word.lower().count(letter.lower()))


# Problem 3
# Ask the user for a first name and a last name.
# Print their initials (first letter of first name + first letter of last name).
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(first_name[0].upper() + last_name[0].upper())


# Problem 4
# Ask the user for a sentence.
# Replace all spaces with underscores and print the result.
sentence = input("Enter a sentence: ")
print(sentence.replace(" ", "_"))


# Problem 5
# Ask the user for a word.
# Build a new string that contains ONLY the letters at odd indexes (1, 3, 5, ...).
word = input("Enter a word: ")
print(word[1::2])