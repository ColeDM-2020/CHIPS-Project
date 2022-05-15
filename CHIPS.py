from argparse import ArgumentParser
from re import S
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
    
    def __init__(self, name, dice1, dice2):
        """Initializes the name of the player, and the values of dice 1 and
                and dice 2 roll. 

        Args:
            name (str): The name of the player. 
        """
        self.name = name
        self.dice1 = dice1
        self.dice2 = dice2
            
    def turn(self):
        """Asks the player to choose two chips from the board
        """
        
        print(f"Dice 1 rolled a: {self.dice1} \nDice 2 rolled a: {self.dice2}")
        selection1 = int(input(f"""Please select your first and second chip. (or enter q to quit):""" ))
        selection2 = int(input(f"""Please select a second chip or enter 0. (or enter q to quit):""" ))
        boo = [selection1, selection2]
        return boo
    
            
        
class Chips:
    """Runs the Chips game. 
    
    Attributes:
        self.dice1 = Randomized roll for dice1.
        self.dice2 = Randomized roll for dice2.
    """
    def __init__(self, player, chips, dice1, dice2):
        """Initialized the player, chip0 and chip1. 

        Args:
            player (str): The players name.
            chip0 (int, optional): The first chip selection a player makes. 
                    Defaults to One(Get_Move).
            chip1 (int, optional): The second chip selection a plauer makes. 
                    Defaults to Two(Get_Move).
        """
        self.names = player
        self.chips = chips
        self.dice1 = dice1
        self.dice2 = dice2
        
        
        
        
    def valid_move(self):
        """This method checks whether a player is allowed to play a 
                particular chip.
        """
        
        dice = [self.dice1, self.dice2]
        if sum(self.chips) != sum(dice):
            raise ValueError("Please pick chip(s) that add up to the sum of your roll")
       
    
    def check_chips(self):
        """Checks to see if a chip selection is not in the board. 

        Raises:
            ValueError: Prompts the user that they chip they have selected is 
                already taken out of their board.
            ValueError: Prompts the user that they chip they have selected is 
                already taken out of their boar
        """
        if self.chips[0] not in board:
            raise ValueError("The chip you chose has already been taken out of your board")
        elif self.chips[1] not in board:
            raise ValueError("The chip you chose has already been taken out of your board") 
    
    def play_round(self):
        """Regulates checking if a chip selected is in the board. 
        """
        if self.chips[0] in board:
            board[self.chips[0]] = 0
            print(board)
        else:
            print("Your chip has already been chosen pick again")
            
        if self.chips[1] in board:
            board[self.chips[1]] = 0
            print(board)
        else:
            print("Your chip has already been chosen pick again")

    def game_over(self):
        print (f"Your score is greater than 15, you lose") if sum(board[0:11]) > 15 else print("Your score is less than or equal to 15, you win")
    
    ##def game_over(self):
        #"""Determine whether a round is over"""
        #if sum(board[0:11]) > 15:
            #print(f"Your score is greater than 15, you lose.")
        #else:
            #print(f"Your score is less than or equal to 15, you win.")     
    
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
        self.check_chips()
        self.valid_move()
        self.play_round()
        self.current_board()
        
    
               
            
def main(player):
    """The main function which allows our program to run. 

    Args:
        player (str): The players name.
    """
    x = 0
    with open ("instructions.txt", "r", encoding = "utf-8") as f:
        for line in f:
            print(line)
    #print(f"""Game Instructions: \nThe computer will roll two dice for you, then you will choose two chips from the board. \nThe chips on the board range from 1-10.
#The chips you choose must add up to the value of the dice. \nYou cannot choose the same chip multiple times""")
    while x != 5:
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        b = Get_Move(player, dice1, dice2)
        game = Chips(str(player), b.turn(), dice1, dice2)
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

