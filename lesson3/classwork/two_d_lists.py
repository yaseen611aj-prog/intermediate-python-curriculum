# a 2D list can represent a grid
board = [
    [".", ".", "."],
    [".", "X", "."],
    [".", ".", "."]
]

# Print the board row by row
for row in range(len(board)):
    print(board[row])

print(board[1]) # access one row in the 2D list

board[0][2] = "0"
print("After change:")
for row in range(len(board)):
    print(board[row])