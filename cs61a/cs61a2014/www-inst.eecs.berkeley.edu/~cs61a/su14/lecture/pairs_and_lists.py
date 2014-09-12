# Functional representation of pairs

# Don't worry if you don't understand this yet.
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

# Don't worry if you don't understand this yet.
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
    """Returns a list of the results produced by applying f to each
    element in lst.

    >>> my_list = link(1, link(2, link(3, link(4, empty))))
    >>> print_linked_list(map_linked_list(lambda x: x * x, my_list))
    < 1 4 9 16 >
    >>> pokemon = link('bulbasaur', link('charmander', link('squirtle', empty)))
    >>> print_linked_list(map_linked_list(print, pokemon))
    bulbasaur
    charmander
    squirtle
    < None None None >
    """
    if lst == empty:
        return empty
    else:
        return link(f(first(lst)), map_linked_list(f, rest(lst)))

def len_linked_list(lst):
    """Returns the length of the linked list.

    >>> len_linked_list(empty)
    0
    >>> len_linked_list(link(1, link(2, link(3, empty))))
    3
    >>> len_linked_list(link(1, link(link(2, link(3, empty)), empty)))
    2
    """
    if lst == empty:
        return 0
    else:
        return 1 + len_linked_list(rest(lst))

def reduce_linked_list(f, base, lst):
    """Combines all the elements of lst using the binary function f.
    If the elements of the lst are labelled l0, l1, ... ln, then it
    returns f(l0, f(l1, ... f(ln, base) ... ) )

    >>> reduce_linked_list(add, 4, link(1, link(2, link(3, empty))))
    10
    >>> reduce_linked_list(sub, 4, link(1, link(2, link(3, empty))))
    -2
    >>> reduce_linked_list(lambda x, y: str(x) + y, '', link(1, link(2, empty)))
    '12'
    """
    if lst == empty:
        return base
    else:
        return f(first(lst), reduce_linked_list(f, base, rest(lst)))
