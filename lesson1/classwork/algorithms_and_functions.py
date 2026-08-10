numbers = [1, 2, 3, 4, 5]

# Sum algorithm
total = 0
for i in range (len(numbers)):
    total = total + numbers[i]
print("Sum of numbers:", total)

# Count algorithm
count = 0
for i in range(len(numbers)):
    if numbers [i] > 5:
        count = count + 1
print("Count of numbers greater than 5:", count)

# Biggest item algorithm
biggest = numbers[0]
for i in range(len(numbers)):
    if numbers[i] > biggest:
        biggest = numbers[i]
print("Biggest number:", biggest)

# Functions let us reuse code
def add_numbers(a, b):
    return a + b

answer = add_numbers(3, 5)
print("Answer:", answer)

# Local variables only exist inside the function
def double_number(num):
    result = num * 2
    return result
print(double_number(6))