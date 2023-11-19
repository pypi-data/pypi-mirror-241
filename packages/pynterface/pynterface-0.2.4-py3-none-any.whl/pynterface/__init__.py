"""
A python module for dealing with terminal-based inputs and outputs.
"""

__version__ = "0.2.4"
__author__ = "Vivaan Singhvi"

from .menu import *
from .input import *
from .style import *
from .loading import *
from .printing import *

def welcome():
    print(gradient(centered(
            [
                "", "Welcome to Pynterface!",
                f"Author: {__author__}", "",
                f"Version: {__version__}", ""
            ], margin=2
        ), (0, 150, 0), (0, 0, 150)
    ))
