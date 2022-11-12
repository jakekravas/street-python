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
    
    def at_height(self, height):
        """
            Returns string of design of park at specific height
        """

        # if height is 0 or 1, return trunk of tree
        # with equal amount of whitespace on both sides
        if height == 0 or height == 1:
            whitespace_amount = int((self._width - 1) / 2)
            side_whitespace = ' ' * whitespace_amount
            return side_whitespace + '|' + side_whitespace

        # if height is 2, return 5 characters of self._foliage
        # with equal amount of whitespace on both sides
        elif height == 2:
            whitespace_amount = int((self._width - 5) / 2)
            side_whitespace = ' ' * whitespace_amount
            return side_whitespace + (self._foliage * 5) + side_whitespace

        # if height is 3, return 3 characters of self._foliage
        # with equal amount of whitespace on both sides
        elif height == 3:
            whitespace_amount = int((self._width - 3) / 2)
            side_whitespace = ' ' * whitespace_amount
            return side_whitespace + (self._foliage * 3) + side_whitespace

        # if height is 4, return 1 character of self._foliage
        # with equal amount of whitespace on both sides
        elif height == 4:
            whitespace_amount = int((self._width - 1) / 2)
            side_whitespace = ' ' * whitespace_amount
            return side_whitespace + self._foliage + side_whitespace

        # if height > 4, return whitespace of length self._width
        return ' ' * self._width


class Building:
    """
        Holds data of buildings
    """
    def __init__(self, width, height, brick):
        self._width = width
        self._height = height
        self._brick = brick

    def at_height(self, height):
        """
            Returns string of design of building at specific height
        """
        if height <= self._height:
            return self._brick * self._width

        return ' ' * self._width


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

    def at_height(self, height):
        """
            Returns string of design of lot at specific height
        """
        if height == 0:
            trash = self._trash
            # string of self._trash added onto itself
            # until it's equal to length of self._width
            trash_display_str = self.get_trash_str(trash)[:self._width]
            return trash_display_str

        return ' ' * self._width
    
    def remove_trash_underscores(self, trash):
        """
            Returns self._trash with underscores replaced with spaces
        """

        if len(trash) == 0:
            return trash

        if trash[0] == '_':
            return ' ' + self.remove_trash_underscores(trash[1:])

        return trash[0] + self.remove_trash_underscores(trash[1:])

 
    def get_trash_str(self, trash):
        """
            Adds self._trash to string over and over
            until the length of that string is
            equal to self._width, then returns
            that string
        """

        # if length of trash hasn't
        # met or exceeded width, concatenate self._trash
        # to it and call function recursively
        if len(trash) < self._width:
            trash += self._trash
            return self.get_trash_str(trash)
        
        return trash


def get_street_elements(street):
    """
        Returns list of Park instances, Lot instances,
        and Buildings instances based on street argument
    """

    if not street:
        return []

    else:

        # list version of street split by space
        street_list = street.split(' ')
        # street not including first element
        rest_of_street = ' '.join(street_list[1:])

        if not street_list[0]:
            return get_street_elements(rest_of_street)

        # width of street element
        width = int(street_list[0].split(',')[0][2:])

        # if street element is a park, add instance
        # of Park class with data of element to
        # list and call function recursively
        if street[0] == 'p':
            foliage = street_list[0].split(',')[1]
            return [Park(width, foliage)] + get_street_elements(rest_of_street)
        
        # if street element is a building, add instance
        # of Building class with data of element to
        # list and call function recursively
        elif street[0] == 'b':
            height = int(street_list[0].split(',')[1]) - 1
            brick = street_list[0][-1]

            return [Building(width, height, brick)] + get_street_elements(rest_of_street)

        # if street element is an empty parking lot,
        # add instance of Park class with data of element
        # to list and call function recursively
        elif street[0] == 'e':
            trash = street_list[0].split(',')[1]
            return [Lot(width, trash)] + get_street_elements(rest_of_street)


def get_street_height(street_elements, street_height):
    """
        Returns height of tallest element on street
    """
    if not street_elements:
        return street_height
    
    # if height of current street element is greater
    # than street_height, set street_height equal to it
    elif street_elements[0]._height > street_height:
        street_height = street_elements[0]._height

    return get_street_height(street_elements[1:], street_height)


def get_street_width(street_elements):
    """
        Returns integer representing
        width (# of columns) of street
    """

    if street_elements == []:
        return 0

    return street_elements[0]._width + get_street_width(street_elements[1:])

def main():

    street = input('Street: ')
    street_elements = get_street_elements(street)
    street_height = get_street_height(street_elements, 0)
    street_width = get_street_width(street_elements)
    
main()
