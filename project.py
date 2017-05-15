import argparse
from enum import Enum


class InType(Enum):
    """Input types for structures to parse."""
    TEXT = 0
    JSON = 1


class Project(object):
    """Object to store and execute the entirety of the project."""
    variables = []
    programs = []


class Program(object):
    """Object to store rungs."""
    rungs = []
    
    def parse(input_string, input_type=InType.TEXT):
        pass


class Rung(object):
    """Object to store the instructions and their order."""
    instructions = []

    def parse(input_string, input_type=InType.TEXT):
        pass


class Variables():
    """Base class for variable classes."""
    pass

if __name__ == "__main__":
    main()
