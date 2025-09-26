"""This module defines the Rectangle class."""

__author__ = "Lichao Huang"
__version__ = "1.0.0"

from abc import ABC, abstractmethod
from shape.shape import Shape

class Rectangle(Shape):
    """
    Define a rectangle
    
    """
    def __init__(self, color: str, length: int, width: int):
        """

        args:
            color (str): The color of the shape.
            length (int): The length of the length.
            width (int): The length of the width.

        Raises:
            ValueError: color is blank, length is not an int,
                        Width is not an int.

        """
        super().__init__(color)

        if isinstance(length, int):
            self.__length = length
        else:
            raise ValueError("Length must be numeric.")
        

        if isinstance(width, int):
            self.__width = width
        else:
            raise ValueError("Width must be numeric.")
        
    def __str__(self) -> str:
        """
        return a string representation of the information of the shape.

        Return:
            str: The color of the shape, and the length of four sides.

        """
        return (
            super().__str__()
            + f"\nThis rectangle has four sides with lengths of "
            + f"{self.__length}, {self.__width}, {self.__length} and {self.__width} centimeters."
        )


    @property
    def calculate_area(self) -> float:
        """
        area calculator

        Return: Rectangle's area

        """
        area = self.__length * self.__width
        return area
    
    @property
    def calculate_perimeter(self) -> float:
        """
        perimeter calculator

        Return: Rectangle's perimeter

        """
        p = self.__length * 2 + self.__width *2
        return p