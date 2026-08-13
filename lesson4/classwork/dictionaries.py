 # A dictionary maps keys to values
person = {
    "name" : "Yaseen",
    "age" : 15,
    "city" : "Seattle"
}

print(person)

# Access a value in a dictionary
print(person["age"])
print(person["name"])

# Add a new key
person["favorite_food"] = "pizza"
print(person)

# Update a value
person["age"] = person["age"] + 1
print("New age:", person["age"])

# Check if a key exists
print("name" in person)
print("height" in person)