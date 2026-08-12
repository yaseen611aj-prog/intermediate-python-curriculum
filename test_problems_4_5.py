# Problem 4
# Create a 2D list of numbers.
# Count how many numbers are greater than 10.
numbers = [
    [1, 12, 3],
    [14, 5, 20],
    [7, 11, 9]
]

count = 0
for row in numbers:
    for num in row:
        if num > 10:
            count += 1

print("Problem 4 - Count of numbers > 10:", count)




# Problem 5
# Create a 2D list of letters.
# Build one string that contains every letter in the 2D list.
# Print the final string.
letters = [
    ["a", "b"],
    ["c", "d"],
    ["e"]
]

word = "".join(letter for row in letters for letter in row)
print("Problem 5 - Final string:", word)
