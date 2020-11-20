import numpy as np
import random
from copy import deepcopy
import math

class connect4Board():

    def __init__(self):
        self.board = None
        self.boardsize_length = 7
        self.boardsize_height = 6
        self.black = 'b'
        self.white = 'w'
        self.currentPlayer = None
        self.NS = 8
        self.WE = 1
        self.winner = None
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
    '''
    def play(self):
        
        player = self.currentPlayer
        if player == "b":
            print("current play is ", player)
            change = False
            boardPos = 'abcdefg'
            position = input("Where to play? \n")

            if position not in boardPos:
                print("Wrong position")
                return change
    
            playPos = boardPos.find(position)
            #print("playpos")
            #print(playPos)
            if not self.board[0,playPos] == 0:#only need to check the first row
                print("This column is full!")
                return change
    
            print("im here",playPos)
            for i in range(self.boardsize_height-1,-1,-1):
                print(i)
                if self.board[i,playPos]==0:
                    print("yes")
                    
                    self.board[i,playPos] = self.convertPieceInt(player)
                    #check end game
                    player_int = self.board[i,playPos]
                    end = self.check_end_game(player_int)
                    if end:
                        self.winner = self.currentPlayer
                        self.end_game = True
                        print('GG')
                        print('winner is ', self.winner)
                    change = True
                    break
            return change
        
        else:
            print("current play is ", player)
            change = False
            boardPos = 'abcdefg'
            pos = random.randrange(7)
            position = boardPos[pos]

            if position not in boardPos:
                print("Wrong position")
                return change
    
            playPos = boardPos.find(position)
            #print("playpos")
            #print(playPos)
            if not self.board[0,playPos] == 0:#only need to check the first row
                print("This column is full!")
                return change
    
            print("im here",playPos)
            for i in range(self.boardsize_height-1,-1,-1):
                print(i)
                if self.board[i,playPos]==0:
                    print("yes")
                    
                    self.board[i,playPos] = self.convertPieceInt(player)
                    #check end game
                    player_int = self.board[i,playPos]
                    end = self.check_end_game(player_int)
                    if end:
                        self.winner = self.currentPlayer
                        self.end_game = True
                        print('GG')
                        print('winner is ', self.winner)
                    change = True
                    break
            return change
            
        '''

    def play(self):
        player = self.currentPlayer
        print("current player is", player)
        change = False
        boardPos = 'abcdefg'
        position = input("Where to play? \n")

        if position not in boardPos:
            print("Wrong position")
            return change

        playPos = boardPos.find(position)
        if 0 not in self.board[:,playPos]:
            print("This column is full!")
            return change


        for i in range(self.boardsize_height-1,-1,-1):
            #print(i)
            if self.board[i,playPos]==0:
                #print("yes")
                self.board[i,playPos] = self.convertPieceInt(player)
               
                change = True
                break
        
        return change

    def changePlayer(self,change):
        if change is True:
            #print("test123")
            if self.currentPlayer == self.black:
                self.currentPlayer = self.white
            elif self.currentPlayer == self.white:
                self.currentPlayer = self.black

        return

    def printBoard(self):
        print(self.board)
        return
    '''
    def check_end_game(self,player_int):
        #citation: 
        # https://medium.com/@geoffrey.mariette/crazy-connect4-with-python-146d384f4cfb
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
    '''
    def check_end_game(self):
        checkplayer = self.convertPieceInt(self.currentPlayer)
        #citation: 
        # https://medium.com/@geoffrey.mariette/crazy-connect4-with-python-146d384f4cfb
        #check rows for connected four only first four as possible start
        for col in range(self.boardsize_length-3):

            for row in range(self.boardsize_height):
                if self.board[row][col] == checkplayer and self.board[row][col+1] == checkplayer  and self.board[row][col+2] == checkplayer and self.board[row][col+3] == checkplayer:
                    return True
        #check columns for connected four only first four as possible start
        for col in range(self.boardsize_length):
            for row in range(self.boardsize_height-3):
                if self.board[row][col] == checkplayer and self.board[row+1][col] == checkplayer  and self.board[row+2][col] == checkplayer and self.board[row+3][col] == checkplayer:
                    return True

        #check diags for y = x direction, since starter can only be  four columns and  4 rows
        for col in range(self.boardsize_length-3):
            for row in range(self.boardsize_height-3):
                if self.board[row][col] == checkplayer and self.board[row+1][col+1] == checkplayer  and self.board[row+2][col+2] == checkplayer and self.board[row+3][col+3] == checkplayer:
                    return True
        ##check diags for y = -x direction,since starter can only start at and before row 3 and first 4 columns
        for col in range(self.boardsize_length-3):
            for row in range(self.boardsize_height-4,self.boardsize_height):
                if self.board[row][col] == checkplayer and self.board[row-1][col+1] == checkplayer  and self.board[row-2][col+2] == checkplayer and self.board[row-3][col+3] == checkplayer:
                    return True
        
        return False
    
    

    def legalMoves(self,board):
        columns = 'abcdefg'
        legalPositions = []
        for i in range(self.boardsize_length):
            if 0 in board[:,i]:
                legalPositions.append(columns[i])
        
        return legalPositions

    def simulate(self):
        sim_Board = deepcopy(self.board)

        return


    def play_move(self,board,move,player):
        change = False
        boardPos = 'abcdefg'

        playPos = boardPos.find(move)
        #print("test-------------------------",board)
        for i in range(self.boardsize_height-1,-1,-1):
            if board[i,playPos]==0:
                board[i,playPos] = self.convertPieceInt(player)
               
                change = True
                break
        
        return change


    def evaluate_window(self,window, piece):
        score = 0
        opp_piece = 2#white
        if piece == 2:#black
            opp_piece = 1#white

        if window.count(piece) == 4:
           score += 100
        elif window.count(piece) == 3 and window.count(0) == 1:
           score += 5
        elif window.count(piece) == 2 and window.count(0) == 2:
           score += 2

        if window.count(opp_piece) == 3 and window.count(0) == 1:
            score -= 4
        # print(window)
        return score

    def scoring(self,board,piece):
        score = 0

	## Score center column
        center_array = [int(i) for i in board[:, self.boardsize_length//2]]
        center_count = center_array.count(piece)
        score += center_count * 3

        ## Score Horizontal
        for r in range(self.boardsize_height):
            row_array = [int(i) for i in list(board[r,:])]
            for c in range(self.boardsize_length-3):
                window = row_array[c:c+self.window]
                score += self.evaluate_window(window, piece)

        ## Score Vertical
        for c in range(self.boardsize_length):
            col_array = [int(i) for i in list(board[:,c])]
            for r in range(self.boardsize_height-3):
                window = col_array[r:r+self.window]
                score += self.evaluate_window(window, piece)

        ## Score posiive sloped diagonal
        for r in range(self.boardsize_height-3):
            for c in range(self.boardsize_length-3):
                window = [board[r+i][c+i] for i in range(self.window)]
                score += self.evaluate_window(window, piece)

        for r in range(self.boardsize_height-3):
            for c in range(self.boardsize_length-3):
                window = [board[r+3-i][c+i] for i in range(self.window)]
                score += self.evaluate_window(window, piece)

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
    def minimax(self,board,depth,maximizingPlayer):
        node = board
        legal_positions = self.legalMoves(node) 

        if depth ==0 or self.check_end_game()==True:
            if self.check_end_game():
                if self.winner == 'b':
                    return 1e6,None
                else:
                    return -1e6,None
            else:
                return self.scoring(board,self.black),None
        
        if maximizingPlayer:
            value = -math.inf
            pp = random.choice(legal_positions)#random move choice
            for col in legal_positions:
                newBoard = deepcopy(node)
                self.play_move(newBoard,pp,self.black)
                newVal = self.minimax(board,depth-1,False)[0]
                if newVal < value:
                    value = newVal
                    pp = col
            print("Max",newVal,pp)
            return newVal,pp
        
        else:
            value = math.inf
            pp = random.choice(legal_positions)#random move choice
            for col in legal_positions:
                newBoard = deepcopy(node)
                self.play_move(newBoard,pp,self.white)
                newVal = self.minimax(board,depth-1,True)[0]
                if newVal > value:
                    value = newVal
                    pp = col
            print("min",newVal,pp)
            return newVal, pp

            

        return

board = connect4Board()

print(board.drawBoard())
board.setStartingPlayer()
print(board.currentPlayer)

while not board.end_game:#if not over
    change = board.play()
    col,minimaxScore = board.minimax(board.board,3,True)
    print(col,minimaxScore)
    #print("change is ",change)
    if board.check_end_game():
        print("Game done ")
        break
    board.changePlayer(change)
    board.printBoard()
    print(board.check_end_game())
    

board.printBoard()
    
    

        
