from argparse import ArgumentParser
from blessed import Terminal
import sys
import random
import re
from time import sleep

from parso import ParserSyntaxError

TERM = Terminal()

PCOLOR = TERM.red2       
NCOLOR = TERM.cyan2
PNAME = TERM.green3

SLOT = "{:>0}"
TEMPLATE = f"""{TERM.home+TERM.clear}\
<SP>{PCOLOR}<NAME>  {SLOT}  {SLOT}  {SLOT}  {SLOT}  {SLOT}  {SLOT}  {SLOT}  {SLOT}  {SLOT}  {SLOT}
<SP>{NCOLOR}------------------------------------
{PNAME}       a  b  c  d  e  f  g  h  i  j {TERM.normal}"""

PAUSE = 0.2

NUM0 = "abcdefghij"
NUM1 = [9]

class Dice:
    def __init__(self, dice1 = random.randint(1,6), dice2 = random.randint(1,6)):
        self.dice1 = dice1
        self.dice2 = dice2
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
    
        dice = print(f"Dice 1 rolled a: {self.dice1} \nDice 2 rolled a: {self.dice2}") 
        return dice
    
    def addroll(self):
        """Adding the two dice together to return to the user.
        
        
        Returns:
            int : The sum of the two dice rolls. 
        """
        
        
        result = (self.dice1 + self.dice2)
        return result

class Get_Move:
    def __init__(self, name):
        self.name = name
    
    def turn(self, board):
        """Take a turn.
        
        Args:
            state (GameState): a snapshot of the current state of the game.
        
        Returns:
            str: the player's guess (a letter or a word).
        """
        raise NotImplementedError
class One(Get_Move):
    def turn(self, c = Dice()):
        print(c.rolldice())
        selection1 = ((input(f"""{self.name}, please select your first chip. (or enter q to quit):""" ))
                    .lower()
                    .strip())
        if selection1 == "q":
            sys.exit(0)
            
class Two(Get_Move):
    def turn(self, c = Dice()):
        print(c.rolldice())
        selection2 = ((input(f"""{self.name}, select a second chip or enter 0. (or enter q to quit):""" ))
                    .lower()
                    .strip())
        if selection2 == "q":
            sys.exit(0)
        
class Chips:
    def __init__(self, player, chip0 = One(Get_Move), chip1 = Two(Get_Move)):
        self.names = player
        self.chip0 = chip0
        self.chip1 = chip1
        self.board = []
        
    def valid_move(self):
        """This method checks whether a player is allowed to play from a particular chip.
        
        Args: value(int): the sum of the player's selection
        """
        roll = Dice()
        value = self.chip0 + self.chip1
        
        if value != roll.addroll:
            raise ValueError("Please pick chip(s) that add up to the sum of your roll")
    ##dont know if should be printed or returned####   
    
    def play_round(self):
        self.board = [0,1,2,3,4,5,6,7,8,9,10]
        self.current_board()
        if self.chip0 in self.board:
            self.board[self.chip0] = 0
            return
        else:
            print("Your chip has already been chosen pick again")
        if self.chip1 in self.board:
            self.board[self.chip1] = 0
            return
        else:
            print("Your chip has already been chosen pick again")

    def game_over(self):
        """Determine whether a round is over"""
        return sum(self.board[0:10]) == 0     
    
    def score(self):
        """Calculate player's score"""
        return sum(self.board[0:10])    
    
    def current_board(self, pause=PAUSE):
        """Displays the board in the terminal and pauses momentarily.
         
         """
        template = (TEMPLATE
                    .replace("<NAME>", self.names)
                    .replace("<SP>", " "*len(self.names[1])))
        print(template.format(*(self.board[0::-1]+self.board[1:])))
        sleep(pause)
        
    def play(self):
        while self.game_over == False:
            self.play_round()
            print(self.current_board())
        if self.game_over == True:
            print(f"{self.player}, you win! Your final score is 0.")
            
    def playay(self):        
        with TERM.fullscreen():
            while True:
                try:
                    self.play()
                except SystemExit:
                    print("Thanks for playing!")
                    sleep(PAUSE*3)
                    raise
            
def main(player, chip0, chip1):
    pass
     
 
def parse_args(arglist):
    parser = ArgumentParser()   
    parser.add_argument("player", nargs="*", help="player names")
    parser.add_argument("chip0", nargs="*", help="player names")
    parser.add_argument("chip1", nargs="*", help="player names")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.player, args.chip0, args.chip1)

