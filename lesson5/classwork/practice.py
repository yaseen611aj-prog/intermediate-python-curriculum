# Problem 1
# Create a tuple called colors with 3 colors.
# Print the first color and the last color.

colors = ("red", "blue", "green")
print(colors[0])
print(colors[-1])


# Problem 2
# Create a tuple called location with (city, state).
# Unpack it into city and state variables and print them.

location = ("Seattle", "Washington")
city, state = location
print(city)
print(state)


# Problem 3
# Create a list of numbers.
# Sort the list and print it.

numbers = [5, 2, 8, 1, 9, 3]
numbers.sort()
print(numbers)


# Problem 4
# Create a list of tuples called points with 3 points.
# Sort the list and print it.

points = [(3, 1), (1, 5), (2, 2)]
points.sort()
print(points)


# Problem 5
# Create a list of words.
# Sort the words by length and print the list.

words = ["python", "code", "computer", "is", "fun"]
words.sort(key=len)
print(words)
