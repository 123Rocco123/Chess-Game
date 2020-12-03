#Chess Game

#Tower = T, Horse = H, Bishop = B, King = K, Queen = Q, Pawn = P

pieces = " ".join(['T','H','B','K','Q','B','H','T'])
pawns = " ".join(['P','P','P','P','P','P','P','P'])

rows =  ([0,1,2,3,4,5,6,7,8])
rows1 = [" ".join(['1', '2', '3', '4', '5', '6', '7', '8'])]
rows_direction = rows[::-1]

blacks = [pieces, pawns]
whites = [pieces, pawns]
line = "".center(len(pieces), "-")

board_row = " ".join(['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'])
white_space = [board_row, board_row, board_row, board_row]

def chess():
    global chess_board, test

    chess_board = []
    chess_board.extend(blacks)
    chess_board.extend(white_space)
    chess_board.extend(whites)
    chess_board.extend(rows1)

    test = (zip(rows_direction, chess_board))

    for x in test:
        print(x)
print("Welcome to Chess".center(70))

chess()

print("Game Rules\n\nIf you want to move a piece, then you have to write the letter of that piece when prompted to, and then specifiy the direction you want to go to. ")

white_piece = ("What piece do you want to move (Row, Letter)? ")

def movement(x):
    pass