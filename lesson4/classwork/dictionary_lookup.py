# A lookup problem uses a key to find a value
phonebook = {
    "Ava" : "555-1111",
    "Ben" : "555-2222",
    "Kai" : "555-3333"
}

# Check if a key is in the dictionary before using it
name = "Ben"
if name in phonebook:
    print(name, "has phone number", phonebook[name])
else: print("Unknown contact")