import numpy as np
import random
from numpy.lib.shape_base import column_stack



class connect4Board():

    def __init__(self):
        self.board = None
        self.boardsize_length = 7 #column
        self.boardsize_height = 6 #row
        self.black = 'b'
        self.white = 'w'
        self.currentPlayer = None
        self.NS = 8
        self.WE = 1
        #init_endgame
        self.end_game = False
        self.winner = None
        self.window = 4

    
    
    #change from ['b'，'w'] ->[1,2]
    def setStartingPlayer(self):
        if self.currentPlayer is None:
            self.currentPlayer = self.black

    

    def convertPieceInt(self,piece: str):
        pieceInt = None

        if piece == self.black:
            pieceInt = 1
        else:
            pieceInt = 2

        return pieceInt

    '''
      a b c d e f g
     _________________
   6 | 0 0 0 0 0 0 0 | 6
   5 | 0 0 0 0 0 0 0 | 5
   4 | 0 0 0 0 0 0 0 | 4
   3 | 0 0 0 0 0 0 0 | 3
   2 | 0 0 0 0 0 0 0 | 2
   1 | 0 0 0 0 0 0 0 | 1
     _________________
      a b c d e f g
    
    '''
    
    def drawBoard(self):
        self.board = np.zeros((self.boardsize_height,self.boardsize_length))
        return self.board
    


    def is_valid(self,play):

        return self.board[0,play] == 0

    def legalMoves(self):
        columns = 'abcdefg'
        legalPositions = []
        for i, col in enumerate(columns):#range(self.boardsize_length):
            if self.is_valid(i):
                legalPositions.append(i)
        
        return legalPositions

    def get_row_col(self,play):
        for row in range(self.boardsize_height-1,-1,-1):
            if self.board[row,play]==0:
                return row


        
    


    def play(self,playPos):
        
        player = self.currentPlayer
        print("current play is ", player)
        change = False
        boardPos = 'abcdefg'
        position = playPos

        if position not in boardPos:
            print("Wrong position")
            return change

        play = boardPos.find(position)#find relative index
        if not self.is_valid(play):#only need to check the first row
            print("This column is full!")
            return change

        print("im here",play)
        for i in range(self.boardsize_height-1,-1,-1):
            print(i)
            if self.board[i,play]==0:
                print("yes")
                
                self.board[i,play] = self.convertPieceInt(player)
                #check end game
                player_int = self.board[i,play]
                end = self.check_end_game(player_int)
                if end:
                    self.winner = self.currentPlayer
                    self.end_game = True
                    print('GG')
                    print('winner is ', self.winner)
                change = True
                break
        return change
            
                

    def changePlayer(self,change):
        if change is True:
            print("test123")
            if self.currentPlayer == self.black:
                self.currentPlayer = self.white
            elif self.currentPlayer == self.white:
                self.currentPlayer = self.black

        return

    def printBoard(self):
        print(self.board)
        return



    def check_end_game(self,player_int):
        #citation: 
        # https://stackoverflow.com/questions/29949169/python-connect-4-check-win-function
#check rows for connected four only first four as possible start
        for col in range(self.boardsize_length-3):
            for row in range(self.boardsize_height):
                if self.board[row][col] == player_int and self.board[row][col+1] == player_int  and self.board[row][col+2] == player_int and self.board[row][col+3] == player_int:
                    return True
#check columns for connected four only first four as possible start
        for col in range(self.boardsize_length):
            for row in range(self.boardsize_height-3):
                if self.board[row][col] == player_int and self.board[row+1][col] == player_int  and self.board[row+2][col] == player_int and self.board[row+3][col] == player_int:
                    return True
#check diags for y = x direction, since starter can only be  four columns and  4 rows
        for col in range(self.boardsize_length-3):
            for row in range(self.boardsize_height-3):
                if self.board[row][col] == player_int and self.board[row+1][col+1] == player_int  and self.board[row+2][col+2] == player_int and self.board[row+3][col+3] == player_int:
                    return True
##check diags for y = -x direction,since starter can only start at and before row 3 and first 4 columns
        for col in range(self.boardsize_length-3):
            for row in range(self.boardsize_height-4,self.boardsize_height):
                if self.board[row][col] == player_int and self.board[row-1][col+1] == player_int  and self.board[row-2][col+2] == player_int and self.board[row-3][col+3] == player_int:
                    return True

        

        #solver
        #minimax
        #score?


    def evaluate_window(self,window, player_int):
        score = 0
        opp_play = 2#white
        if player_int == 2:#black
            opp_play = 1#white

        if window.count(player_int) == 4:
           score += 100
        elif window.count(player_int) == 3 and window.count(0) == 1:
           score += 5
        elif window.count(player_int) == 2 and window.count(0) == 2:
           score += 2
        
        

        if window.count(opp_play) == 3 and window.count(0) == 1:
            score -= 10

        elif window.count(opp_play) == 2 and window.count(0) == 2:
           score -= 4
        # print(window)
        return score

    def scoring(self,player_int,board):
        score = 0

	## Score center column
        center_array = [int(i) for i in board[:, self.boardsize_length//2]]
        center_count = center_array.count(player_int)
        score += center_count * 3

        ## Score Horizontal
        for r in range(self.boardsize_height):
            row_array = [int(i) for i in list(board[r,:])]
            for c in range(self.boardsize_length-3):
                window = row_array[c:c+self.window]
                score += self.evaluate_window(window, player_int)

        ## Score Vertical
        for c in range(self.boardsize_length):
            col_array = [int(i) for i in list(board[:,c])]
            for r in range(self.boardsize_height-3):
                window = col_array[r:r+self.window]
                score += self.evaluate_window(window, player_int)

        ## Score posiive sloped diagonal
        for r in range(self.boardsize_height-3):
            for c in range(self.boardsize_length-3):
                window = [board[r+i][c+i] for i in range(self.window)]
                score += self.evaluate_window(window, player_int)

        for r in range(self.boardsize_height-3):
            for c in range(self.boardsize_length-3):
                window = [board[r+3-i][c+i] for i in range(self.window)]
                score += self.evaluate_window(window, player_int)

        return score


    '''
    function minimax(node, depth, maximizingPlayer) is
        if depth = 0 or node is a terminal node then
            return the heuristic value of node
        if maximizingPlayer then
            value := −∞
            for each child of node do
                value := max(value, minimax(child, depth − 1, FALSE))
            return value
        else (* minimizing player *)
            value := +∞
            for each child of node do
                value := min(value, minimax(child, depth − 1, TRUE))
            return value
    '''

    
    '''
    def is_terminal_node(self,player_int):
        return check_end_game(self,player_int) or len(legalMoves()== 0)
'''
    def simulate(self):
        best_score = 0

        legalMoves = self.legalMoves()
        best_col = random.choice(legalMoves)
        for col in legalMoves:
            row = self.get_row_col(col)
            temp_board = self.board.copy()
            temp_board[row,col] = 2
            score = self.scoring(2,temp_board)
            if score > best_score:
                best_score = score
                best_col = col
        return best_col
    







board = connect4Board()

print(board.drawBoard())
board.setStartingPlayer()
print(board.currentPlayer)

while not board.end_game:#if not over
    position = input("Where to play? \n")
    change = board.play(position)
    print("change is ",change)

    board.changePlayer(change)
    board.printBoard()

    if board.currentPlayer == board.white and not board.end_game:
        boardPos = 'abcdefg'
        #playpos = random.choice(boardPos)
        playpos = board.simulate()

        play_ch = boardPos[playpos]

        change = board.play(play_ch)
        print("change is ",change)

        board.changePlayer(change)
        board.printBoard()




    
