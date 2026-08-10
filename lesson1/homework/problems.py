# Problem 1
# Ask the user for two numbers.
# Print their sum, difference, and product.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2
print("Sum:", sum_result)
print("Difference:", difference_result)
print("Product:", product_result)



# Problem 2
# Ask the user for a number.
# Print whether the number is even or odd.
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")




# Problem 3
# Create a list of numbers.
# Print the biggest number in the list.
numbers = [3, 7, 2, 9, 5]
biggest = numbers[0]
for i in range(len(numbers)):
    if numbers[i] > biggest:
        biggest = numbers[i]
print("Biggest number:", biggest)



# Problem 4
# Use a while loop to print the numbers from 1 to 10.
i = 1
while i <= 10:
    print(i)

# Problem 5
# Create a function called count_above_10(numbers).
# It should return how many numbers in the list are above 10.
# Call it and print the result.
def count_above_10(numbers):
    count = 0
    for n in numbers:
        if n > 10:
            count += 1
    return count

result = count_above_10([5, 15, 8, 12, 3])
print("Count of numbers above 10:", result)
