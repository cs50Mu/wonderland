def square(x):
    """Returns the square of x.
    >>> square(3)
    9
    >>> square(12)
    144
    """
    return x * x

def super_compose(mask, *args):
    """
    >>> add_one = lambda x: x + 1
    >>> double = lambda x: 2 * x
    >>> identity = super_compose('000', square, double, add_one)
    >>> identity(5)
    5
    >>> quadric = super_compose('11', square, square)
    >>> quadric(4)
    256
    >>> quadric_and_one = super_compose('1101', add_one, square, double, square)
    >>> quadric_and_one(3)
    82
    """
    def result(x):
        if "YOUR CODE HERE":
            return x
        rest_fn = super_compose(mask[1:], *args[1:])
        if mask[0] == '0':
            "YOUR CODE HERE"
        else:
            "YOUR CODE HERE"
    return "YOUR CODE HERE"

def super_compose2(mask, *args):
    """
    >>> add_one = lambda x: x + 1
    >>> double = lambda x: 2 * x
    >>> identity = super_compose2('000', square, double, add_one)
    >>> identity(5)
    5
    >>> quadric = super_compose2('11', square, square)
    >>> quadric(4)
    256
    >>> quadric_and_one = super_compose2('1101', add_one, square, double, square)
    >>> quadric_and_one(3)
    82
    """
    def helper(mask, funcs, x):
        if "YOUR CODE HERE":
            return x
        elif mask[0] == '0':
            "YOUR CODE HERE"
        else:
            "YOUR CODE HERE"
    return "YOUR CODE HERE"

def super_compose3(mask, *args):
    """
    >>> add_one = lambda x: x + 1
    >>> double = lambda x: 2 * x
    >>> identity = super_compose3('000', square, double, add_one)
    >>> identity(5)
    5
    >>> quadric = super_compose3('11', square, square)
    >>> quadric(4)
    256
    >>> quadric_and_one = super_compose3('1101', add_one, square, double, square)
    >>> quadric_and_one(3)
    82
    """
    def helper(x):
        for VARIABLE in "ITERABLE":
            if "YOUR CODE HERE":
                "YOUR CODE HERE"
        return x
    return "YOUR CODE HERE"

# square = 4

def count_link_atoms(link_lst):
    """ Counts the number of atoms (things that are not pairs or empty lists)
    in link_lst, which is a (possibly deep) linked list.

    >>> count_link_atoms(link('s', link('u', link(1, link(4, empty)))))
    4
    >>> count_link_atoms(to_linked_list([[[1, 2], 3], 4, 5, [9, [10]]]))
    7
    """
    if link_lst == empty:
        return "YOUR CODE HERE"
    elif "YOUR CODE HERE":
        return "YOUR CODE HERE"
    else:
        return "YOUR CODE HERE"

def count_atoms(lst_or_atom):
    """ Counts the number of atoms (things that are not lists)
    in lst_or_atom, which is a (possibly deep) Python list.

    >>> count_atoms(['s', 'u', 1, 4])
    4
    >>> count_atoms([[[1, 2], 3], 4, 5, [9, [10]]])
    7
    """
    if type(lst_or_atom) != list:
        return "YOUR CODE HERE"
    return "YOUR CODE HERE"


def edit_distance(s1, s2):
    """
    Computes the edit distance between s1 and s2.
    >>> edit_distance('sunny', 'sunny')
    0
    >>> edit_distance('sunny', 'funny')
    1
    >>> edit_distance('foo', 'bar')
    3
    >>> edit_distance('sun', 'rain')
    3
    >>> 5 # edit_distance('polynomial', 'exponential')
    6
    """
    return 0

def make_deep_generator(thing):
    """
    Yields all non-iterable elements in thing.
    If thing is iterable and contains iterable elements, those
    elements will be searched recursively.
    
    >>> g = make_deep_generator([1, 2, [3, 4], [[5]]])
    >>> next(g)
    1
    >>> for x in g:
    ...     print(x)
    ...
    2
    3
    4
    5
    """
    if "YOUR CODE HERE":
        yield thing
    "YOUR CODE HERE"


##############
# Given code #
##############

class PairError(Exception):
    pass

def cons(a, b):
    def answer(m):
        if m == 'car':
            return a
        elif m == 'cdr':
            return b
        else:
            # This is a way for us to create our own error messages.
            raise PairError('You can only use car or cdr on a pair!')
    return answer

def car(p):
    """
    >>> car(cons(1, 2))
    1
    """
    return p('car')

def cdr(p):
    """
    >>> cdr(cons(1, 2))
    2
    """
    return p('cdr')

def is_pair(pair):
    """
    >>> is_pair(cons(1, 2))
    True
    >>> is_pair(1)
    False
    >>> is_pair(lambda x: x)
    False
    >>> is_pair([1, 2])
    False
    """
    try:
        pair('invalid')
        return False
    except PairError:
        return True
    except:
        return False

# Implementation of linked lists using cons

class ListError(Exception):
    pass

empty = lambda: 42

def link(element, lst):
    return cons(element, lst)

def first(lst):
    """
    >>> first(link(1, link(2, empty)))
    1
    """
    if lst == empty:
        # This is a way for us to create our own error messages.
        raise ListError('Cannot call first on the empty list!')
    return car(lst)

def rest(lst):
    """
    >>> rest(rest(link(1, link(2, empty)))) == empty
    True
    >>> first(rest(link(1, link(2, empty))))
    2
    """
    if lst == empty:
        # This is a way for us to create our own error messages.
        raise ListError('Cannot call rest on the empty list!')
    return cdr(lst)

def is_linked_list(lst):
    """
    >>> is_linked_list(empty)
    True
    >>> is_linked_list(link(1, link(4, link(7, empty))))
    True
    >>> is_linked_list(link(1, link(4, 7)))
    False
    >>> is_linked_list(link(link(2, empty), empty))
    True
    """
    return lst == empty or (is_pair(lst) and is_linked_list(rest(lst)))

def linked_list_to_str(lst):
    s = '< '
    while lst != empty:
        if is_linked_list(first(lst)):
            s = s + linked_list_to_str(first(lst)) + ' '
        else:
            s = s + repr(first(lst)) + ' '
        lst = rest(lst)
    return s + '>'

def print_linked_list(lst):
    """
    >>> print_linked_list(empty)
    < >
    >>> print_linked_list(link(1, empty))
    < 1 >
    >>> print_linked_list(link(2, link(3, link(link(4, empty), empty))))
    < 2 3 < 4 > >
    >>> print_linked_list(link(1, link(link(2, link(3, empty)), \
            link(4, link(link(5, link(6, link(7, empty))), empty)))))
    < 1 < 2 3 > 4 < 5 6 7 > >
    """
    print(linked_list_to_str(lst))

def map_linked_list(f, lst):
    if lst == empty:
        return empty
    return link(f(first(lst)), map_linked_list(f, rest(lst)))

def to_linked_list(lst):
    if lst == []:
        return empty
    if type(lst) != type([]):
        return lst
    return link(to_linked_list(lst[0]), to_linked_list(lst[1:]))
