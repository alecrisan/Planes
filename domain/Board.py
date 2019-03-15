'''
Created on Jan 5, 2018

@author: Ale
'''
from Square import *

class Board:
    """
    0 - empty square
    1 - plane square 
    2 - hit a plane (X on the board)
    3 - did not hit a plane (0 on the board)
    """
    def __init__(self):
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0]]
        self.planeCabins = list()
        
    def __getitem__(self, item):
        return self.board[item]
    
    def __str__(self):
        """
        Prints the board
        output: A string representing the board
        """
        board = ""

        board += "   A B C D E F G H\n"
        board += "  -----------------\n"
        for i, line in zip(range(1, 9), self.board):
            board += str(i)
            board += " |"
            for item in line:
                if item == 1:
                    board += "*"
                elif item == 2:
                    board += "X"
                elif item == 3:
                    board += "0"
                else:
                    board += " "
                board += "|"

            board += "\n"
            board += "  -----------------\n"

        return board
    
    def getValidMoves(self):
        """
        Returns a list of squares representing the valid moves
        output: A list
        """
        validMoves = list()
        board = self.board

        for i in range(0, 8):
            for j in range(0, 8):
                if board[i][j] == 0:
                    validMoves.append(Square(i, j))

        return validMoves
    
    def checkMove(self, squareMove):
        """
        Checks if the move can be made
        input: a square
        output: True if it can be made, False otherwise
        """
        x = squareMove.get_x()
        y = squareMove.get_y()

        if x not in range(0, 8) or y not in range(0, 8) or self.board[x][y] != 0:
            return False
        return True
    
    def move(self, squareMove, value):
        """
        Makes a move to a square with a certain value
        input: The square where the move is made and the value of the move
        output: None
        """
        x = squareMove.get_x()
        y = squareMove.get_y()

        self.board[x][y] = value
        
    def checkSquareList(self, squareList):
        """
        Check if the square list can be placed on the board
        input: the list of squares
        output: True if all can be placed, False otherwise
        """
        for square in squareList:
            x = square.get_x()
            y = square.get_y()

            if x not in range(0, 8) or y not in range(0, 8) or self.board[x][y] != 0:
                return False

        return True

    def checkIfPlaneIsValid(self, square, direction):
        """
        Checks if the plane's cabin can be put there
        input: the square and the direction the plane is facing
        output: True and a list of squares if it can be placed, False otherwise
        """
        x = square.get_x()
        y = square.get_y()
        squareList = None

        if direction == "up":
            squareList = [Square(x, y),
                          Square(x + 1, y - 2), Square(x + 1, y - 1), Square(x + 1, y), Square(x + 1, y + 1), Square(x + 1, y + 2),
                          Square(x + 2, y),
                          Square(x + 3, y - 1), Square(x + 3, y), Square(x + 3, y + 1)]
            
        elif direction == "down":
            squareList = [Square(x, y),
                          Square(x - 1, y - 2), Square(x - 1, y - 1), Square(x - 1, y), Square(x - 1, y + 1), Square(x - 1, y + 2),
                          Square(x - 2, y),
                          Square(x - 3, y - 1), Square(x - 3, y), Square(x - 3, y + 1)]
            
        elif direction == "right":
            squareList = [Square(x, y),
                          Square(x - 2, y - 1), Square(x - 1, y - 1), Square(x, y - 1), Square(x + 1, y - 1), Square(x + 2, y - 1),
                          Square(x, y - 2),
                          Square(x - 1, y - 3), Square(x, y - 3), Square(x + 1, y - 3)]
        elif direction == "left":
            squareList = [Square(x, y),
                          Square(x - 2, y + 1), Square(x - 1, y + 1), Square(x, y + 1), Square(x + 1, y + 1), Square(x + 2, y + 1),
                          Square(x, y + 2),
                          Square(x - 1, y + 3), Square(x, y + 3), Square(x + 1, y + 3)]

        if self.checkSquareList(squareList) == True:
            return True, squareList
        return False,

    def drawPlane(self, cabin, direction):
        """
        Draws a plane on the board
        input: The cabin of the plane and the direction the plane is facing
        output: True if the cabin was placed, False otherwise
        """
        returnedTuple = self.checkIfPlaneIsValid(cabin, direction)

        if returnedTuple[0]:
            squareList = returnedTuple[1]

            for square in squareList:
                self.board[square.get_x()][square.get_y()] = 1
            self.planeCabins.append(cabin)

            return True
        return False
    
    def checkWin(self, hitBoard):
        """
        Check if there is a win
        input: the board to which the current one is checked (The draw board compared to the hit board)
        output: True if both planes on the board are dead, False otherwise
        """
        planeOneCabinX = self.planeCabins[0].get_x()
        planeOneCabinY = self.planeCabins[0].get_y()
        planeTwoCabinX = self.planeCabins[1].get_x()
        planeTwoCabinY = self.planeCabins[1].get_y()

        if hitBoard[planeOneCabinX][planeOneCabinY] == 2 and hitBoard[planeTwoCabinX][planeTwoCabinY] == 2:
            return True

        return False
