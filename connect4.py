import numpy as np
import random
from numpy.lib.shape_base import column_stack
import math



class connect4Board():

    def __init__(self):
        self.board = None
        self.boardsize_length = 7 #column
        self.boardsize_height = 6 #row
        self.black = 'black'
        self.white = 'white'
        self.currentPlayer = None
        self.NS = 8
        self.WE = 1
        #init_endgame
        self.end_game = False
        self.winner = None
        self.window = 4
        self.AI = None
        self.start = None

    
    
    #change from ['b'，'w'] ->[1,2]
    def setStartingPlayer(self,player):
        if player == 'b':
            self.currentPlayer = self.black
            self.start = self.black
            self.AI = 2
            return False
        elif player == 'w':
            self.currentPlayer = self.white
            self.start = self.white
            self.AI = 1
            return False
        elif player =='pvp':
            self.currentPlayer = self.black
            return False
        elif player == 'aivsai':
            self.currentPlayer = self.black
            return False
        elif player == 'aivsrand':
            self.currentPlayer = self.black
            return False



        else:
            
            print('invalid player!')
            return True



        
        

    def dropPlay(self, board, row, col, playerInt):
        board[row][col] = playerInt

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
        print("current play is: ", player)
        change = False
        boardPos = 'abcdefg'
        position = playPos

        if position not in boardPos:
            print("Position Invalid")
            return change

        play = boardPos.find(position)#find relative index
        if not self.is_valid(play):#only need to check the first row
            print("This column is full!")
            return change

        # print("im here",play)
        for i in range(self.boardsize_height-1,-1,-1):
            # print(i)
            if self.board[i,play]==0:
                # print("yes")
                
                self.board[i,play] = self.convertPieceInt(player)
                #check end game
                player_int = self.board[i,play]
                end = self.check_end_game(player_int)
                if end:
                    self.winner = self.currentPlayer
                    self.end_game = True
                    print('Game Over.')
                    print('winner is:', self.winner)
                change = True
                break
        return change
            
                

    def changePlayer(self,change):
        if change is True:
            # print("test123")
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
           score += 200
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


    # citation:
    # https://www.youtube.com/watch?v=MMLtza3CZFM&feature=youtu.be
    # modified base on this video.
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
        ## Score negative sloped diagonal
        for r in range(self.boardsize_height-3):
            for c in range(self.boardsize_length-3):
                window = [board[r+3-i][c+i] for i in range(self.window)]
                score += self.evaluate_window(window, player_int)

        return score


    def is_terminal(self):
        # 1 is black and 2 is white
        return self.check_end_game(1) or self.check_end_game(2)

    # Untested minimax agent
    # citation:
    # https://en.wikipedia.org/wiki/Minimax#Pseudocode
    # Modified base on wikipedia minimax pseudocode
    def minimax(self, board, depth, maximizingPlayer):
        legalPositions = self.legalMoves()
        is_end = self.is_terminal()
        if depth == 0 or is_end:
            if is_end:
                if self.check_end_game(2):
                    return (None, 999999999)
                elif self.check_end_game(1):
                    return (None, -999999999)
                else:
                    return (None, 0)
            else:
                return (None, self.scoring(2, board))

        if maximizingPlayer:
            value = -math.inf
            column = random.choice(legalPositions)
            for col in legalPositions:
                row = self.get_row_col(col)
                copyBoard = board.copy()
                self.dropPlay(copyBoard, row, col, 2)
                temp, update_score = self.minimax(copyBoard, depth - 1, False)
                if update_score > value:
                    value = update_score
                    column = col
            return column, value
        else:
            value = math.inf
            column = random.choice(legalPositions)
            for col in legalPositions:
                row = self.get_row_col(col)
                copyBoard = board.copy()
                self.dropPlay(copyBoard, row, col, 1)
                temp, update_score = self.minimax(copyBoard, depth - 1, True)
                if update_score < value:
                    value = update_score
                    column = col
            return column, value
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

    # Best move agent
    def simulate(self):
        best_score = 0

        legalMoves = self.legalMoves()
        best_col = random.choice(legalMoves)
        for col in legalMoves:
            row = self.get_row_col(col)
            temp_board = self.board.copy()
            temp_board[row,col] = self.AI
            score = self.scoring(self.AI,temp_board)
            if score > best_score:
                best_score = score
                best_col = col
        return best_col
    




def main():
    boardList = ["    a b c d e f g", "  -----------------", "6 | 0 0 0 0 0 0 0 | 6", "5 | 0 0 0 0 0 0 0 | 5", "4 | 0 0 0 0 0 0 0 | 4", "3 | 0 0 0 0 0 0 0 | 3", "2 | 0 0 0 0 0 0 0 | 2", "1 | 0 0 0 0 0 0 0 | 1", "  -----------------", "    a b c d e f g"]
    connect4 = connect4Board()
    connect4.drawBoard()
    for i in boardList:
        print(i)
    player = input('Select your player:(b/w/pvp/aivsai/aivsrand) PS.BLACK ALWAYS GO FIRST   ').lower()
    
    end_game = connect4.setStartingPlayer(player)
    print('')
    print("You Choose Player {} .".format(connect4.currentPlayer))

    while not end_game:
        
        print("Player Black is 1, Player White is 2 and empty spot is 0.")
        
        
        if connect4.start == connect4.black:
            if connect4.currentPlayer == connect4.black and not connect4.end_game:
                position = input("Where to play black? (enter 'a - g' to play, 'help' for help, 'exit' to exit.) \n").lower()
                if position == 'help':
                    for i in boardList:
                        print(i)
                    print("enter a letter from a to g to pick the column you want to play. \n")
                elif position == 'exit':
                    end_game = True

                    
                change = connect4.play(position)
                connect4.changePlayer(change)
                connect4.printBoard()
                print('')
                if connect4.end_game:
                    end_game = True

                elif connect4.AI == 2  and not connect4.end_game:
                    if connect4.currentPlayer == connect4.white:
                        boardPos = 'abcdefg'
                        playPos = connect4.simulate()
                        play_ch = boardPos[playPos]

                        change = connect4.play(play_ch)
                        connect4.changePlayer(change)
                        connect4.printBoard()
                        if connect4.end_game:
                            end_game = True

        elif connect4.start == connect4.white:

            
            if connect4.AI == 1 and not connect4.end_game:
                
                
                
                boardPos = 'abcdefg'
                playPos = connect4.simulate()
                play_ch = boardPos[playPos]
                connect4.currentPlayer = connect4.black

                change = connect4.play(play_ch)
                connect4.changePlayer(change)
                connect4.printBoard()
                if connect4.end_game:
                    end_game = True

                elif connect4.currentPlayer == connect4.white and not connect4.end_game:
                    position = input("Where to play white? (enter 'a - g' to play, 'help' for help, 'exit' to exit.) \n").lower()
                    if position == 'help':
                        for i in boardList:
                            print(i)
                        print("enter a letter from a to g to pick the column you want to play. \n")
                    elif position == 'exit':
                        end_game = True
                    change = connect4.play(position)
                    connect4.changePlayer(change)
                    connect4.printBoard()
                    print('')
                    if connect4.end_game:
                        end_game = True

        elif player == 'pvp':
            if not connect4.end_game:
                print("Where to play black? (enter 'a - g' to play, 'help' for help, 'exit' to exit.) \n")
                
                player_b = input('black plays: \n').lower()
                change = connect4.play(player_b)
                connect4.changePlayer(change)
                connect4.printBoard()
                print('')
                if connect4.end_game:
                    end_game = True
                if not connect4.end_game:
                    player_w = input('white plays: \n').lower()
                    change = connect4.play(player_w)
                    connect4.changePlayer(change)
                    connect4.printBoard()
                    print('')
                    if connect4.end_game:
                        end_game = True

        elif player == 'aivsai':
            if connect4.currentPlayer == connect4.black and not connect4.end_game:
                boardPos = 'abcdefg'
                connect4.AI = 1
                playPos = connect4.simulate()
                play_ch = boardPos[playPos]

                change = connect4.play(play_ch)
                connect4.changePlayer(change)
                connect4.printBoard()
                if connect4.end_game:
                    end_game = True
                if connect4.currentPlayer == connect4.white and not connect4.end_game:
                    boardPos = 'abcdefg'
                    connect4.AI = 2
                    playPos = connect4.simulate()
                    play_ch = boardPos[playPos]

                    change = connect4.play(play_ch)
                    connect4.changePlayer(change)
                    connect4.printBoard()
                    
                    if connect4.end_game:
                        end_game = True
        elif player == 'aivsrand':
            if not connect4.end_game:
                boardPos = 'abcdefg'
                connect4.AI = 1
                playPos = connect4.simulate()
                play_ch = boardPos[playPos]

                change = connect4.play(play_ch)
                connect4.changePlayer(change)
                connect4.printBoard()
                if connect4.end_game:
                    end_game = True
                if not connect4.end_game:
                    boardPos = 'abcdefg'
                    playpos = random.choice(boardPos)

                    change = connect4.play(playpos)
                    connect4.changePlayer(change)
                    connect4.printBoard()
                    
                    if connect4.end_game:
                        end_game = True


                


            

            
            
                
                

                

            
                
                
            

main()




# board = connect4Board()

# print(board.drawBoard())
# board.setStartingPlayer()
# print(board.currentPlayer)

# while not board.end_game:#if not over
#     position = input("Where to play? \n")
#     change = board.play(position)
#     print("change is ",change)

#     board.changePlayer(change)
#     board.printBoard()

#     if board.currentPlayer == board.white and not board.end_game:
#         boardPos = 'abcdefg'
#         #playpos = random.choice(boardPos)
#         playpos = board.simulate()

#         play_ch = boardPos[playpos]

#         change = board.play(play_ch)
#         print("change is ",change)

#         board.changePlayer(change)
#         board.printBoard()



