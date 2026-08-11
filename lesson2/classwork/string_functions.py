text = "   Hello, World!   "
print("Raw text is:", text)

print(text.lower()) # make everything lowercase
print(text.upper()) # make everything uppercase
print(text.title()) # title case

print(text.strip()) # remove whitespace from both ends
print(text.strip().lower())

message = "bannana bread"
print("Count of a: ", message.count("a")) # count how many times a character appears
print("Find 'bread': ", message.find("bread")) # find the index of a substring

print(message.replace("bannana", "pumpkin")) # replace a substring with another