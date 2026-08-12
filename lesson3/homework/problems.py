# Problem 1
# Ask the user for a number n.
# Print all multiples of 3 from 0 to n (including n if it is a multiple of 3).
n = int(input("Enter a number n: "))

if n >= 0:
    multiples_of_3 = [num for num in range(0, n + 1) if num % 3 == 0]
else:
    multiples_of_3 = [num for num in range(n, 1, 1) if num % 3 == 0]

print(multiples_of_3)


# Problem 2
# Ask the user for a number n.
# Build a list of the squares from 1*1 up to n*n.
# Print the list.
n = int(input("Enter a number n: "))
squares = [i * i for i in range(1, n + 1)]
print(squares)



# Problem 3
# Use nested loops to print a triangle of stars with 5 rows.
# The first row has 1 star, the second row has 2 stars, and so on.
for row in range(1, 6):
    print("*" * row)


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

print(count)




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
print(word)
