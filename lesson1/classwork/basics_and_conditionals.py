name = "Alex" # String variable
age = 12 # Integer variable
height = 5.2 # Float variable
likes_python = True # Boolean variable

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Likes Python:", likes_python)

# input() gives us a string
# int(input()) converts the string to an integer
num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")
# % gives us the remainder after division
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Logical operators let us combine conditions
if num > 0 and num < 100:
    print("The number is between 1 and 100")

if num < 0 or num > 100:
    print("The number is outside the normal range")