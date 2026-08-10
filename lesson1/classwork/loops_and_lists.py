# for loops repeat code a certain number of times
for i in range(5):
    print("Hello, world!")

for i in range(6):
    print(i)

# while loops repeat while a condition is true 
i = 1
while i <= 5:
    print("While loop number:", i)
    i = i + 1

colors = ["red", "green", "blue", "yellow"]

print("First color:", colors[0]) # lists start at index 0
print("Second color:", colors[1])
print("Third color:", colors[2])
print("Fourth color:", colors[3])

print("List length:", len(colors)) # len() gives us the length of a list

# Loop through the list using indexes
for i in range(len(colors)):
    print("Color at index", i, "is", colors[i])