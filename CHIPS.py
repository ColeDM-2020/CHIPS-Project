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