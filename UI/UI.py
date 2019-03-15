'''
Created on Jan 5, 2018

@author: Ale
'''
from domain.GamePlay import *

class UI:
    def __init__(self):
        self.game = GamePlay()
    
    def start(self):
        
        turn = "user"
        userBoard = self.game.userBoard
        userHitsBoard = self.game.userHitsBoard
        computerBoard = self.game.computerBoard
        computerHitsBoard = self.game.computerHitsBoard
        
        """
        Drawing the planes
        """
        
        self.drawUserPlanes(userBoard)
        self.drawComputerPlanes(computerBoard)
        print(userBoard)
        print(computerBoard)

        letters = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7}
        while True:
            
            if turn == "user": 
                """
                Your turn!
                """ 
                print("What's your move? ")
                x = int(input("x: "))
                y = raw_input("y: ")
                x = x - 1
                y = int(letters.get(y))
                userMove = Square(x, y)

                while userHitsBoard.checkMove(userMove) is False:
                    print("Invalid move or it has already been made. Try again!")
                    x = int(input("x: "))
                    y = raw_input("y: ")
                    x = x - 1
                    y = int(letters.get(y))
                    userMove = Square(x, y)

                self.game.moveUser(userMove)
                print("\n    User hit board\n")
                print(userHitsBoard)
                print("\n The hidden computer board\n")
                print(computerBoard)

                if computerBoard.checkWin(userHitsBoard):
                    print("You won! Congrats")
                    print("\nComputer's board\n")
                    print(computerBoard)

                    return
    
                turn = "computer"
            else:
                """
                Computer's turn
                """
                self.game.moveComputer()
                print("\n  Computer hit board\n")
                print(computerHitsBoard)
                print("\n The hidden user board\n")
                print(userBoard)

                if userBoard.checkWin(computerHitsBoard):
                    print("You lost! The computer won")
                    print("\n   User's board\n")
                    print(userBoard)

                    return

                turn = "user"
                
    def drawUserPlanes(self, userBoard):
        """
        Asks for input data and draws the user's planes
        input: The user's board
        output: None
        """
        letters = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7}
        print("Coordinates for plane number one?")
        planeOneCabinX = int(raw_input("x: "))
        planeOneCabinY = raw_input("y: ")
        planeOneDirection = raw_input("Direction: ")
        planeOneCabinX -=1
        planeOneCabinY = int(letters.get(planeOneCabinY))
        print("Coordinates for plane number two?")
        planeTwoCabinX = int(raw_input("x: "))
        planeTwoCabinY = raw_input("y: ")
        planeTwoDirection = raw_input("Direction: ")
        planeTwoCabinX -=1
        planeTwoCabinY = int(letters.get(planeTwoCabinY))

        while userBoard.drawPlane(Square(planeOneCabinX, planeOneCabinY), planeOneDirection) is False or \
                userBoard.drawPlane(Square(planeTwoCabinX, planeTwoCabinY), planeTwoDirection) is False:
                print("Please give 2 valid planes!")
                print("Coordinates for plane number one?")
                planeOneCabinX = int(raw_input("x: "))
                planeOneCabinY = raw_input("y: ")
                planeOneDirection = raw_input("Direction: ")
                planeOneCabinX -=1
                planeOneCabinY = int(letters.get(planeOneCabinY))
                print("Coordinates for plane number two?")
                planeTwoCabinX = int(raw_input("x: "))
                planeTwoCabinY = raw_input("y: ")
                planeTwoDirection = raw_input("Direction: ")
                planeTwoCabinX -=1
                planeTwoCabinY = int(letters.get(planeTwoCabinY))

    def drawComputerPlanes(self, computerBoard):
        """
        Draws the computer's planes
        input: the computer's board 
        output: None
        """
        computerPlanes = ComputerPlanes()
        planes = computerPlanes.getRandomPlanes()
        cabinOne = Square(planes[0][0], planes[0][1])
        directionOne = planes[0][2]
        cabinTwo = Square(planes[1][0], planes[1][1])
        directionTwo = planes[1][2]

        computerBoard.drawPlane(cabinOne, directionOne)
        computerBoard.drawPlane(cabinTwo, directionTwo)
                
ui = UI()

ui.start()