#Setting Board as a Global Variable
from argparse import ArgumentParser
from multiprocessing.sharedctypes import Value
from blessed import Terminal
import sys
from time import sleep
import random
import re

class Dice:
    
    def rolldice(self):
        """"rolls two dice
    
        Args: 
            dice1(int): The number that is rolled on dice 1 that is 1-6.
            dice2(int): The number that is rolled on dice 2 that is 1-6.
    
        Side effect:
            Prints out the numbers rolled on the dice to the terminal. 
        """
        self.dice1 = random.randint(1,6)
        self.dice2 = random.randint(1,6)
    
        dice = print(f"Dice 1 rolled a: {self.dice1} \n Dice 2 rolled a: {self.dice2}") 
        return dice
    
    def addroll(self):
        """adding the two dice together"""
        
        result = self.dice1 + self.dice2
        return result


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
        if type(selection1) == int and type(selection2) == int:
            value = selection1 + selection2
            return value

class GameState:
    def __init__(self):
        """set attributes"""
        def num_or_dot(num, mask):
            if num in board:
                return mask
            return num             
        self.board = " ".join(num_or_dot(c, "\u2022") for c in word)
        self.expr = ("^"
                     + "".join(num_or_dot(c, ".", re.escape) for c in word)
                     + "$")
    def __str__(self):
        result = [self.board]
        return result
    def match(self, s):
        return bool(re.search(self.expr, s.strip()))

class Chips:
    """check if the dice value matches the values of get_move"""
    def __init__(self, player, func = get_move):
        self.names = player
        self.turn_funcs = func
        self.board =[]
        
    def valid_move(self, value):
        """This method checks whether a player is allowed to play from a particular chip.
        
        Args: value(int): the sum of the player's selection
        """
        roll = Dice()
        
        if value != roll.addroll():
            raise ValueError("Please pick chip(s) that add up to the sum of your roll")
        
    def play_round(self):
        """This method manages one round of game play. It initializes the 
      board for the new round, prints the board, manages turns until one player win"""   
        pass
    def game():
        pass
    
    def game_over():
        """Determine whether a round is over"""
        pass
    def score():
        """Calculate player's score"""
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
    
