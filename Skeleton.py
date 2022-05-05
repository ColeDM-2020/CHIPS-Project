#Setting Board as a Global Variable
from argparse import ArgumentParser
from blessed import Terminal
import sys
import random
import re
from time import sleep

##Board Setup

TERM = Terminal()

PCOLOR = TERM.red1 

SLOT = "{:>0}"
TEMPLATE = f"""{TERM.home+TERM.clear}\
<SP> {PCOLOR} {SLOT} {SLOT} {SLOT} {SLOT} {SLOT} {SLOT} {SLOT} {SLOT} {SLOT} {SLOT} {SLOT}
{PCOLOR} <NAME> a  b  c  d  e  f  g  h  i  j {TERM.normal}"""

PAUSE = 0.2

NUM0 = "abcdefghij"
NUM1 = [9]

class Dice:
    
    def __init__ (self):
        """
        attributes
        
        """

    
    def rolldice(self):
        """"rolls two dice
    
        Args: 
            dice1(int): The number that is rolled on dice 1 that is 1-6.
            dice2(int): The number that is rolled on dice 2 that is 1-6.
            
        Returns:
            str: The string of the two numbers rolled on the dice. 
    
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
            int : The sum of the two dice rolls. 
        
        """
        
        result = (self.dice1 + self.dice2)
        return result


def get_move(game, player):
    """Asks the player what chips they want to choose.
    
    Args:
        player (): The player. 
    
    
 
    list_selections = list_selections
    
    Dice.rolldice
    Dice.addroll
   
    while True:
        print()
        selection = (input(input((f"{game.names[player]}, select chips that you would" 
                                        "like to choose. Please seperate each chip by a space"
                                        "(or enter q to quit):" )))
                    .lower()
                    .strip())
        
        list_selections = list((int,selection().split()))
        
        if selection == "q":
            sys.exit(0)
        for x in list_selections:
            if type(x) == int:
                return x
        
        list = [1,2,3,4,5,6,7,8,9,10]
        try:
            for x in list_selections:
                if x not in list:
                    raise ValueError("Please enter numbers between 1-10.")
        
                if x != int:
                    raise ValueError("Please enter a number.")
        except ValueError as e:
                    print (e) """
        


class Chips:
    """check if the dice value matches the values of get_move"""
    def __init__(self, game, player, func = get_move):
        self.names = player
        self.func = func
        self.board = []
        
    def get_move(self, player):
        """Asks the player what chips they want to choose.
    
    Args:
        player (): The player. 
    
    """
        self.player = player
    
        Dice.rolldice
        Dice.addroll
   

    
        selection = (input(input((f"{[player]}, select chips that you would" 
                                        "like to choose. Please seperate each chip by a space"
                                        "(or enter q to quit):" )))
                    .lower()
                    .strip())
        print(selection)
        print("hi")
        
        self.list_selections = list((int,selection().split()))
        
        if selection == "q":
            sys.exit(0)
        for x in self.list_selections:
            if type(x) == int:
                return x
        
            
                    
    def valid_move(self, value):
        """This method checks whether a player is allowed to play from a particular chip.
        
        Args: value(int): the sum of the player's selection
        """
        roll = Dice()
        
        if value != roll.addroll:
            raise ValueError("Please pick chip(s) that add up to the sum of your roll")
        
        #Make sure they only pick avaiable spots on the board or else raise error 
    
    def game_over(self):
        """Determine whether a round is over"""
        if sum(self.board[0:9]) == 0:
            return f"Your final score was {self.score}."
    
    def score(self):
        """Calculate player's score"""
        return sum(self.board[0:9])
        
    def play(self):
        """Manage game play
        Ask if they want to play again and call play_again()"""

        get_move(self.game, self.names)
       
        self.board = [1,2,3,4,5,6,7,8,9,10]
        self.current_board()
        
        while self.game_over() == True:
                 
            for x in self.list_selections:
                if x in self.board:
<<<<<<< HEAD
                    self.board[x] = 0
                    
            for x in self.board:       
                print (x)
=======
<<<<<<< HEAD
                    self.board.remove(x)
                    
        print (self.current_board)
=======
                    self.board[x] = 0

    def play_round(self):
    
        with TERM.fullscreen():
            while True:
                try:
                    self.play()
                    if not self.play_again():
                        sys.exit(0)
                except SystemExit:
                    print("Thanks for playing!")
                    sleep(PAUSE*3)
                    raise
                
    def play_again():
        
        print()
        while True:
            response = (input("Would you like to play again (y/n)? ")
                        .strip()
                        .lower()[0])
            if response not in "ny":
                print("Please type 'y' or 'n'.")
                continue
            return response == "y"
>>>>>>> 941085f4402094d1d33828d5d9ff72f7319c9593
                          
>>>>>>> b9121b0c401060ef157897087004b428ddb424a8
        
    """def __str__(self):
        result = [self.board, 
                  f"{self.selection1} and {self.selection2}, both chips have been removed from the board."]
        for name, score in self.score.items():
            msg = f"{name} has made {score} of {self.max_score} bad guesses"
            result.append(msg)
        #why did u add this, do they even have the option to make bad guessess???
        return "\n".join(result)
    
    def match(self, s):
        return bool(re.search(self.expr, s.strip()))
        
    print(self.state().board)
        outcome = self.outcome()
        if outcome == "win":
            print(f"Your score for the round was {self.score()}")
        else:
            print(fThe game is not over.)"""
            
    def current_board(self, pause=PAUSE):
        """Displays the board in the terminal and pauses momentarily.
         
         """
        template = (TEMPLATE
                    .replace("<SP>", " "*len(self.names[0]))
                    .replace("<NAME>", self.names[0]))
        print(template.format((self.board[9:])))
        sleep(pause)
    
def parse_args(arg):
    parser = ArgumentParser()
    parser.add_argument("name", help="the first player's name")
    return parser.parse_args(arg)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    game = Chips(args.name)
    game.play()


