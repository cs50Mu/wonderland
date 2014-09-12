###########
# Reverse #
###########

def reverse_iter(lst):
    """Returns the reverse of the given list.

    >>> reverse_iter([1, 2, 3, 4])
    [4, 3, 2, 1]
    """
    "*** YOUR CODE HERE ***"

def reverse_recursive(lst):
    """Returns the reverse of the given list.

    >>> reverse_recursive([1, 2, 3, 4])
    [4, 3, 2, 1]
    """
    "*** YOUR CODE HERE ***"


#######
# OOP #
#######

class Horse:
    breathes = "air"
    def __init__(self, color):
        self.color = color
        self.cry = "neigh"
    def call(self):
        return self.call

class Seahorse(Horse):
    def __init__(self, color):
        Horse.__init__(self, 'purple')
        self.breathes = "water"
        self.cry = "glub"
    def change_color(self, who):
        who.color, self.color = self.color, who.color


#############
# Iterators #
#############

class SquaresIterator:
    """
    >>> for ps in SquaresIterator(7.3):
    ...     print(ps)
    ...
    1
    4
    9
    16
    25
    36
    49
    """
    def __init__(self, n):
        "*** YOUR CODE HERE ***"

    def __next__(self):
        "*** YOUR CODE HERE ***"

    def __iter__(self):
        "*** YOUR CODE HERE ***"


##############
# Generators #
##############

def char_gen(str):
    """
    >>> for char in char_gen("hello"):
    ...     print(char)
    ...
    h
    e
    l
    l
    o
    """
    "*** YOUR CODE HERE ***"

