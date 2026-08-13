# Problem 1
# Create a dictionary called student with these keys:
# "name" -> your name
# "grade" -> your grade level
# Print the dictionary and then print only the name.
student = {"name": "Alice", "grade": 10}
print(student)
print(student["name"])



# Problem 2
# Create a dictionary called prices with:
# "apple" -> 2
# "banana" -> 1
# "orange" -> 3
# Ask the user for a fruit name and print its price.
# If the fruit is not in the dictionary, print "Not found".
prices = {"apple": 2, "banana": 1, "orange": 3}
fruit = input("Enter a fruit name: ")
if fruit in prices:
    print(prices[fruit])
else:
    print("Not found")



# Problem 3
# Ask the user for a word.
# Use a dictionary to count how many times each letter appears.
# Print the dictionary.
word = input("Enter a word: ")
letter_count = {}
for letter in word:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1
print(letter_count)



# Problem 4
# Create a dictionary called phonebook with 3 names and phone numbers.
# Ask the user for a name and print the phone number if it exists.
# Otherwise print "Unknown contact".
phonebook = {"Alice": "555-1234", "Bob": "555-5678", "Charlie": "555-9012"}
name = input("Enter a name: ")
if name in phonebook:
    print(phonebook[name])
else:
    print("Unknown contact")



# Problem 5
# Create a dictionary called scores with 3 students and their test scores.
# Print the name of the student with the highest score.
scores = {"Alice": 95, "Bob": 87, "Charlie": 92}
highest_name = max(scores, key=scores.get)
print(highest_name)
