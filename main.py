import random

board = [[0 for _ in range(3)] for _ in range(3)]


def insertLetter(letter, pos):
    board[pos[0]][pos[1]] = letter


def spaceIsFree(pos):
    return board[pos[0]][pos[1]] == 0


def printBoard(bo):
    for i in range(3):
        for j in range(3):
            if bo[i][j] == 0:
                bo[i][j] = " "
        if i == 0:
            print(" ----------------- ")
        else:
            print("|-----|-----|-----|")

        for j in range(3):
            print("|", end="  ")

            if j == 2:
                print(bo[i][j], end="  |\n")
            else:
                print(str(bo[i][j]), end="  ")
            if bo[i][j] == " ":
                bo[i][j] = 0
    print(" ----------------- ")


def isWinner(board, le):
    for i in range(3):
        if board[i][0] == le and board[i][1] == le and board[i][2] == le:
            return True
        if board[0][i] == le and board[1][i] == le and board[2][i] == le:
            return True
    for i in range(3):
        if not board[i][i] == le:
            break
        if i == 2:
            return True
    for i in range(3):
        if not board[i][2 - i] == le:
            break
        if i == 2:
            return True
    return False


def playerMove():
    run = True
    while run:
        move = input("Please select a position to place an \"X\" (1 - 9): ")
        if move.isdigit:
            move = int(move)
            if move > 0 and move < 10:
                space = ((move - 1) // 3, (move - 1) % 3)
                if spaceIsFree(space):
                    insertLetter("X", space)
                    run = False
                else:
                    print("Please choose an open space to place an \"X\"!")
            else:
                print("Please enter a number from 1 - 9!")
        else:
            print("Please enter a number!")


def compMove(board):
    possibleMoves = [(x, y) for x in range(3) for y in range(3) if board[x][y] == 0]
    finalMove = 0, 0
    for let in ["O", "X"]:
        for move in possibleMoves:
            testBoard = [x[:] for x in board]
            testBoard[move[0]][move[1]] = let
            if isWinner(testBoard, let):
                finalMove = move
                return finalMove

    corners = []
    for i in possibleMoves:
        if i in [(0, 0), (0, 2), (2, 0), (2, 2)]:
            corners.append(i)
    if len(corners) > 0:
        finalMove = selectRandom(corners)
        return finalMove

    if (1, 1) in possibleMoves:
        finalMove = (1, 1)
        return finalMove

    edges = []
    for i in possibleMoves:
        if i in [(0, 1), (1, 0), (1, 2), (2, 1)]:
            edges.append(i)
    if len(edges) > 0:
        finalMove = selectRandom(edges)
        return finalMove

    return finalMove


def selectRandom(li):
    return random.choice(li)


def isBoardFull(board):
    return board.count(0) > 1


def main():
    print("Let's play Tic-Tac-Toe!")
    printBoard(board)

    while not isBoardFull((board)):
        if not isWinner(board, "O"):
            playerMove()
            printBoard(board)
        else:
            print("Sorry, O's won this time!")
            break
        if not isWinner(board, "X"):
            move = compMove(board)
            if move == 0:
                print("Tie Game!")
            else:
                insertLetter("O", move)
                print("Computer placed an \"O\" in position " + str(move) + ":")
                printBoard(board)
        else:
            print("Good job, X's won this time!")
            break

    if isBoardFull(board):
        print("Tie Game!")


if __name__ == '__main__':
    while True:
    	board = [[0 for _ in range(3)] for _ in range(3)]
        main()
        if not "y" in input("Do you want to play again? (Y/n) "):
            break
