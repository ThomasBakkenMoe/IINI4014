''' Circuitous, LLC -
    An Advanced Circle Analytics Company

'''

import math


class Circle(object):               # New-style class
    'An advanced circle analytic toolkit'

    # flyweight design pattern suppresses
    # th instance dictionary

    __slots__ = ['diameter']
    version = '0.6'                # class variable

    def __init__(self, radius):

        # Here, I have chosen to change self.radius to self. diameter, as the code will not run properly if I don't
        self.diameter = 2 * radius        # instance variable

    def area(self):
        'Perform quadrature on a shape of uniform radius'
        p = self.__perimeter()
        r = p / math.pi / 2.0
        return math.pi * r ** 2.0 # The '**' operator can be considered the same as 'power'

    'This method of setting radius as a property is similar to getters & setters in Java' \
        'it lets you change the underlying code without breaking your client´s code'
    @property                       # convert dotted access to method calls
    def radius(self):
        'Radius of a circle'
        return self.diameter / 2.0

    def perimeter(self):
        return 2.0 * math.pi * self.radius

    __perimeter = perimeter

    @staticmethod                   # attach functions to classes
    def angle_to_grade(angle):
        'Convert angle in degree to a percentage grade'
        return math.tan(math.radians(angle)) * 100.0

    @classmethod                    # alternative constructor
    def from_bbd(cls, bbd):
        'Construct a circle from a bounding box diagonal'
        radius = bbd / 2.0 / math.sqrt(2.0)
        return cls(radius)


'Tire is a sub-class of circle'
class Tire(Circle):
    'Tires are circles with a corrected perimiter'

    'This is called "extending", since the parent class, Circle, is called.' \
        'if the parent class had not been called in the method, this would be called "Overriding"'

    def perimeter(self):
        'Circumference corrected for the rubber'
        return Circle.perimeter(self) * 1.25
