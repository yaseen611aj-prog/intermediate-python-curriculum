# Building a string with a loop (using +)
name = "Max"
result = ""
for ch in name:
    result = result + ch + "-"
print(result)  # Output: M-a-x-

# Building a string by collecting pieces in a list and joining them
letters = ["p", "y", "t", "h", "o", "n"]
built = "".join(letters)
print(built)  # Output: python

# Make a new string with only the even index characters
word = "computer"
new_word = ""
for i in range(len(word)):
    if i % 2 == 0:
        new_word = new_word + word[i]