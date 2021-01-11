#Chess Game
#Tower = T, Horse = H, Bishop = B, King = K, Queen = Q, Pawn = P
def chess_board1():
    global chess_board0, columb

    chess_board0 = ['R21','H21','B21','K2','Q2','B22','H22','R22', 
                    'P21','P22','P23','P24','P25','P26','P27','P28',
                    'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 
                    'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 
                    'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 
                    'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 
                    'P11','P12','P13','P14','P15','P16','P17','P18', 
                    'R11','H11','B12','K11','Q11','B12','H12','R12', 
                    " ", " ", " ", " ", " ", " ", " ", " ", " "]
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
    elif piece == "T1" or piece == "T2" or piece == "TA" or piece == "TB":
        piece0 = input("Where do you want to move that piece to? ").upper()
        piece2 = chess_board0.index(piece0)

        vert = [8,16,24,32,40,48,56,64]
        horiz = [1,2,3,4,5,6,7]
        
        for x in vert:
            if chess_board0[piece2] == chess_board0[piece1 - x]:
                chess_board0[piece1], chess_board0[piece2] = chess_board0[piece2], chess_board0[piece1]
        for x in horiz:
            if chess_board0[piece2] == chess_board0[piece1 + x]:
                chess_board0[piece1], chess_board0[piece2] = chess_board0[piece2], chess_board0[piece1]
            elif chess_board0[piece2] == chess_board0[piece1 - x]:
                chess_board0[piece1], chess_board0[piece2] = chess_board0[piece2], chess_board0[piece1]
        chess_format(chess_board0)    
    

class pieceMovement:
    def rules(self):
        teams = ["1", "2"]
        possible_positions = ["1", "2", "3", "4", "5", "6", "7", "8"]
        pieces = ["R", "H", "B", "K", "Q"]

        desired_move = input("Where do you want to move the piece to? ")
        
        for statuets in pieces: 
            for numbers in possible_positions:
                for team in teams:
                    if self.selected_piece == "P" + team + numbers:
                        piece = "P" + team + numbers
                        if desired_move == chess_board0[piece - 8] and chess_board0[piece - 8] == "X":
                            chess_board0[piece1], chess_board0[piece2] = chess_board0[piece2], chess_board0[piece1]

                        elif desired_move == (chess_board0[piece - 7] and chess_board0[piece - 7] != "X" and chess_board0[piece - 7] != pieces + "1" + numbers) or (chess_board0[piece - 9] and chess_board0[piece - 9] != "X" and chess_board0[piece - 9] != pieces + "1" + numbers):
                            chess_board0[self.selected_piece], chess_board0[desired_move] = chess_board0[desired_move], chess_board0[self.selected_piece]
                            chess_board0[desired_move] = "X"

                    #This if statement is used to determine where the rook (tower) is allowed to move on the chess board.
                        #Both the vertical and horizontal movements are seperate from one another to make sure that the chances of an error occuring are decreased. 
                    elif self.selected_piece == "R" + team + numbers:
                        piece = "R" + team + numbers
                        if desired_move == chess_board0[piece * numbers] and chess_board0[piece * numbers] == "X":
                            chess_board0[self.selected_piece], chess_board0[desired_move] = chess_board0[desired_move], chess_board0[self.selected_piece]
                        
                        elif desired_move  == (chess_board0[piece + numbers] and chess_board0[piece + numbers] == "X" ) or (chess_board0[piece - numbers] and chess_board0[piece - numbers] == "X" ):
                            chess_board0[self.selected_piece], chess_board0[desired_move] = chess_board0[desired_move], chess_board0[self.selected_piece]
                        
                        #This else if statement is to specify how a rook can take another piece from the other team in a vertical plane. 
                        elif desired_move == chess_board0[piece * numbers] and chess_board0[piece * numbers] != "X" and chess_board0[piece * numbers] != pieces + "1" + numbers:
                            chess_board0[self.selected_piece], chess_board0[desired_move] = chess_board0[desired_move], chess_board0[self.selected_piece]
                            chess_board0[desired_move] = "X"
                        
                        #This else if statement is to specify how a rook can take another piece from the other team in a horizontal plane. 
                        elif desired_move == ((chess_board0[piece + numbers] and chess_board0[piece + numbers] == "X" ) or (chess_board0[piece - numbers] and chess_board0[piece - numbers] == "X" )) and chess_board0[piece * numbers] != pieces + "1" + numbers:
                            chess_board0[self.selected_piece], chess_board0[desired_move] = chess_board0[desired_move], chess_board0[self.selected_piece]
                            chess_board0[desired_move] = "X"

    def move(self):
        selected_piece = input("What piece do you want to move?")

        for x in chess_board0:
            if selected_piece == x:
                self.rules()


#print("Welcome to Chess".center(70))
#print("Game Rules\n\nIf you want to move a piece, then you have to write the letter of that piece when prompted to, and then specifiy the direction you want to go to. ")

chess_board1()
for x in range(3):
    movement()