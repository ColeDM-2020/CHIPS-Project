from argparse import ArgumentParser
from blessed import Terminal
import sys
import random
from time import sleep

TERM = Terminal()

PCOLOR = TERM.red1       
NCOLOR = TERM.cyan1

SLOT = "{:>0}"
TEMPLATE = f"""{TERM.home+TERM.clear}
<SP>{NCOLOR}<NAME>:{PCOLOR}  {SLOT}  {SLOT}  {SLOT}  {SLOT}  {SLOT}  {SLOT}  {SLOT}  {SLOT}  {SLOT}  {SLOT}  {SLOT}
{TERM.normal}"""

PAUSE = 0.2

NUM0 = "abcdefghij"
NUM1 = [10]

board = [0,1,2,3,4,5,6,7,8,9,10]


class Get_Move:
    """Class created to manage the moves that a player can make.
    
    Attributes:
        self.dice1 (int): Random value assigned to Dice 1.
        self.dice2 (int): Random value assigned to Dice 2. 
    """
    
    def __init__(self, name):
        """Initializes the name of the player, and the values of dice 1 and
                and dice 2 roll. 

        Args:
            name (str): The name of the player. 
        """
        self.name = name
        self.dice1 = random.randint(1,6)
        self.dice2 = random.randint(1,6)
            
    def turn(self, board):
        raise NotImplementedError
    
    
class One(Get_Move):
    """First sub class of Get_move to manage one chip selection. 

    """
    
    def turn(self):
        """ Organizes how a chip selection will work for the player.  
        """
        print(f"Dice 1 rolled a: {self.dice1} \nDice 2 rolled a: {self.dice2}")
        selection1 = int(input(f"""Please select your first chip. (or enter q to quit):""" ))
        return selection1
            
class Two(Get_Move):
    """Second child class of Get_Move to manage second chip selection. 

    """
    
    def turn(self):
        """Organizes how a chip selection will work for the player.
        """
        selection2 = int(input(f"""Please select a second chip or enter 0. (or enter q to quit):""" ))
        return selection2
        
class Chips:
    """Runs the Chips game. 
    
    Attributes:
        self.dice1 = Randomized roll for dice1.
        self.dice2 = Randomized roll for dice2.
    """
    def __init__(self, player, chip0 = One(Get_Move), chip1 = Two(Get_Move)):
        """Initialized the player, chip0 and chip1. 

        Args:
            player (str): The players name.
            chip0 (_type_, optional): The first chip selection a player makes. 
                    Defaults to One(Get_Move).
            chip1 (_type_, optional): The second chip selection a plauer makes. 
                    Defaults to Two(Get_Move).
        """
        self.names = player
        self.chip0 = chip0
        self.chip1 = chip1
        self.dice1 = random.randint(1,6)
        self.dice2 = random.randint(1,6)
        
        
    def valid_move(self):
        """This method checks whether a player is allowed to play from a 
                particular chip.
        """
        
        value = self.chip0 + self.chip1
        dices = self.dice1 + self.dice2
        
        if value != dices:
            raise ValueError("Please pick chip(s) that add up to the sum of your roll")
    ##dont know if should be printed or returned####   
    
    def check_chips(self):
        """Checks to see if a chip selection is not in the board and raises a 
                value error.

        Raises:
            ValueError: Will prompt the user that they chip they selected has 
                    already been taken out of the board and end the game.
        """
        if self.chip0 or self.chip1 not in board:
            raise ValueError("The chip you chose has already been taken out of your board")
    
    def play_round(self):
        """Regulates checking if a chip selected is in the board. 
        """
        #self.current_board()
        if self.chip0 in board:
            board[self.chip0] = 0
            print(board)
        else:
            print("Your chip has already been chosen pick again")
            
        if self.chip1 in board:
            board[self.chip1] = 0
            print(board)
        else:
            print("Your chip has already been chosen pick again")

    def game_over(self):
        """Determine whether a round is over"""
        if sum(board[0:11]) > 10:
            print(f"Your score is greater than 10, you lose.")
        else:
            print(f"Your score is less than 10, you win.")     
    
    def score(self):
        """Calculate player's score"""
        print(f"Your final score is {sum(board[0:11])}")   
    
    def current_board(self, pause=PAUSE):
        """Displays the board in the terminal and pauses momentarily.
         
         """
        template = (TEMPLATE
                    .replace("<NAME>", self.names)
                    .replace("<SP>", " "*len(self.names[1])))
        print(template.format(*(board[0::-1]+board[1:])))
        sleep(pause)
        
    def play(self):
        """ Calls the board, play round and the current board function. 
        """
        board
        self.play_round()
        self.current_board()
        
        """if self.game_over is False:
            self.play_round()
            print(self.current_board())
        if self.game_over is True:
            print(f"{self.player}, you win! Your final score is 0.")"""
    
               
            
def main(player):
    """The main function which allows our program to run. 

    Args:
        player (str): The players name.
    """
    x = 0
    while x != 5:
        b = One(Get_Move)
        c = Two(Get_Move)
        game = Chips(str(player), b.turn(), c.turn())
        game.play()
        x += 1  
    game.score()
    game.game_over()
 

def parse_args(arglist):
    parser = ArgumentParser()   
    parser.add_argument("player", nargs="*", help="player names")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.player)

