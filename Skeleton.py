#Setting Board as a Global Variable
from argparse import ArgumentParser
from blessed import Terminal
import sys
from time import sleep
import random

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


def rolldice(self, dice1, dice2):
    """"rolls two dice
    
    Args: 
        dice1(int): The number that is rolled on dice 1 that is 1-6.
        dice2(int): The number that is rolled on dice 2 that is 1-6.
    
    Side effect:
        Prints out the numbers rolled on the dice to the terminal. 
    """
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    
    dice = print(f"Dice 1 rolled a: {dice1} \n Dice 2 rolled a: {dice2}") 
    return(dice)

def get_move(game, player):
    """asks the player what chips they want to choose"""
    
    while True:
        print()
        selection1 = (input(f"{game.names[player]}, select 1 chip that you would" 
                            "like to choose (or enter q to quit): ")
                     .lower()
                     .strip())
        
        selection2 = (input(f"{game.names[player]}, select 1 chip that you would" 
                            "like to choose or enter '0' to skip this chip." 
                            "(or enter q to quit): ")
                     .lower()
                     .strip())
        if selection1 == "q" or selection2 == "q":
            sys.exit(0)
        
        value = selection1 + selection2
        
        if value ==     
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
    def play():
        """Manage game play
        Ask if they want to play again and call play_again()"""
    def play_again():
        """Ask if they want to play another round"""
        pass
    def print_board(self, pause=PAUSE):
        """Prints the board"""
        template = (TEMPLATE
                .replace("<NAME0>", self.names[0])
                .replace("<NAME1>", self.names[1])
                .replace("<SP>", " "*len(self.names[1])))
        sleep(pause)
        
    def print_winner():
        "Prints the winnner"
        pass
    
def parse_args(arg):
    pass


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    game = Chips(args.name0, args.name1)
    game.play()
    
