#Setting Board as a Global Variable
from argparse import ArgumentParser
from blessed import Terminal
import sys

#####
# Board Setup
#####

TERM = Terminal()

P1COLOR = TERM.green3
P2COLOR = TERM.red3


def rolldice(dice1, dice2): 
    """"
    rolls two dice
    """
    pass

def get_move(game, player):
    """asks the player what chips they want to choose"""
    pass

class Chips:
    """check if the dice value matches the values of get_move
    """
    def __init__(self):
        pass

class Player:
    def __init__(self):
        pass
    
    def turn():
        pass
    
    def valid_move():
        pass
    
class GameState:
    



#Possible if name == main statement    
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args., args., args., args.)
    
## Or this 
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    game = (args.name0, args.name1)
    game.()
    