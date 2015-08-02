from board import board
from move import move

class MinMax:
    
    def __init__(self, level, token):
        self.level = level
        self.token = token
        
    def move(self, board):
        return move(self.token, 2, 2)