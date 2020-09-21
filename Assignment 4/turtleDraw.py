import turtle
import math

class Point:
    # Helper-class to hold position data.
    # I find this to be more organized rather than saving each point to an array with 2 length

    def __init__(self, x_init, y_init):
        self.x = x_init
        self.y = y_init

def findpoint(radius, point, points):
    # This function finds a point along the circle,
    # it is called for each iteration instead of saving all the points in an array, thus saving memory

    degree = (360.0 / points) * point

    return Point((math.cos(math.radians(degree)))*radius, (math.sin(math.radians(degree))*radius))

def drawVizualisation(frank, radius, points, interval):

    for x in range(points):

            # Sets turtle to the starting location of the line
            frank.penup()
            p1 = findpoint(radius, x, points)
            frank.goto(p1.x, p1.y)

            # Draws the line
            frank.pendown()
            p2 = findpoint(radius, x * interval, points)
            frank.goto(p2.x, p2.y)


if __name__ == '__main__':

    '''Control variables'''
    circleRadius = 300
    points = 200
    interval = 21

    '''Turtle setup'''
    turtle.setup(800, 800)  # creates the window for turtle
    frank = turtle.Turtle()  # Our turtle will be named Frank!
    frank.speed(0)
    frank.pencolor('magenta')  # Changes the pen color to something a little more interesting
    frank.penup()
    frank.sety(-circleRadius)  # Makes sure the the perimeter circle is drawn in the middle of the screen
    frank.pendown()
    frank.circle(circleRadius)

    '''Execution of the drawing'''
    drawVizualisation(frank, circleRadius, points, interval)

    turtle.done()  # Prevents the screen from disappearing when drawing is complete
