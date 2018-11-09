# CMPT 120 Intro to Programming
# Lab #6 – Lists and Error Handling
# Author: Joey LoRusso
# Created: 2018-11-08

symbol = [ " ", "x", "o" ]

def printRow(row):
    # initialize output to the left border
    output = "|"
    # for each square in the row...
    for cell in row:
        # add to output the symbol for this square followed by a border
        output += " " +symbol[cell] + " |"
        # print the completed output for this row
    print(output)
    pass

def printBoard(board):
    # print the top border
    print("+-----------+")
    # for each row in the board...
    for i in board:
        # print the row
        printRow(i)
        #print("|   |   |   |")
        # print the next border
        print("+-----------+")
    pass

def markBoard(board, row, col, player):
    # check to see whether the desired square is blank
    if board[int(row)][int(col)] == 0:
        # if so, set it to the player number
        board[int(row)][int(col)] = player
    pass

def getPlayerMove():
    r = input("Enter a row (0, 1, or 2): ") # prompt the user separately for the row and column numbers
    c = input("Enter a column (0, 1, or 2): ")
    return (r,c) # then return that row and column instead of (0,0)

def hasBlanks(board):
    # for each row in the board...
    for i in range(len(board)):
        # for each square in the row...
        for j in range(len(board[i])):
            # check whether the square is blank
            if board[i][j] == 0:
                # if so, return True
                return True
    return False # if no square is blank, return False

def main():
    board = [[0,0,0],[0,0,0],[0,0,0]]
    player = 1
    while hasBlanks(board):
        printBoard(board)
        row,col = getPlayerMove()
        markBoard(board,row,col,player)
        player = player % 2 + 1 # switch player for next turn
main()
