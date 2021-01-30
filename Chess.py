#Chess Game

chess_board0 = ['R21','K21','B21','K2','Q2','B22','K22','R22', 
                'P21','P22','P23','P24','P25','P26','P27','P28',
                'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 
                'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 
                'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 
                'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 
                'P11','P12','P13','P14','P15','P16','P17','P18', 
                'R11','K11','B12','K1','Q11','B12','K12','R12', 
                " ", " ", " ", " ", " ", " ", " ", " ", " "]
columb = ["1","2","3","4","5","6","7","8"]

def chess_print():    
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


class pieceMovement:

    #This function will be used to determine which piece to move, and where to move it to.
    def call_func(self):
        piece_to_move = input("What piece do you want to move (LetterNumber)? ")

        desired_move = input(f"Where do you want to move {piece_to_move} to (Same Format)? ")

        #The following will be used as a verification step where we check to see if the position that the user inputed is correct or not. 
        for positions in chess_board0:
            if positions == chess_board0[piece_to_move]:
                pass
            else:
                ticker += 1

        if ticker == len(chess_board0):
            print("Your move is invalid.")
        else:
            pass

    #This function is used to determine how the movement of the king is determined. 
    def king_move(self, position, negative_position, side):
        #This series of else if statemetns is used to determine the positive movement of the king piece. 
        if self.desired_move == chess_board0[chess_board0[self.piece] + position] and chess_board0[chess_board0[self.piece] + position] == "X":
            self.switch
        elif self.desired_move == chess_board0[chess_board0[self.piece] + position] and chess_board0[chess_board0[self.piece] + position] != "X" and chess_board0[chess_board0[self.piece] + position] == self.pieces + self.team:
            self.switch
            chess_board0[self.desired_position] = "X"
        
        #This series of else if statements is used to determine the negative movement of the king piece.
        elif self.desired_move == chess_board0[chess_board0[self.piece] + negative_position] and chess_board0[chess_board0[self.piece] + negative_position] == "X":
            self.switch
        elif self.desired_move == chess_board0[chess_board0[self.piece] + negative_position] and chess_board0[chess_board0[self.piece] + negative_position] != "X" and chess_board0[chess_board0[self.piece] + negative_position] == self.pieces + self.team:
            self.switch
            chess_board0[self.desired_position] = "X"

        #This series of else if statements is used to determine the lateral movement of the king piece. 
        elif self.desired_move == chess_board0[chess_board0[self.piece] + side] and chess_board0[chess_board0[self.piece] + side] == "X":
            self.switch
        elif self.desired_move == chess_board0[chess_board0[self.piece] + side] and chess_board0[chess_board0[self.piece] + side] != "X" and chess_board0[chess_board0[self.piece] + side] == self.pieces + self.team:
            self.switch
            chess_board0[self.desired_position] = "X"

    #This function is used to determine the movement of the queen piece. 
        #The code is identical to the king with the difference being that there is a new argument that the function takes into consideration. 
    def queen_move(self, position, negative_position, side, multiples):
        #This series of else if statemetns is used to determine the positive movement of the king piece. 
        if self.desired_move == chess_board0[chess_board0[self.piece] + position * multiples] and chess_board0[chess_board0[self.piece] + position * multiples] == "X":
            self.switch
        elif self.desired_move == chess_board0[chess_board0[self.piece] + position * multiples] and chess_board0[chess_board0[self.piece] + position * multiples] != "X" and chess_board0[chess_board0[self.piece] + position * multiples] == self.pieces + self.team:
            self.switch
            chess_board0[self.desired_position] = "X"
        
        #This series of else if statements is used to determine the negative movement of the king piece.
        elif self.desired_move == chess_board0[chess_board0[self.piece] + negative_position * multiples] and chess_board0[chess_board0[self.piece] + negative_position * multiples] == "X":
            self.switch
        elif self.desired_move == chess_board0[chess_board0[self.piece] + negative_position * multiples] and chess_board0[chess_board0[self.piece] + negative_position * multiples] != "X" and chess_board0[chess_board0[self.piece] + negative_position * multiples] == self.pieces + self.team:
            self.switch
            chess_board0[self.desired_position] = "X"

        #This series of else if statements is used to determine the lateral movement of the king piece. 
        elif self.desired_move == chess_board0[chess_board0[self.piece] + side * multiples] and chess_board0[chess_board0[self.piece] + side * multiples] == "X":
            self.switch
        elif self.desired_move == chess_board0[chess_board0[self.piece] + side * multiples] and chess_board0[chess_board0[self.piece] + side * multiples] != "X" and chess_board0[chess_board0[self.piece] + side * multiples] == self.pieces + self.team:
            self.switch
            chess_board0[self.desired_position] = "X"

    #This function is used to determine if there is a chess piece infront of the one that you want to move, and if the move that you want to do interfers. 
        #Pawns weren't included because they have a fixed movement, where they can only move one step in front of them, and when defining the movement for the pawn, the if condition specifies that the space has to be empty. 
        #Knights were also not included because of the fact that they're able to jump over friendly pieces, meaning that as long as the final destination is free, they're allowed to move there. 
    def team_kill(self, piece_type, direction, additional_movement):
        piece_dic = {"Rook" : [8,1,-1,-8],
                     "Bishop" : [9, 7, -9, -7],
                     "King" : [1, 7, 8, 9, -1, -7, -8, -9],
                     "Queen" : [1, 7, 8, 9, -1, -8, -7, -9]
                     }

        side_to_side = [-1, 1]

        for chess_pieces in piece_dic:
            if piece_type == chess_pieces:
                numbers_cycle = len(piece_dic[chess_pieces]) / 2
                
                if direction == "positive":
                    for spaces in piece_dic[chess_pieces[0:numbers_cycle]]:
                        if additional_movement == spaces:
                            #The additional movement is here to determine the first square of the direction of the piece. 
                                #Without it, the code would look to see if any pieces that were near the chosen piece were on the same team, and throw up the error below. 
                            if chess_board0[self.desired_move] == self.pieces + "1" + self.numbers:
                                print("Invalid move, there is a piece from your that's blocking you.")
                                self.rules()

                elif direction == "negative":
                    for spaces in piece_dic[chess_pieces[numbers_cycle:]]:
                        if additional_movement == spaces:
                            if chess_board0[self.desired_move] == self.pieces + "1" + self.numbers:
                                print("Invalid move, there is a piece from your that's blocking you.")
                                self.rules()

                elif direction == "horizontal":
                    for spaces in side_to_side:
                        if additional_movement == spaces:
                            if chess_board0[chess_board0[self.piece] + spaces] == self.pieces + "1" + self.numbers:
                                print("Invalid move, there is a piece from your that's blocking you.")
                                self.rules()

                else:
                    #The reason that we use pass here is because of the fact that if none of the conditions are met, then we want nothing to happen, and the code to continue off as it should. 
                    self.switch

    #This function is used to specify the movement of the pieces on the board. 
    def rules_movement(self, piece, numbers, vert1, vert2, horiz1, horiz2):
        #The if statement below is used to determine how the vertical movements of the piece, both in the positive (down) and negative (up) directions. 
        if self.desired_move == (chess_board0[chess_board0[piece] + vert1] and chess_board0[chess_board0[piece] * numbers] == "X" and chess_board0[chess_board0[piece] * numbers] != self.pieces + "1" + numbers) or \
            self.desired_move == (chess_board0[chess_board0[piece] + vert2] and chess_board0[chess_board0[piece] * numbers] == "X" and chess_board0[chess_board0[piece] * numbers] != self.pieces + "1" + numbers) or \
            self.desired_move == (chess_board0[chess_board0[piece] - vert1] and chess_board0[chess_board0[piece] * numbers] == "X" and chess_board0[chess_board0[piece] * numbers] != self.pieces + "1" + numbers) or \
            self.desired_move == (chess_board0[chess_board0[piece] - vert2] and chess_board0[chess_board0[piece] * numbers] == "X" and chess_board0[chess_board0[piece] * numbers] != self.pieces + "1" + numbers):
            self.switch

        #This else if statement is used to determine which positions are possible for the piece to move in the horizontal axis of the board.
            #An important difference here is that the same for loop is used as the one in the previous else if conditions, with the key difference being that the piece will only move if, and only if, the rows aren't the same. 
        elif self.desired_move == (chess_board0[chess_board0[piece] + horiz1] and chess_board0[chess_board0[self.piece] * numbers] == "X" and chess_board0[chess_board0[piece] * numbers] != self.pieces + "1" + numbers) or \
                self.desired_move == (chess_board0[chess_board0[piece] + horiz2] and chess_board0[chess_board0[piece] * numbers] == "X" and chess_board0[chess_board0[piece] * numbers] != self.pieces + "1" + numbers) or \
                self.desired_move == (chess_board0[chess_board0[piece] - horiz1] and chess_board0[chess_board0[piece] * numbers] == "X" and chess_board0[chess_board0[piece] * numbers] != self.pieces + "1" + numbers) or \
                self.desired_move == (chess_board0[chess_board0[piece] - horiz2] and chess_board0[chess_board0[piece] * numbers] == "X" and chess_board0[chess_board0[piece] * numbers] != self.pieces + "1" + numbers):
                    
            for row in self.rows:
                for indexes in self.rows[row]:
                    row_of_start = chess_board0[piece]
                    row_of_end = chess_board0[self.desired_move]
                                    
                    if indexes == row_of_start:
                        initial_row = row
                    if indexes == row_of_end:
                        final_row = row
                
            if self.same == True:
                if initial_row == final_row:
                    self.switch
                            
            elif self.same == False:
                if initial_row != final_row:
                    self.switch
                else:
                    print("Invalid movement.")
                    self.rules()
        #These else if statements are used to determine how the movement of the piece is to occur depending on if they want to take a piece from the other team, as well as if the move to take that piece is a vertical one. 
        elif self.desired_move == (chess_board0[chess_board0[piece] + vert1] and chess_board0[chess_board0[piece] * numbers] != "X" and chess_board0[chess_board0[piece] * numbers] != self.pieces + "1" + numbers) or \
            self.desired_move == (chess_board0[chess_board0[piece] + vert2] and chess_board0[chess_board0[piece] * numbers] != "X" and chess_board0[chess_board0[piece] * numbers] != self.pieces + "1" + numbers) or \
            self.desired_move == (chess_board0[chess_board0[piece] - vert1] and chess_board0[chess_board0[piece] * numbers] != "X" and chess_board0[chess_board0[piece] * numbers] != self.pieces + "1" + numbers) or \
            self.desired_move == (chess_board0[chess_board0[piece] - vert2] and chess_board0[chess_board0[piece] * numbers] != "X" and chess_board0[chess_board0[piece] * numbers] != self.pieces + "1" + numbers):
            self.switch
            chess_board0[self.desired_move] = "X"

        #If the move means taking a piece from the other team, as well as the move being horizontal, then the following code block will be executed. 
        elif self.desired_move == (chess_board0[chess_board0[piece] + horiz1] and chess_board0[chess_board0[piece] * numbers] != "X" and chess_board0[chess_board0[piece] * numbers] != self.pieces + "1" + numbers) or \
                self.desired_move == (chess_board0[chess_board0[piece] + horiz2] and chess_board0[chess_board0[piece] * numbers] != "X" and chess_board0[chess_board0[piece] * numbers] != self.pieces + "1" + numbers) or \
                self.desired_move == (chess_board0[chess_board0[piece] - horiz1] and chess_board0[chess_board0[piece] * numbers] != "X" and chess_board0[chess_board0[piece] * numbers] != self.pieces + "1" + numbers) or \
                self.desired_move == (chess_board0[chess_board0[piece] - horiz2] and chess_board0[chess_board0[piece] * numbers] != "X" and chess_board0[chess_board0[piece] * numbers] != self.pieces + "1" + numbers):
            
            for row in self.rows:
                for indexes in self.rows[row]:
                    row_of_start = chess_board0[piece]
                    row_of_end = chess_board0[self.desired_move]
                                    
                    if indexes == row_of_start:
                        initial_row = row
                    if indexes == row_of_end:
                        final_row = row
                
            if self.same == True:
                if initial_row == final_row:
                    self.switch
                    chess_board0[self.desired_move] = "X"
                            
            elif self.same == False:
                if initial_row != final_row:
                    self.switch
                    chess_board0[self.desired_move] = "X"
                else:
                    print("Invalid movement.")
                    self.rules()

    def rules(self):
        teams = ["1", "2"]
        possible_positions = ["1", "2", "3", "4", "5", "6", "7", "8"]
        pieces = ["R", "H", "B", "K", "Q"]

        rows = {"1" : [0,1,2,3,4,5,6,7],
                "2" : [8,9,10,11,12,13,14,15],
                "3" : [16,17,18,19,20,21,22,23],
                "4" : [24,25,26,27,28,29,30,31],
                "5" : [32,33,34,35,36,37,38,39],
                "6" : [40,41,42,43,44,45,46,47],
                "7" : [48,49,50,51,52,53,54,55],
                "8" : [56,57,58,59,60,61,62,63]
                }

        #This function call is used to ask the player what piece they want to move, and where they want to move it to. 
        self.call_func()
        
        switch = chess_board0[self.selected_piece], chess_board0[self.desired_move] = chess_board0[self.desired_move], chess_board0[self.selected_piece]

        for statuets in pieces: 
            for numbers in possible_positions:
                for team in teams:
                    if self.selected_piece == "P" + team + numbers:
                        piece = "P" + team + numbers
                        if self.desired_move == chess_board0[piece - 8] and chess_board0[piece - 8] == "X":
                            chess_board0[piece], chess_board0[desired_move] = chess_board0[desired_move], chess_board0[piece]

                        elif self.desired_move == (chess_board0[chess_board0[piece] - 7] and chess_board0[chess_board0[piece] - 7] != "X" and chess_board0[chess_board0[piece] - 7] != pieces + "1" + numbers) or (chess_board0[chess_board0[piece] - 9] and chess_board0[chess_board0[piece] - 9] != "X" and chess_board0[chess_board0[piece] - 9] != pieces + "1" + numbers):
                            switch
                            chess_board0[self.desired_move] = "X"

                    #This if statement is used to determine where the rook (tower) is allowed to move on the chess board.
                        #Both the vertical and horizontal movements are seperate from one another to make sure that the chances of an error occuring are decreased. 
                    elif self.selected_piece == "R" + team + numbers:
                        piece = "R" + team + numbers
                        same = True

                        #This if statement is used to determine if the desired place that you want to move your piece to is free or not.
                            #It is important to note here that this if statemetn is only used to move the piece in a vertical direction on the board. 
                        if self.desired_move == chess_board0[piece + (8 * numbers)] and chess_board0[piece + (8 * numbers)] == "X":
                            if chess_board0[desired_move] % 8 == 0: 
                                self.team_kill("Rook", "positive", 8)
                            elif chess_board0[desired_move] > 1 and chess_board0[desired_move] < 8:
                                self.team_kill("Rook", "positive", 1)
                        
                        #This else if statement is used to determine how the piece is allowed to move from one place to another on the same row.
                            #What is important to note here is that the reason that this else if statement is much longer than the rest is because it has to specify that the switch can only occur for elements in the same row. 
                        elif self.desired_move == (chess_board0[chess_board0[piece] + numbers] and chess_board0[chess_board0[piece] + numbers] == "X") or (chess_board0[chess_board0[piece] - numbers] and chess_board0[chess_board0[[piece] - numbers]] == "X"):
                            for row in rows:
                                for indexes in rows[row]:
                                    row_of_start = chess_board0[piece]
                                    row_of_end = chess_board0[self.desired_move]
                                    
                                    if indexes == row_of_start:
                                        initial_row = row
                                    if indexes == row_of_end:
                                        final_row = row

                            if initial_row == final_row:
                                switch
                        
                        #This else if statement is to specify how a rook can take another piece from the other team in a vertical plane. 
                        elif self.desired_move == chess_board0[piece * numbers] and chess_board0[piece * numbers] != "X" and chess_board0[piece * numbers] != pieces + "1" + numbers:
                            switch
                            chess_board0[self.desired_move] = "X"
                        
                        #This else if statement is to specify how a rook can take another piece from the other team in a horizontal plane. 
                        elif self.desired_move == ((chess_board0[chess_board0[piece] + numbers] and chess_board0[chess_board0[piece] + numbers] != "X" ) or (chess_board0[chess_board0[piece] - numbers] and chess_board0[chess_board0[piece] - numbers] != "X" )) and chess_board0[chess_board0[piece] * numbers] != pieces + "1" + numbers:
                            for row in rows:
                                for indexes in rows[row]:
                                    row_of_start = chess_board0[piece]
                                    row_of_end = chess_board0[self.desired_move]

                                    if indexes == row_of_start:
                                        initial_row = row
                                    if indexes == row_of_end:
                                        final_row = row

                            if initial_row == final_row:
                                switch
                                chess_board0[self.desired_move] = "X"

                    #This else if statement is used to determine how the knight is supposed to move. 
                    elif self.selected_piece == "K" + team + numbers:
                        piece = "K" + team + numbers
                        same = False

                        self.rules_movement(self, piece, numbers, 17, 15, 10, 6)
                    
                    #This else if statement is uesd to determine how the bishop is supposed to move. 
                    elif self.selected_piece == "B" + team + numbers:
                        piece = "B" + team + numbers

                        future_move = chess_board0[piece]
                        diagonal_multiples = [1,2,3,4,5,6,7]

                        #The following if and if else statements are used to determine how the movement of the bishop is to be defined when the spot that the player wants to move it to is free.
                        for numbers in diagonal_multiples:
                            if self.desired_move[future_move + (9 * numbers)] and self.desired_move[future_move + (9 * numbers)] == "X":
                                switch
                            elif self.desired_move[future_move - (9 * numbers)] and self.desired_move[future_move - (9 * numbers)] == "X":
                                switch
                            elif self.desired_move[future_move + (7 * numbers)] and self.desired_move[future_move + (7 * numbers)] == "X":
                                switch
                            elif self.desired_move[future_move - (7 * numbers)] and self.desired_move[future_move - (7 * numbers)] == "X":
                                switch

                            #This set of else if statements are used to determine the movement of the bishop when it can take a piece from the other team. 
                                #Because of the unique movement restrictions of the bishop, the extra for loops that were used for the towers and knights aren't necessary.
                                #This is due to the fact that they can only move in an X, as well as being stuck to one tile color rather than being able to move to every square on the board. 
                            elif self.desired_move[future_move + (9 * numbers)] and desired_move[future_move + (9 * numbers)] != "X" and desired_move[future_move + (9 * numbers)] != pieces + "1" + numbers:
                                switch
                                chess_board0[desired_move] = "X"
                            elif self.desired_move[future_move - (9 * numbers)] and desired_move[future_move - (9 * numbers)] != "X" and desired_move[future_move - (9 * numbers)] != pieces + "1" + numbers:
                                switch
                                chess_board0[desired_move] = "X"
                            elif self.desired_move[future_move + (7 * numbers)] and self.desired_move[future_move + (7 * numbers)] != "X" and desired_move[future_move + (7 * numbers)] != pieces + "1" + numbers:
                                switch
                                chess_board0[desired_move] = "X"
                            elif self.desired_move[future_move - (7 * numbers)] and self.desired_move[future_move - (7 * numbers)] != "X" and desired_move[future_move - (7 * numbers)] != pieces + "1" + numbers:
                                switch
                                chess_board0[self.desired_move] = "X"

                    #This else if statement is used to determine the movement of the king piece. 
                    elif self.selected_piece == "K" + team:
                        piece = "K" + team

                        positive = [7,8,9]
                        negative = [-7,-8,-9]
                        side_to_side = [-1,1]

                        #The following for loops are used to cycle through all of the data in the lists above to allow the correct movement of the king to occur. 
                        for positive_nums in positive:
                            for negative_nums in negative:
                                for side_move in side_to_side:
                                    self.king_move(positive_nums, negative_nums, side_move)

                    #This else if statemetn is used to determine the movement of the queen piece. 
                    elif self.selected_piece == "Q" + team:
                        piece = "Q" + team

                        positive = [7,8,9]
                        negative = [-7,-8,-9]
                        side_to_side = [-1,1]

                        multiples = [1,2,3,4,5,6,7,8]

                        #The difference between the Queen piece and the King piece is that there is another for loop for the queen piece.
                            #The extra for loop is used to multiply the numbers so as to allow the piece to move the length of the board in one move. 
                        for positive_nums in positive:
                            for negative_nums in negative:
                                for side_move in side_to_side:
                                    for multipliers in multiples:
                                        self.queen_move(positive_nums, negative_nums, side_move, multipliers)

    def move(self):
        selected_piece = input("What piece do you want to move?")

        for x in chess_board0:
            if selected_piece == x:
                self.rules()

#print("Welcome to Chess".center(70))
#print("Game Rules\n\nIf you want to move a piece, then you have to write the letter of that piece when prompted to, and then specifiy the direction you want to go to. ")

chess_print()
for x in range(3):
    initiate = pieceMovement()
    initiate.rules()