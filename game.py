# Trial gameboard
#||====================================================================||
#||        ##        ##        ##        ##        ##        ##        ||                                        
#||        ##        ##        ##        ##        ##        ##        ||                                                  
#||        ##        ##        ##        ##        ##        ##        ||                                                  
#|| ====== ## ====== ## ====== ## ====== ## ====== ## ====== ## ====== ||
#||        ##        ##        ##        ##        ##        ##        ||                                        
#||        ##        ##        ##        ##        ##        ##        ||                                                  
#||        ##        ##        ##        ##        ##        ##        ||                                                  
#|| ====== ## ====== ## ====== ## ====== ## ====== ## ====== ## ====== ||
#||        ##        ##        ##        ##        ##        ##        ||                                        
#||        ##        ##        ##        ##        ##        ##        ||                                                  
#||        ##        ##        ##        ##        ##        ##        ||                                                  
#|| ====== ## ====== ## ====== ## ====== ## ====== ## ====== ## ====== ||
#||        ##        ##        ##        ##        ##        ##        ||                                        
#||        ##        ##        ##        ##        ##        ##        ||                                                  
#||        ##        ##        ##        ##        ##        ##        ||                                                  
#|| ====== ## ====== ## ====== ## ====== ## ====== ## ====== ## ====== ||
#||        ##        ##        ##        ##        ##        ##        ||                                        
#||        ##        ##        ##        ##        ##        ##        ||                                                  
#||        ##        ##        ##        ##        ##        ##        ||                                                  
#|| ====== ## ====== ## ====== ## ====== ## ====== ## ====== ## ====== ||
#||        ##        ##        ##        ##        ##        ##        ||                                        
#||        ##        ##        ##        ##        ##        ##        ||                                                  
#||        ##        ##        ##        ##        ##        ##        ||                                                  
#||====================================================================||

class Game:
  rows = 6
  columns = rows + 1
  col_list = list(range(columns))
  game_board_dict = {}
  start_finish = "||"
  top_bottom = "=" * 8 + "==" * rows

  def __init__(self):
    self.game_board = 

  def start_game(self):

  def new_game_dict(self, col_list):
    for num in col_list:
      game_board_dict[num + 1] = [i * 0 for i in range(rows)]

  def print_game_board(self, game_board_dict):

  def update_game_board_dict(self, game_board_dict):

  def check_win(self, game_board_dict):

  def win(self, winner):
    

#the game function creates a game board, and begins taking turns asking the players which column they would like to place a token 
#calling the input function that calls the update gameboard function and the print gameboard function 
#print gameboard function uses an dictionary that contains one list for every column the key being the column number
#update gameboard function takes in user input and changes the dictionary that is then used when the print function is used
#check for win function uses the game dictionary to test for possible win scenarios if a win is detected, then the win function is called 
#the win function takes in the winners name prints out a winning statement, and then asks the user if they would like to play again
