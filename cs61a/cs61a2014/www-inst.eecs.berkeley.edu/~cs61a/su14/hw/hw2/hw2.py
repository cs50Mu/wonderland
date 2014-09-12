# CS 61A Spring 2014
# Name:
# Login:

def square(x):
    """ Returns x squared. """
    return x * x

def product(n, term):
    """ Return the product of the first n terms in a sequence.

    term -- a function that takes one argument

    >>> product(4, square)
    576
    >>> product(3, lambda x: 2 * x)
    48
    >>> product(6, lambda x: 2)
    64
    """
    "*** YOUR CODE HERE ***"

def factorial(n):
    """ Return n factorial for n >= 0 by calling product.

    >>> factorial(4)
    24
    >>> factorial(6)
    720
    """
    "*** YOUR CODE HERE ***"

def accumulate(combiner, start, n, term):
    """ Return the result of combining the first n terms in a sequence.
    
    >>> accumulate(lambda a, b: a + b, 0, 5, lambda x: x)
    15
    >>> accumulate(pow, 2, 3, lambda x: 2)
    65536
    >>> accumulate(lambda x, y: x * y, 1, 4, lambda k: 3)
    81
    """
    "*** YOUR CODE HERE ***"

def summation_using_accumulate(n, term):
    """ An implementation of summation using accumulate.

    >>> summation_using_accumulate(4, square)
    30
    >>> summation_using_accumulate(4, lambda x: 2**x)
    30
    """
    "*** YOUR CODE HERE ***"

def product_using_accumulate(n, term):
    """ An implementation of product using accumulate.

    >>> product_using_accumulate(4, square)
    576
    >>> product_using_accumulate(6, lambda x: 3)
    729
    """
    "*** YOUR CODE HERE ***"


def repeated(f, n):
    """ Return the function that computes the nth application of f.

    f -- a function that takes one argument
    n -- a positive integer

    >>> repeated(square, 2)(5)
    625
    >>> repeated(square, 4)(5) # square(square(square(square(square(x)))))
    152587890625
    >>> repeated(lambda x: x + 1, 5)(309)
    314
    >>> repeated(lambda x: 2**x, 3)(2)
    65536
    """
    "*** YOUR CODE HERE ***"

def double(f):
    """ Return a function that applies f twice.

    f -- a function that takes one argument

    >>> double(square)(2)
    16
    """
    "*** YOUR CODE HERE ***"

def compose1(f, g):
    """ Return a function h, such that h(x) = f(g(x)). """
    def h(x):
        return f(g(x))
    return h

def zero(f):
    return lambda x: x

def successor(n):
    return lambda f: lambda x: f(n(f)(x))

def one(f):
    """ Church numeral 1. """
    "*** YOUR CODE HERE ***"

def two(f):
    """ Church numeral 2. """
    "*** YOUR CODE HERE ***"

def church_to_int(n):
    """ Convert the Church numeral n to a Python integer.

    >>> church_to_int(zero)
    0
    >>> church_to_int(one)
    1
    >>> church_to_int(two)
    2
    """
    "*** YOUR CODE HERE ***"

def add_church(m, n):
    """ Return the Church numeral for m + n, for Church numerals m and n.

    >>> three = successor(two)
    >>> church_to_int(add_church(two, three))
    5
    """
    "*** YOUR CODE HERE ***"

def mul_church(m, n):
    """ Return the Church numeral for m * n, for Church numerals m and n.

    >>> three = successor(two)
    >>> four = successor(three)
    >>> church_to_int(mul_church(two, three))
    6
    >>> church_to_int(mul_church(three, four))
    12
    """
    "*** YOUR CODE HERE ***"



