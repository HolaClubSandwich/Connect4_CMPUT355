import numpy as np



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
        #init_endgame
        self.end_game = False
        self.winner = None

    
    
    #change from ['b'w'] ->[1,2]
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

    def play(self):
        
        player = self.currentPlayer
        print("current play is ", player)
        change = False
        boardPos = 'abcdefg'
        position = input("Where to play? (a,b,c,d,e,f,g)\n")

        if position not in boardPos:
            print("Wrong position")
            return change

        playPos = boardPos.find(position)
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

        

        
    







board = connect4Board()

print(board.drawBoard())
board.setStartingPlayer()
print(board.currentPlayer)

while not board.end_game:#if not over
    change = board.play()
    print("change is ",change)
    board.changePlayer(change)
    board.printBoard()
    