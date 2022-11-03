"""
    File: street.py
    Author: Jake Kravas
    Purpose: Uses recursion
    to display design of
    street based on
    user-inputted string
"""

class Park:
    """
        Holds data of parks
    """
    def __init__(self, width, foliage):
        self._width = width
        self._foliage = foliage
        self._height = 4

class Building:
    def __init__(self, width, height, brick):
        self._width = width
        self._height = height
        self._brick = brick

class Lot:
    """
        Holds data of parking lots
    """
    def __init__(self, width, trash):

        # replace trash underscores with spaces
        trash = self.remove_trash_underscores(trash)

        self._width = width
        self._trash = trash
        self._height = 0
