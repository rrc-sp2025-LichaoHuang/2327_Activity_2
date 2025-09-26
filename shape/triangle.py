"""This module defines the Triangle class."""

__author__ = "Lichao Huang"
__version__ = "1.0.0"

from abc import ABC, abstractmethod
from shape.shape import Shape

class Triangle(Shape):
    """
    Define a triangle

    """
    def __init__(self, color: str,side_1: int, side_2: int, side_3: int):
        """
        args:
            color (str): The color of the shape.
            side_1 (int): side 1 length
            side_2 (int): side 2 length
            side_3 (int): side 3 length

        Raises:
            ValueError: color is blank, side_1 is not an int,
                        side_2 is not an int, side_3 is not an int

        """
        super().__init__(color)

        if isinstance(side_1, int):
            self.__side_1 = side_1
        else:
            raise ValueError("Side 1 must be numeric.")
        

        if isinstance(side_2, int):
            self.__side_2 = side_2
        else:
            raise ValueError("Side 2 must be numeric.")
        

        if isinstance(side_3, int):
            self.__side_3 = side_3
        else:
            raise ValueError("Side 3 must be numeric.")
        
        if ((self.__side_1 + self.__side_2 > self.__side_3) and
            (self.__side_1 + self.__side_3 > self.__side_2) and
            (self.__side_2 + self.__side_3 > self.__side_1)):
            pass
        else:
            raise ValueError("The sides do not satisfy the Triangle Inequality Theorem.")

    def __str__(self) -> str:
        """
        return a string representation of the information of the shape.

        Return:
            str: The color of the triangle, and the length of three sides. 

        """
        return (
            super().__str__()
            + f"\nThis triangle has three sides with lengths of "
            + f"{self.__side_1}, {self.__side_2} and {self.__side_3} centimeters."
        )
    
    @property
    def calculate_area(self) -> float:
        """
        area calculator

        Return: Triangle's area

        """
        sp = (self.__side_1 + self.__side_2 + self.__side_3) / 2
        area = (sp * (sp - self.__side_1) * (sp - self.__side_2) * (sp - self.__side_3)) ** 0.5
        return area
    
    @property
    def calculate_perimeter(self) -> float:
        """
        perimeter calculator

        Return: Triangle's perimeter

        """
        p = self.__side_1 + self.__side_2 + self.__side_3
        return p
