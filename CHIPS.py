## This is a new file 
from argparse import ArgumentParser
from blessed import Terminal
import sys
import random
import re
from time import sleep

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