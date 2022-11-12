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
    """
        Holds data of buildings
    """
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
        # trash = self.remove_trash_underscores(trash)

        self._width = width
        self._trash = trash
        self._height = 0


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


def main():

    street = input('Street: ')
    street_elements = get_street_elements(street)

main()
