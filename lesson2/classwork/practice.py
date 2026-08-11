# Problem 1
# Ask the user for a word.
# Print the first 3 letters, and then print the last 3 letters.
word = "Yaseen"
print(word)
print(word[:3])
print(word[3:])

# Problem 2
# Ask the user for a sentence.
# Print it in all caps, then print it in all lowercase.
text = "Hello"
print(text.lower())
print(text.upper())



# Problem 3
# Ask the user for a word.
# Print how many vowels it has (a, e, i, o, u).
word = input("Enter a word: ")
vowel_count = sum(1 for char in word.lower() if char in "aeiou")
print(vowel_count)



# Problem 4
# Ask the user for a phrase.
# Build a new string that removes all spaces.
phrase = input("Enter a phrase: ")
no_spaces = phrase.replace(" ", "")
print(no_spaces)




# Problem 5
# Ask the user for a word.
# Print "Palindrome" if it reads the same backwards, otherwise print "Not palindrome".
word = input("Enter a word: ")
if word.lower() == word.lower()[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")
