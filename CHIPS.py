from argparse import ArgumentParser
from blessed import Terminal
import sys
import random
from time import sleep

TERM = Terminal()

PCOLOR = TERM.red1       
NCOLOR = TERM.cyan1

SLOT = "{:>0}"
TEMPLATE = f"""{TERM.home+TERM.clear}
<<<<<<< HEAD
<SP>{PCOLOR}<NAME>  {SLOT}  {SLOT}  {SLOT}  {SLOT}  {SLOT}  {SLOT}  {SLOT}  {SLOT}  {SLOT}  {SLOT}
<SP>{NCOLOR}------------------------------------
{PNAME}       a  b  c  d  e  f  g  h  i  j {TERM.normal}"""
=======
<SP>{NCOLOR}<NAME>:{PCOLOR}  {SLOT}  {SLOT}  {SLOT}  {SLOT}  {SLOT}  {SLOT}  {SLOT}  {SLOT}  {SLOT}  {SLOT}  {SLOT}
{TERM.normal}"""
>>>>>>> 053cfd1716b89032fb6aa549e1eb770a5cbd0781

PAUSE = 0.2

NUM0 = "abcdefghij"
NUM1 = [10]

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
<<<<<<< HEAD
    def __init__(self, player, chip0, chip1):
=======
    
    def __init__(self, player, chip0 = One(Get_Move), chip1 = Two(Get_Move)):
>>>>>>> 053cfd1716b89032fb6aa549e1eb770a5cbd0781
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
        else:
            print("Your chip has already been chosen pick again")
            
        if self.chip1 in self.board:
            self.board[self.chip1] = 0
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
        print("hi")
        """while self.game_over is False:
            self.play_round()
            print(self.current_board())
        if self.game_over is True:
            print(f"{self.player}, you win! Your final score is 0.")"""
            
    def playay(self):        
        with TERM.fullscreen():
<<<<<<< HEAD
                self.play()
                
=======
            while True:
                try:
                    self.play_round()
                except SystemExit:
                    print("Thanks for playing!")
                    sleep(PAUSE*3)
                    raise
>>>>>>> 053cfd1716b89032fb6aa549e1eb770a5cbd0781
            
def main(player):
    roll = Dice
    roll.rolldice
    roll.addroll
    a = Get_Move
    b = One(Get_Move)
    c = Two(Get_Move)
    game = Chips(a, b.turn, c.turn)
    game.playay()
        
     
 
def parse_args(arglist):
    parser = ArgumentParser()   
    parser.add_argument("player", nargs="*", help="player names")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.player)

