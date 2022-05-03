#Setting Board as a Global Variable
from argparse import ArgumentParser
from sre_parse import State
import sys
import random
import re

class Dice:
    
    def rolldice(self):
        """"Rolls the two dice. 
    
        Args: 
            dice1(int): The number that is rolled on dice 1 that is 1-6.
            dice2(int): The number that is rolled on dice 2 that is 1-6.
            
        Returns: 
            int: The number rolled on the dice. 
    
        Side effect:
            Prints out the numbers rolled on the dice to the terminal. 
        """
        self.dice1 = random.randint(1,6)
        self.dice2 = random.randint(1,6)
    
        dice = print(f"Dice 1 rolled a: {self.dice1} \n Dice 2 rolled a: {self.dice2}") 
        return dice
    
    def addroll(self):
        """Adding the two dice together to return to the user.
        
        Returns:
            int: The sum of the two dice. 
        
        """
        
        result = (self.dice1 + self.dice2)
        return result


def get_move1(game, player):
    """Asks the player what chips they want to choose or if they want to quit 
            the game.
    
    Args:
        player (str): The player playing the game. 
    
    """
    
    while True:
        print()
        selection = (input(f"{game.names[player]}, select 1 chip that you would" 
                            "like to choose (or enter q to quit): ")
                    .lower()
                    .strip())
        
        if selection == "q":
            sys.exit(0)
        if type(selection) == int :
            return selection

class GameState:
    """ Provides current information on the board when a number is taken out."""
    def __init__(self, selection1, selection2, score, num):
        """Set attributes of the GameState class.
        
        """
        def num_or_dot(num, mask):
            if num in selection1 or selection2:
                return mask
            else:
                return num             
        self.board = " ".join(num_or_dot(c, "\u2022") for c in num)
        self.expr = ("^"
                     + "".join(num_or_dot(c, ".", re.escape) for c in num)
                     + "$")
        self.selection1 = selection1
        self.selection2 = selection2
        self.left = set("123456789101112") - (self.selection1 + self.selection2)
        ##^^ does not workk, need to fix
        self.score = score.copy()
        
    def __str__(self):
        result = [self.board, 
                  f"{self.selection1} and {self.selection2}, both chips have been removed from the board."]
        for name, score in self.score.items():
            msg = f"{name} has made {score} of {self.max_score} bad guesses"
            result.append(msg)
        #why did u add this, do they even have the option to make bad guessess???
        return "\n".join(result)
    
    def match(self, s):
        return bool(re.search(self.expr, s.strip()))

class Chips:
    """check if the dice value matches the values of get_move"""
    def __init__(self, player, func = get_move1):
        self.names = player
        self.func = func
        self.board = []
        self.number = []
        
    def valid_move(self, value):
        """This method checks whether a player is allowed to play from a 
                particular chip.
        
        Args: 
            value (int): The sum of the player's selection
            
        Raises:
            Raises a ValueError if chips that do not add up to the players 
                roll is selected. 
        """
        roll = Dice()
        
        if value != roll.addroll():
            raise ValueError("Please pick chip(s) that add up to the sum of your roll")
    def state(self):
        return GameState(self.func, self.score, self.number)   
    
    def play_round(self, player):
        """This method manages one round of game play. it takes rolls the dice, takes the input, removes the chips"""   
        state = self.state()
        while True:
           pass 
    
    def game_over():
        """Determine whether a round is over"""
        pass
    def score():
        """Calculate the player's score"""
        pass
    def outcome(self):
        if self.board == None:
            return f"Win"
        else:
            return None
        
    def play(self):
        """Manage game play
        Ask if they want to play again and call play_again()"""
        print(self.state().board)
        outcome = self.outcome()
        if outcome == "win":
            print(f"Your score for the round was {self.score()}")
        else:
            print(f"The game is not over.")
    
def parse_args(arg):
    parser = ArgumentParser()
    parser.add_argument("name", help="the first player's name")
    return parser.parse_args(arg)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    game = Chips(args.name)
    game.play()
    
