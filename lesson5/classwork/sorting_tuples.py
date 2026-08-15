points = [(3, 5), (1, 9), (1, 2), (4, 0)]
print("Original", points)

# Tuples sort by the first value, then the second value
points.sort()
print("Sorted:", points)

students = [("Ava", 95), ("Ben", 88),("Kai", 73)]
print(students)

# Loop through a list of tuples
for name, score in students:
    print(name, "scored", score)