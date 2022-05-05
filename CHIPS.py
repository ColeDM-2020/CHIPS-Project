## This is a new file 
from argparse import ArgumentParser
from blessed import Terminal
import sys
import random
import re
from time import sleep

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
    
        dice = print(f"Dice 1 rolled a: {self.dice1} \n Dice 2 rolled a: {self.dice2}") 
        return dice
    
    def addroll(self):
        """Adding the two dice together to return to the user.
        
        
        Returns:
            int : The sum of the two dice rolls. 
        """
        
        
        result = (self.dice1 + self.dice2)
        return result
    
<<<<<<< HEAD
def get_move(player):
    """Asks the player what chips they want to choose.
    
    Args:
        player (): The player. 
    
    """
    c = Dice()
    print(c.rolldice())
    selection1 = ((input(f"""{player}, please select your first chip. (or enter q to quit):""" ))
                .lower()
                .strip())
    selection2 = ((input(f"""{player}, select a second chip or enter 0. (or enter q to quit):""" ))
                .lower()
                .strip())
    if selection1 == "q" or selection2 == "q":
        sys.exit(0)
    
=======
    
    
    
    
    
    
    
def current_board(self, pause=PAUSE):
        """Displays the board in the terminal and pauses momentarily.
         
         """
        template = (TEMPLATE
                    .replace("<NAME>", self.names)
                    .replace("<SP>", " "*len(self.names[1])))
        print(template.format(*(self.board[0::-1]+self.board[1:])))
        sleep(pause)
        
>>>>>>> 95e043118dc3c7ec3162846d05789f498549e856
