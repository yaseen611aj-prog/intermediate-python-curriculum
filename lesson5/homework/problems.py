# Problem 1
# Create a tuple called scores with 4 numbers.
# Print the average score.
scores = (95, 87, 92, 88)
average = sum(scores) / len(scores)
print(average)


# Problem 2
# Create a list of tuples representing students:
# ("Ava", 95), ("Ben", 88), ("Kai", 73)
# Print the name of the student with the highest score.
students = [("Ava", 95), ("Ben", 88), ("Kai", 73)]
highest_student = max(students, key=lambda x: x[1])
print(highest_student[0])


# Problem 3
# Create a list of words.
# Sort it alphabetically, then print it.
# Then sort it by length, then print it.
words = ["zebra", "apple", "mango", "cat", "elephant"]
sorted_alphabetically = sorted(words)
print(sorted_alphabetically)
sorted_by_length = sorted(words, key=len)
print(sorted_by_length)


# Problem 4
# Create a list of tuples where each tuple is (word, length_of_word).
# Sort the list and print it.
words = ["cat", "elephant", "apple", "dog", "zebra"]
word_tuples = [(word, len(word)) for word in words]
sorted_tuples = sorted(word_tuples, key=lambda x: x[1])
print(sorted_tuples)


# Problem 5
# Create a list of tuples called players.
# Each tuple should have (name, score).
# Sort the players from highest score to lowest score and print the list.
players = [("Alice", 150), ("Bob", 200), ("Charlie", 175), ("Diana", 190)]
sorted_players = sorted(players, key=lambda x: x[1], reverse=True)
print(sorted_players)
