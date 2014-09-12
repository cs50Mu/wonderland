from math import sin, cos, atan2, pi

### Demo: Coercion Revisited

def rational_to_complex(r):
    return ComplexRI(r.numer/r.denom, 0)

class Number:
    def __add__(self, other):
        x, y = self.coerce(other)
        return x.add(y)

    def __mul__(self, other):
        x, y = self.coerce(other)
        return x.mul(y)

    def coerce(self, other):
        # No coercion yet
        return self, other

    coercions = {('rat', 'com'): rational_to_complex}


from fractions import gcd
class Rational(Number):
    type_tag = 'rat'

    def __init__(self, numer, denom):
        g = gcd(numer, denom)
        self.numer = numer // g
        self.denom = denom // g

    def add(self, other):
        nx, dx = self.numer, self.denom
        ny, dy = other.numer, other.denom
        return Rational(nx * dy + ny * dx, dx * dy)

    def mul(self, other):
        numer = self.numer * other.numer
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __repr__(self):
        return 'Rational({0}, {1})'.format(self.numer, self.denom)

class Complex(Number):
    type_tag = 'com'

    def add(self, other):
        return ComplexRI(self.real + other.real, self.imag + other.imag)

    def mul(self, other):
        return ComplexMA(self.magnitude * other.magnitude, self.angle + other.angle)

class ComplexRI(Complex):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    @property
    def magnitude(self):
        return (self.real ** 2 + self.imag ** 2) ** 0.5

    @property
    def angle(self):
        return atan2(self.imag, self.real)

    def __repr__(self):
        return 'ComplexRI({0:g}, {1:g})'.format(self.real, self.imag)

class ComplexMA(Complex):
    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = angle

    @property
    def real(self):
        return self.magnitude * cos(self.angle)

    @property
    def imag(self):
        return self.magnitude * sin(self.angle)

    def __repr__(self):
        return 'ComplexMA({0:g}, {1:g} * pi)'.format(self.magnitude, self.angle/pi)





# Demo: Linked Lists
class Link:
    """A linked list, with Python integration."""
    empty = None

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is Link.empty:
            rest = ''
        else:
            rest = ', ' + repr(self.rest)
        return 'Link({}{})'.format(self.first, rest)

    def __str__(self):
        if self.rest is Link.empty:
            rest = ''
        else:
            rest = ' ' + str(self.rest)[2:-2]
        return '< {}{} >'.format(self.first, rest)

    def __len__(self):
        if self.rest is Link.empty:
            return 1
        return 1 + len(self.rest)  # self.rest.__len__()

    def __getitem__(self, index):
        if index == 0:
            return self.first
        elif self.rest is Link.empty:
            raise IndexError
        return self.rest[index - 1]  # self.rest.__getitem__(index - 1)

    def __add__(self, other):
        return self # Implement me

    def map(self, fn):
        """
        >>> odds = Link(1, Link(Link(Link(3)), Link(5)))
        >>> odds.map(lambda x: x + 2)
        >>> print(odds)
        < 3 < < 5 > > 7 >
        """
        pass # Implement me

    def remove_alternates(self):
        """
        >>> odds = Link(1, Link(2, Link(3, Link(4, Link(5)))))
        >>> odds.remove_alternates()
        >>> print(odds)
        < 1 3 5 >
        >>> evens = Link(0, Link(1, Link(2, Link(3, Link(4, Link(5))))))
        >>> evens.remove_alternates()
        >>> print(evens)
        < 0 2 4 >
        """
        pass # Implement me

odds = Link(1, Link(3, Link(5)))
foo = Link(2, Link(0, Link(1, Link(4))))





# Demo: Trees
class Tree:
    def __init__(self, datum, *args):
        self.datum = datum
        self.children = []
        for tree in args:
            assert type(tree) is Tree, str(tree)+" is not a Tree!"
            self.children.append(tree)

    def sum_tree(self):
        """ Adds together the contents of a tree.
        >>> t = Tree(1, Tree(2, Tree(4), Tree(5)), Tree(3, Tree(6)))
        >>> t.sum_tree()
        21
        >>> print(Tree('hello', Tree(' '), Tree('world', Tree('!'))).sum_tree())
        hello world!
        """
        total = self.datum
        for child in self.children:
            total += child.sum_tree()
        return total

    def max_tree(self):
        """ Returns the maximum datum in the tree.
        >>> t = Tree(1, Tree(2, Tree(4), Tree(5)), Tree(3, Tree(6)))
        >>> t.max_tree()
        6
        >>> t = Tree(-1, Tree(-2, Tree(-4), Tree(-5)), Tree(-3, Tree(-6)))
        >>> t.max_tree()
        -1
        """
        return 0 # Implement me

    def dejavu(self, n):
        """ Returns True if there is a path in tree that adds up to n.
        >>> t = Tree(1, Tree(2, Tree(4), Tree(5)), Tree(3, Tree(6)))
        >>> t.pretty_print()
        1
        |__2
        |  |__4
        |  |__5
        |__3
           |__6
        >>> t.dejavu(10) # 1 -> 3 -> 6
        True
        >>> t.dejavu(4)
        False
        >>> t.dejavu(9)
        False
        >>> t.dejavu(8) # 1 -> 2 -> 5
        True
        """
        return False # Implement me

    def pretty_print(self, indent=''):
        """ Prints the tree.
        >>> t = Tree(1, Tree(2, Tree(4), Tree(5)), Tree(3, Tree(6)))
        >>> t.pretty_print()
        1
        |__2
        |  |__4
        |  |__5
        |__3
           |__6
           
        >>> Tree(0, Tree('hello'), Tree('world'), Tree('!')).pretty_print()
        0
        |__hello
        |__world
        |__!
        >>> Tree(0, Tree('hello', Tree('world')), Tree('Goodbye')).pretty_print()
        0
        |__hello
        |  |__world
        |__Goodbye

        """
        if not indent:
            print(self.datum)
        else:
            print(indent[:-3] + '|__' + str(self.datum))

        if self.children:
            for child in self.children[:-1]:
                child.pretty_print(indent + '|  ')
            self.children[-1].pretty_print(indent + '   ')




# Demo: Binary Trees

class BinaryTree:
    def __init__(self, datum, left=None, right=None):
        self.datum = datum
        self.left = left
        self.right = right

    def __str__(self, indent=''):
        """
        >>> t = BinaryTree(1, BinaryTree(2), BinaryTree(3))
        >>> print(t)
          3
        1
          2
        >>> t = BinaryTree(1, BinaryTree(2, BinaryTree(3), BinaryTree(4)))
        >>> print(t)
        1
            4
          2
            3
        """
        result = ''
        if self.right:
            result += self.right.__str__(indent + '  ') + '\n'
        result += indent + str(self.datum) + '\n'
        if self.left:
            result += self.left.__str__(indent + '  ') + '\n'
        return result[:-1] # Remove last newline

    def __iter__(self):
        """
        >>> t = BinaryTree(4, BinaryTree(2, BinaryTree(1), BinaryTree(3)))
        >>> t = BinaryTree(5, t, BinaryTree(6, None, BinaryTree(7)))
        >>> print(t)
            7
          6
        5
          4
              3
            2
              1
        >>> for num in t:
        ...     print(num)
        ... 
        1
        2
        3
        4
        5
        6
        7
        """
        return self  # Implement me






# Demo: Memoization

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


fib_cache = {}
def memo_fib(n):
    if n <= 1:
        return n
    return memo_fib(n-1) + memo_fib(n-2)


def memo(f):
    """Return a memoized version of function f.
    """
    cache = {}
    def memoized(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return memoized

# @memo
# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n-1) + fib(n-2)


# def count_change(a, coins=(50, 25, 10, 5, 1)):
#     """Efficiently count the number of ways to make change.

#     >>> count_change(500, (50, 25, 10, 5, 1))
#     59576
#     """
#     if a == 0:
#         return 1
#     elif a < 0 or len(coins) == 0:
#         return 0
#     return count_change(a, coins[1:]) + count_change(a - coins[0], coins)
