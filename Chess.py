#Chess Game
#Tower = T, Horse = H, Bishop = B, King = K, Queen = Q, Pawn = P
def chess_board1():
    global chess_board0, columb

    chess_board0 = ['T1','H1','B1','K1','Q1','B1','H1','T1', 'PA','PB','PC','PD','PE','PF','PG','PH','W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8', 'WA', 'WB', 'WC', 'WD', 'WE', 'WF', 'WG', 'WH', 'WI', 'WJ', 'WK', 'WL', 'WM', 'WN', 'WO', 'WP', 'WQ', 'WR', 'WS', 'WT', 'WU', 'WV', 'WW', 'WX', 'P1','P2','P3','P4','P5','P6','P7','P8', 'T2','H2','B2','K2','Q2','B2','H2','T2']
    columb = ["1","2","3","4","5","6","7","8"]
    
    #Blacks
    print("Row:8|", " ".join(chess_board0[0:8]))
    print("    7|", " ".join(chess_board0[8:16]))
    #White Space
    print("    6|", " ".join(chess_board0[16:24]))
    print("    5|", " ".join(chess_board0[24:32]))
    print("    4|", " ".join(chess_board0[32:40]))
    print("    3|", " ".join(chess_board0[40:48]))
    #Whites
    print("    2|", " ".join(chess_board0[48:56]))
    print("    1|", " ".join(chess_board0[56:64]))
    print("      ========================")
    print("Column:" +  "  ".join(columb))

def chess_format(x):
    global columb

    print("Row:8|", " ".join(x[0:8]))
    print("    7|", " ".join(x[8:16]))
    #White Space
    print("    6|", " ".join(x[16:24]))
    print("    5|", " ".join(x[24:32]))
    print("    4|", " ".join(x[32:40]))
    print("    3|", " ".join(x[40:48]))
    #Whites
    print("    2|", " ".join(x[48:56]))
    print("    1|", " ".join(x[56:64]))
    print("      ========================")
    print("Column:" +  "  ".join(columb))


def movement():
    global chess_board0

    piece = input("What piece do you want to move? ").upper()
    piece1 = chess_board0.index(piece)

    if piece == 'P1'or piece =='P2'or piece =='P3'or piece =='P4'or piece =='P5'or piece =='P6'or piece =='P7'or piece =='P8':
        #Pawn Code for White Team
        piece0 = input("Where do you want to move that piece to? ").upper()
        piece2 = chess_board0.index(piece0)
        if chess_board0[piece2] == chess_board0[piece1 - 8]:
            chess_board0[piece1], chess_board0[piece2] = chess_board0[piece2], chess_board0[piece1]
            chess_format(chess_board0)
        else:
            print("You can't move there, try again.")
            movement()
    elif piece == 'PA'or piece =='PB'or piece =='PC'or piece =='PD'or piece =='PE'or piece =='PF'or piece =='PG'or piece =='PH':
        #Pawn Code for Black Team
        piece0 = input("Where do you want to move that piece to? ").upper()
        piece2 = chess_board0.index(piece0)
        print(piece1, piece2)
        if chess_board0[piece2] == chess_board0[piece1 + 8]:
            chess_board0[piece1], chess_board0[piece2] = chess_board0[piece2], chess_board0[piece1]
            chess_format(chess_board0)
        else:
            print("You can't move there, try again.")
            movement()
    

#print("Welcome to Chess".center(70))
#print("Game Rules\n\nIf you want to move a piece, then you have to write the letter of that piece when prompted to, and then specifiy the direction you want to go to. ")

chess_board1()
for x in range(3):
    movement()