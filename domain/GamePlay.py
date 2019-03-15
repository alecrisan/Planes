'''
Created on Jan 5, 2018

@author: Ale
'''
from Board import *
import random

class GamePlay:
    def __init__(self):
        self.userBoard = Board()
        self.userHitsBoard = Board()
        self.computerBoard = Board()
        self.computerHitsBoard = Board()

    def moveUser(self, squareMove):
        """
        Makes the user's move
        input: The square where the user made the move 
        output: None
        """
        value = self.checkIfHit(self.computerBoard, squareMove)

        self.userHitsBoard.move(squareMove, value)

    def moveComputer(self):
        """
        Makes the computer's move
        output: None
        """
        validMoves = self.computerHitsBoard.getValidMoves()
        randomMoveIndex = random.randint(0, len(validMoves) - 1)
        computerMove = validMoves[randomMoveIndex]
        value = self.checkIfHit(self.userBoard, computerMove)

        self.computerHitsBoard.move(computerMove, value)

    def checkIfHit(self, drawingBoard, move):
        """
        Check if the move hits a plane or not
        input: The drawing board on which the move is made and the move(square)
        output: 2 if the plane is hit, 3 otherwise
        """
        x = move.get_x()
        y = move.get_y()

        if drawingBoard[x][y] == 1:
            return 2
        return 3
    
    
class ComputerPlanes:
    def __init__(self):
        self.computerPlanes = dict()

        self.computerPlanes[0] = ((3, 3, "down"), (4, 3, "up"))
        self.computerPlanes[1] = ((2, 7, "right"), (4, 2, "up"))
        self.computerPlanes[2] = ((3, 2, "down"), (3, 3, "up"))
        self.computerPlanes[3] = ((5, 1, "left"), (2, 6, "right"))
        self.computerPlanes[4] = ((0, 2, "up"), (7, 5, "down"))

    def getRandomPlanes(self):
        """
        Gets random planes
        output: A plane configuration
        """
        p = random.randint(0, len(self.computerPlanes) - 1)

        return self.computerPlanes[p]