#Setting Board as a Global Variable
from argparse import ArgumentParser
from blessed import Terminal
import sys

def rolldice(dice1, dice2):
    """"rolls two dice
    
    Args: 
        dice1(int): The number that is rolled on dice 1 that is 1-6.
        dice2(int): The number that is rolled on dice 2 that is 1-6.
    
    Side effect:
        Prints out the numbers rolled on the dice to the terminal. 
    """
    pass
def get_move(game, player):
    """asks the player what chips they want to choose"""
    pass

class Chips:
    """check if the dice value matches the values of get_move"""
    def __init__():
        pass
    def valid_move():
        """This method checks whether a player is allowed to play from a particular pit.
"""
        pass
    def play_round():
        """This method manages one round of game play. It initializes the 
      board for the new round, prints the board, manages turns until one player win"""   
        pass
    def game():
        pass
    
    def game_over():
        """Determine whether a round is over"""
        pass
    def score():
        """calculate player's score"""
        pass
    
    
#####
# Board Setup
#####

TERM = Terminal()

P0COLOR = TERM.green3
P1COLOR = TERM.red3

SLOT = "{:>2}"
TEMPLATE = f"""{TERM.home+TERM.clear}\
<SP> {P0COLOR} <NAME0> \u2192 {SLOT} {SLOT} {SLOT} {SLOT} {SLOT} {SLOT} {SLOT} {SLOT} {SLOT} {SLOT}
<SP> {P1COLOR} <NAME1> \u2192 {SLOT} {SLOT} {SLOT} {SLOT} {SLOT} {SLOT} {SLOT} {SLOT} {SLOT} {SLOT}
{TERM.normal}"""

PAUSE = 0.2
STORES = [10, 20]


    

    



#Possible if name == main statement    
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args., args., args., args.)
    
## Or this 
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    game = (args.name0, args.name1)
    game.()
    
