import math

class Shape:
    """
    A base class to represent a geometric shape.

    Methods:
    --------
    area():
        Abstract method that must be implemented by subclasses to calculate the area of the shape.
    """
    def area(self):
        """
        Abstract method for calculating the area of the shape.

        Raises:
        -------
        NotImplementedError
            If the method is not implemented in a subclass.
        """
        raise NotImplementedError("Subclasses need to overwrite the area method")


class Rectangle(Shape):
    """
    A class to represent a rectangle, inheriting from the Shape class.

    Attributes:
    -----------
    length : float
        The length of the rectangle.
    width : float
        The width of the rectangle.
    """

    def __init__(self, length: str, width: str):
        """
        Initializes a new Rectangle instance.

        Parameters:
        -----------
        length : float
            The length of the rectangle.
        width : float
            The width of the rectangle.
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
        --------
        float
            The area of the rectangle, calculated as length * width.
        """
        return self.length * self.width


class Circle(Shape):
    """
    A class to represent a circle, inheriting from the Shape class.

    Attributes:
    -----------
    radius : float
        The radius of the circle.
    """

    def __init__(self, radius: float):
        """
        Initializes a new Circle instance.

        Parameters:
        -----------
        radius : float
            The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculates the area of the circle.

        Returns:
        --------
        float
            The area of the circle, calculated as π * radius^2.
        """
        return math.pi * self.radius ** 2
