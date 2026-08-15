words = ["dog", "elephant", "cat", "bird"]
print("Original:", words)

# Sort by word length instead of alphabetical order
words.sort(key=len)
print("Sorted by length:", words)

students = [("Ava", 95), ("Ben", 88),("Kai", 73)]

# A key function tells python what value to sort by
def get_score(student):
    return student[1]

students .sort(key=get_score)
print("Sorted by score:", students)

# reverse=True sorts from biggest to smallest
students.sort(key=get_score, reverse=True)
print("Sorted by score backwards:", students)