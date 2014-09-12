## Data and Sequences, Data Abstraction ##

#Q4

def get_seven_a(lst):
    """
    >>> x = [1, 3, [5, 7], 9]
    >>> get_seven_a(x)
    7
    """
    return 'PUT YOUR CODE HERE'

def get_seven_b(lst):
    """
    >>> x = [[7]]
    >>> get_seven_b(x)
    7
    """
    return 'PUT YOUR CODE HERE'

def get_seven_c(lst):
    """
    >>> x = [1, [2, [3, [4, [5, [6, [7]]]]]]]
    >>> get_seven_c(x)
    7
    """
    return 'PUT YOUR CODE HERE'


#Q5

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


#Q6

def deep_len(lst):
    """Returns the deep length of the list.

    >>> deep_len([1, 2, 3])     # normal list
    3
    >>> x = [1, [2, 3], 4]      # deep list
    >>> deep_len(x)
    4
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> deep_len(x)
    6
    """
    "*** YOUR CODE HERE ***"


#Q7

def merge(lst1, lst2):
    """Merges two sorted lists recursively.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    "*** YOUR CODE HERE ***"



#Q8

def add_rat(a, b):
    """Adds two rational numbers A and B. For example,
    (3 / 4) + (5 / 3) = (29 / 12)

    >>> a, b = make_rat(3, 4), make_rat(5, 3)
    >>> c = add_rat(a, b)
    >>> num(c)
    29
    >>> den(c)
    12
    """
    "*** YOUR CODE HERE ***"


def sub_rat(a, b):
    """Subtracts two rational numbers A and B. For example,
    (3 / 4) - (5 / 3) = (-11 / 12)

    >>> a, b = make_rat(3, 4), make_rat(5, 3)
    >>> c = sub_rat(a, b)
    >>> num(c)
    -11
    >>> den(c)
    12
    """
    "*** YOUR CODE HERE ***"



#Q9
"""Your friend did a bad job making these functions, so you have to
make them now."""

from fractions import gcd

def make_rat(num, den):
    """Creates a rational number, given a numerator and denominator.

    >>> a = make_rat(2, 4)
    >>> num(a)
    1
    >>> den(a)
    2
    >>> make_rat('???', 2)
    Traceback (most recent call last):
        ...
    AssertionError
    """
    "*** YOUR CODE HERE ***"

def num(rat):
    """Extracts the numerator from a rational number."""
    "*** YOUR CODE HERE ***"

def den(rat):
    """Extracts the denominator from a rational number."""
    "*** YOUR CODE HERE ***"


# Q10


def print_rat(rat):
    ''' Print out rational numbers in human readable form

    >>> print_rat(make_rat(4, 5))
    4 / 5
    '''
    print(rat[0], '/', rat[1])

def approximate_pi(iter=1000):
    """ Computes an approximation of pi based on the idea
        pi/4 = (2/3)*(4/3)*(4/5)*(6/5)*(6/7)*(8/7)...

    >>> approximate_pi(10)
    3.2751010413348074
    >>> approximate_pi()
    3.1431607055322663
    >>> approximate_pi(10000)
    3.1417497057380523
    """
    result = make_rat(1, 1)
    compute_num = lambda x: 2 + 2 * ((x + 1) // 2)
    compute_dem = lambda x: 1 + 2 * ((x + 2) // 2)
    for i in range(iter):
        n = compute_num(i)
        d = compute_dem(i)
        result = [n * result[0], d * result[1]]
    return 4 * num(result) / result[1]
  

# You may need this for Question 11
def mul_rat(a, b):
    """Multiplies two rational numbers A and B. For example,
    (3 / 4) * (5 / 3) = (15 / 12)

    >>> a, b = make_rat(3, 4), make_rat(5, 3)
    >>> c = mul_rat(a, b)
    >>> num(c)
    5
    >>> den(c)
    4
    """
    "*** YOUR CODE HERE ***"

