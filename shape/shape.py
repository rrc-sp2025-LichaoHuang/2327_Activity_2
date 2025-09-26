"""This module defines the Shape class."""

__author__ = "Lichao Huang"
__version__ = "1.0.0"

from abc import ABC, abstractmethod

class Shape(ABC):
    """
    An abstract shape class
    
    """
    def __init__(self, color: str):
        """

        args:
            color (str): The color of the shape.

        Raises:
            ValueError: color is blank.

        """
        if len(color.strip()) > 0:
            self._color = color
        else:
            raise ValueError("Color cannot be blank.")
        
    def __str__(self) -> str:
        """
        return a string representation of the information of the shape.

        Return:
            str: The color of the shape.

        """
        return(f"The shape color is {self._color}.")
    
    @abstractmethod
    def calculate_area(self)-> float:
        """
        Undefined abstract area calculator.

        """
        pass

    
    @abstractmethod
    def calculate_perimeter(self) -> float:
        """
        Undefined abstract perimeter calculator.

        """
        pass