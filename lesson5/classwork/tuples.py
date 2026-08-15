# A tuple is like a list, but it cannot be changed (immutable)
point = (3, 5)
print(point)

print("x:", point[0])
print("y:", point[1])

print("Length:", len(point))

# Tuples can hold mixed types too
meal = ("Pizza", 30, "Grams")
print(meal)

# You can loop through a tuple
for item in meal:
    print(item)