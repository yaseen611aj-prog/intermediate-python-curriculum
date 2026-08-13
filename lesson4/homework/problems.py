# Problem 1
# Ask the user for a sentence.
# Use a dictionary to count how many times each word appears.
# Print the dictionary.
# (Hint: split the sentence)
sentence = input("Enter a sentence: ")
words = sentence.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)


# Problem 2
# Create a dictionary called capitals with states and their capitals.
# Ask the user for a state and print the capital.
# If not found, print "No data".
capitals = {
    "Washington": "Olympia",
    "Oregon": "Salem",
    "California": "Sacramento",
    "Nevada": "Carson City"
}
state = input("Enter a state: ")
if state in capitals:
    print(capitals[state])
else:
    print("No data")


# Problem 3
# Ask the user for a word.
# Print the letter that appears the most times.
# If there is a tie, print any one of them.
word = input("Enter a word: ")
letter_count = {}
for letter in word:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1
most_common = max(letter_count, key=letter_count.get)
print(most_common)


# Problem 4
# Create a dictionary called inventory with items and their quantity.
# Ask the user what item they want to buy and how many.
# If there are enough, subtract from the inventory and print the new inventory.
# Otherwise print "Not enough".
inventory = {"apple": 10, "banana": 5, "orange": 8}
item = input("What item do you want to buy? ")
quantity = int(input("How many? "))
if item in inventory and inventory[item] >= quantity:
    inventory[item] -= quantity
    print(inventory)
else:
    print("Not enough")


# Problem 5
# Ask the user for two words.
# Use dictionaries to check if they are anagrams (same letters, different order).
# Print "Anagram" or "Not anagram".
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

letter_count1 = {}
for letter in word1.lower():
    if letter in letter_count1:
        letter_count1[letter] += 1
    else:
        letter_count1[letter] = 1

letter_count2 = {}
for letter in word2.lower():
    if letter in letter_count2:
        letter_count2[letter] += 1
    else:
        letter_count2[letter] = 1

if letter_count1 == letter_count2:
    print("Anagram")
else:
    print("Not anagram")
