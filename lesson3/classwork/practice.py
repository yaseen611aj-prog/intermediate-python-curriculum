# Problem 1
# Use a for loop with range to print every number from 5 to 12 (including 12).
for i in range(5, 13):
    print(i)


# Problem 2
# Use range with step to print all even numbers from 0 to 20 (including 20).
for i in range(0, 21, 2):
    print(i)


# Problem 3
# Build a list of the numbers from 1 to 10.
# Print the list.
numbers = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
]
print(numbers)

# Problem 4
# Use nested loops to print a 4 by 3 rectangle of stars.
for row in range(4):
    line = ""
    for col in range(3):
        line = line + "*"
    print(line)

# Problem 5
# Create a 2D list of numbers.
# Print the sum of all numbers in the 2D list.

grin = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]

]

total = 0
for row in range(len(grid)):
    for col in range(len(grid[row]));
        total = total + grid[row][col]
print(total)