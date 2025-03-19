# Polymorphism:
# Polymorphism in object-oriented programming refers to the ability of different objects
# to respond to the same method or function call in different ways. In Python, polymorphism
# is achieved through method overriding, where subclasses can provide their own
# implementations of methods defined in the superclass.

import math

class Shape:
    def area(self):
        """
        Calculate and return the area of the shape.
        
        Notes:
        - This method should be overridden by subclasses to provide
          specific implementations for calculating the area of different shapes.
          
        Returns:
        - float: The area of the shape.
        """
        raise NotImplementedError("Subclasses must override the area() method.")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    """

    To do: Write an area() method for the Circle class to calculate and return the area of the circle.

    Instructions:
    - Implement the area calculation for the circle using the provided formula.
    - Calculate the area of the circle using the formula: Area = π * r^2, where r is the radius.
    
    Returns:
    - float: The area of the circle.
    
    """
    # Write your code here

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    """
    To do: Write an area() method for the Rectangle class to calculate and return the area of the rectangle.

    Instructions:
    - Implement the area calculation for the rectangle using the provided formula.
    - Calculate the area of the rectangle using the formula: Area = width * height, where width and height are the dimensions of the rectangle.
    
    Returns:
    - float: The area of the rectangle.
    """
    # Write you code here
