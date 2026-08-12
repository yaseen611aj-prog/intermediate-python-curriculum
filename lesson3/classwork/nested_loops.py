# A nested loop is a loop inisde another loop
for i in range(3):
    for j in range(4):
        print("i:", i, "j:", j)

# Print a small multiplication table
for row in range(1, 4):
    for col in range(1, 4):
        print(row * col)

# Build rows of stars using nested loops
for row in range(6):
    line = ""
    for col in range(row):
        line = line + "*"
    print(line)