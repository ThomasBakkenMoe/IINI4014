import random
import turtle

class Dice():
    """
    Dice class for rolling aand drawing a dice
    uses turtle to draw the die,
    and random for giving a random value.
    """

    def __init__(self, xPos, yPos, size, primaryColor = None, secondaryColor = None):

        """
        Dice constructor, sets up drawing enviroment and user set variables to
        get a custom dice.
        Input: x and y position of dice, as well as size and colorts
        """

        self.xPos = xPos
        self.yPos = yPos
        self.size = size
        self.rolledValue = None
        self.spacing = size / 5  # Spacing in-between the dots of the die
        print("" + str(self.spacing))

        # If the primaryColor has not been set, a default color will be used
        if primaryColor is None:
            self.primaryColor = "white"  # Default primaryColor
        else:
            self.primaryColor = primaryColor

        # If the secondaryColor has not been set, a default color will be used
        if secondaryColor is None:
            self.secondaryColor = "black"  # Default primaryColor
        else:
            self.secondaryColor = secondaryColor

        self.penSize = 4

        # Setup drawing environment
        turtle.setup(500, 500)
        self.frank = turtle.Turtle()
        self.frank.speed(0)
        self.frank.pensize(1)
        self.frank.hideturtle()

    def getPosition(self):
        """
        Gets the position of the corner of the die
        Returns: a list (length 2) of x and y position, ie [x,y]
        """
        return [self.xPos, self.yPos]

    def getSize(self):
        """
        Gets the size of the die
        returns: Integer of the size of the dice"""
        return self.size

    def rollDice(self):
        """
        Sets the die value to a random integer between 1-6
        """
        self.rolledValue = random.randrange(1, 7)

    def getRolledValue(self):
        """
        Gets the value of the die
        returns: if dice has been rolled, returns the integer value of the die
        """
        # Only returns the rolledValue if the dice has been rolled
        if self.rolledValue:
            print(self.rolledValue)
            return self.rolledValue

    def setDieColor(self, dieColor, dotColor):
        """
        Sets the color of the die and dots
        """
        self.primaryColor = dieColor
        self.secondaryColor = dotColor

    def drawDice(self):
        """
        Draws the die, as long as it has been rolled.
        Raises an Exception if the die has not been rolled.
        """
        rolled = self.getRolledValue()

        rolled = 5
        if rolled:
            self.__drawDiceEdges()

            # Draw value of rolled dice depending on variable
            if rolled == 1:
                self.__drawOne()

            elif rolled == 2:
                self.__drawTwo()

            elif rolled == 3:
                self.__drawThree()

            elif rolled == 4:
                self.__drawFour()

            elif rolled == 5:
                self.__drawFive()

            elif rolled == 6:
                self.__drawSix()
        else:
            raise Exception("Dice needs to be rolled before it can be drawn (call dice.rollDice())")

    def __drawDiceEdges(self): # Note: Not a fan of the way Python handles "Private" methods

        # private method used to draw the outline of the dice
        self.frank.fillcolor(self.primaryColor)
        self.frank.begin_fill()
        self.frank.penup()
        self.frank.goto(self.getPosition())
        self.frank.pendown()

        for x in range(0, 4):
            self.frank.forward(self.getSize())
            self.frank.right(90)

        self.frank.end_fill()

    def __drawOne(self):
        # Private method used to draw the dice roll 1
        self.frank.pensize(self.penSize)
        self.frank.color(self.secondaryColor)
        self.frank.penup()
        self.frank.goto(self.getPosition()[0] + self.getSize() / 2, self.getPosition()[1] - self.getSize() / 2)
        self.frank.pendown()
        self.frank.dot()



    def __drawTwo(self):
        # Private method used to draw the dice roll 2
        self.frank.pensize(self.penSize)
        self.frank.color(self.secondaryColor)

        self.frank.penup()
        self.frank.goto(self.getPosition()[0] + self.getSize() / 2 - self.spacing, self.getPosition()[1] - self.getSize() / 2)
        self.frank.pendown()
        self.frank.dot()
        self.frank.penup()
        self.frank.forward(self.spacing * 2)
        self.frank.pendown()
        self.frank.dot()


    def __drawThree(self):
        # Private method used to draw the dice roll 3
        self.frank.pensize(self.penSize)
        self.frank.color(self.secondaryColor)

        self.frank.penup()
        self.frank.goto(self.getPosition()[0] + self.getSize() / 2, self.getPosition()[1] - self.getSize() / 2)
        self.frank.pendown()
        self.frank.dot()
        self.frank.penup()
        self.frank.left(90)
        self.frank.forward(self.spacing)
        self.frank.pendown()
        self.frank.dot()
        self.frank.penup()
        self.frank.right(180)
        self.frank.forward(self.spacing * 2)
        self.frank.pendown()
        self.frank.dot()

    def __drawFour(self):
        # Private method used to draw the dice roll 4
        self.frank.pensize(self.penSize)
        self.frank.color(self.secondaryColor)

        self.frank.penup()
        self.frank.goto(self.getPosition()[0] + self.getSize() / 2 - self.spacing, self.getPosition()[1] - self.getSize() / 2 + self.spacing)
        self.frank.dot()
        self.frank.penup()
        self.frank.forward(self.spacing * 2)
        self.frank.pendown()
        self.frank.dot()

        for x in range(0,2):
            self.frank.penup()
            self.frank.right(90)
            self.frank.forward(self.spacing * 2)
            self.frank.pendown()
            self.frank.dot()

    def __drawFive(self):
        # Private method used to draw the dice roll 5
        self.frank.pensize(self.penSize)
        self.frank.color(self.secondaryColor)

        self.frank.penup()
        self.frank.goto(self.getPosition()[0] + self.getSize() / 2, self.getPosition()[1] - self.getSize() / 2)
        self.frank.pendown()
        self.frank.dot()

        self.frank.penup()
        self.frank.forward(self.spacing)
        self.frank.left(90)
        self.frank.forward(self.spacing)
        self.frank.pendown()
        self.frank.dot()

        for x in range(0,3):
            self.frank.penup()
            self.frank.left(90)
            self.frank.forward(self.spacing * 2)
            self.frank.pendown()
            self.frank.dot()

    def __drawSix(self):
        # Private method used to draw the dice roll 6
        self.frank.pensize(self.penSize)
        self.frank.color(self.secondaryColor)

        self.frank.penup()
        self.frank.goto(self.getPosition()[0] + self.getSize() / 2, self.getPosition()[1] - self.getSize() / 2)
        self.frank.forward(self.spacing)
        self.frank.pendown()
        self.frank.dot()

        self.frank.penup()
        self.frank.left(90)
        self.frank.forward(self.spacing)
        self.frank.pendown()
        self.frank.dot()

        self.frank.penup()
        self.frank.right(180)
        self.frank.forward(self.spacing * 2)
        self.frank.pendown()
        self.frank.dot()

        self.frank.penup()
        self.frank.right(90)
        self.frank.forward(self.spacing * 2)
        self.frank.right(90)
        self.frank.pendown()
        self.frank.dot()

        for x in range(0,2):
            self.frank.penup()
            self.frank.forward(self.spacing)
            self.frank.pendown()
            self.frank.dot()

if __name__ == "__main__":

    userSettings = input("Please input the X-position, Y-position, and size of your die (x,y,size): ")
    userSettings = tuple(int(x) for x in userSettings.split(","))

    xPos = userSettings[0]
    yPos = userSettings[1]
    size = userSettings[2]
    dicePrimaryColor = "white"
    diceSecondaryColor = "black"

    # create instance of dice
    dice = Dice(xPos, yPos, size, dicePrimaryColor, diceSecondaryColor)

    # Roll the dice
    dice.rollDice()

    # draw dice
    dice.drawDice()

    # holds the image after finished drawing
    turtle.done()

    '''Beneath is an attempt at having the ability to roll the dice multiple times'''
    # while True:
    #
    #     continueInput = input("Roll again? (y/n): ")
    #
    #     if continueInput == "y":
    #         dice.rollDice()
    #         dice.drawDice()
    #
    #         turtle.done()
    #
    #     if continueInput == "n":
    #         break
    #
