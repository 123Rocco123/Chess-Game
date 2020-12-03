#Chess Game

#Tower = T, Horse = H, Bishop = B, King = K, Queen = Q, Pawn = P

pieces = " ".join(['T','H','B','K','Q','B','H','T'])
pawns = " ".join(['P','P','P','P','P','P','P','P'])

blacks = [pieces, pawns]
whites = [pieces, pawns]

board_row = " ".join(['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'])
white_space = [board_row, board_row, board_row]

chess_board = []
chess_board.extend(blacks)
chess_board.extend(white_space)
chess_board.extend(whites)

#" ".join(chess_board)

for x in chess_board:
    print(x)