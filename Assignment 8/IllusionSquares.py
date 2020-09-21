import turtle

if __name__ == '__main__':

    '''
    A sequential program that creates the "dot illusion" based on user input. 
    
    Inputs:
    squareColor: String
    lineColor: String
    dotColor: String
    imageSize: int
    squareSize: int
    lineWidth: int
    '''

    # Variables
    squareColor = input("Please enter the desired square color(f.ex. white, black, red, blue): ")
    lineColor = input("Please enter the desired line color(f.ex. grey, black, red, blue): ")
    dotColor = input("Please enter the desired dot color(f.ex. black, white, red, blue): ")
    imageSize = int(input("Please enter the desired image size(f.ex. 100, 200, 800): "))
    squareSize = int(input("Please enter the desired square size(f.ex. 20, 50, 100): "))
    lineWidth = int(input("Please enter the desired line size(f.ex. 10, 20, 50): "))

    '''Turtle setup'''
    turtle.setup(imageSize, imageSize)  # creates the window for turtle
    frank = turtle.Turtle()  # Our turtle will be named Frank!
    frank.speed(0)
    frank.screen.bgcolor(squareColor)  # The squares are simply just the background color

    '''In these two loops, the lines are drawn, first in the X-axis, and then in the y-axis'''
    frank.color(lineColor)
    for x in range(0, int((imageSize/ squareSize) + 0.5)):
        frank.penup()
        frank.goto((-imageSize / 2) + (lineWidth/2) + squareSize + (x * squareSize), (-imageSize / 2))
        frank.pendown()
        frank.width(lineWidth)
        frank.goto((-imageSize / 2) + (lineWidth/2) + squareSize + (x * squareSize), (imageSize / 2))
        frank.width(1)

    for y in range(0, int((imageSize/ squareSize) + 0.5)):
        frank.penup()
        frank.goto((-imageSize / 2), (-imageSize / 2) + squareSize + (lineWidth/2) + (y * squareSize))
        frank.pendown()
        frank.width(lineWidth)
        frank.goto((imageSize / 2), (-imageSize / 2) + squareSize + (lineWidth/2) + (y * squareSize))
        frank.width(1)

    '''In the below double loop, we create the dots, they are simply circles with a radius of lineWidth / 2'''
    frank.color(dotColor)
    frank.fillcolor(dotColor)
    for x in range(0, int((imageSize/ squareSize) + 0.5)):
        for y in range(0, int((imageSize/ squareSize) + 0.5)):
            frank.penup()
            frank.goto((-imageSize / 2) + squareSize + (lineWidth/2) + (x * squareSize), (-imageSize / 2) + squareSize + (lineWidth/2) + (y * squareSize) - (lineWidth / 2))
            frank.pendown()
            frank.begin_fill()
            frank.circle(lineWidth/2)
            frank.end_fill()

    turtle.done()  # Prevents the screen from disappearing when drawing is complete
