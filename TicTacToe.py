def fullBoard(board):
    if " " in board:
        return False
    else:
        return True


def printBoard(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])


def isWinner(board, sign):
    return ((board[7] == sign and board[8] == sign and board[9] == sign) or  # across the top
            (board[4] == sign and board[5] == sign and board[6] == sign) or  # across the middle
            (board[1] == sign and board[2] == sign and board[3] == sign) or  # across the bottom
            (board[7] == sign and board[4] == sign and board[1] == sign) or  # down the left side
            (board[8] == sign and board[5] == sign and board[2] == sign) or  # down the middle
            (board[9] == sign and board[6] == sign and board[3] == sign) or  # down the right side
            (board[7] == sign and board[5] == sign and board[3] == sign) or  # diagonal
            (board[9] == sign and board[5] == sign and board[1] == sign))  # diagonal


if __name__ == '__main__':
    board = [" "] * 10
    board[0] = "-1"
    signX = "X"
    sign0 = "0"
    moves = 9
    while True:
        print("Set the x in the board: type your n")
        n = int(input())
        while True:
            if board[n] == signX or board[n] == sign0:
                print("This place is already completed. Please give me another input:")
                n = int(input())
            else:
                board[n] = signX
                moves = moves - 1
                break
        if isWinner(board, signX) == True:
            printBoard(board)
            print("The X player won this game!")
            break
        if moves == 0:
            print("It's a TIE.")
            printBoard(board)
            break
        print("Set the 0 in the board: type your n")
        n = int(input())
        while True:
            if board[n] == signX or board[n] == sign0:
                print("This place is already completed. Please give me another input:")
                n = int(input())
            else:
                board[n] = sign0
                moves = moves - 1
                break
        if isWinner(board, sign0) == True:
            printBoard(board)
            print("The 0 player won this game!")
            break
