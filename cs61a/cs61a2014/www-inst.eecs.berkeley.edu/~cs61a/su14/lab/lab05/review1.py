from fractions import gcd

#Question 7
def make_rat(num, den):
    """Creates a rational number, given a numerator and denominator."""
    g = gcd(num, den)
    return [num // g, den // g]

def num(rat):
    """Extracts the numerator from a rational number.
    >>> num(make_rat(2, 4))
    1
    """
    return rat[0]

def den(rat):
    """Extracts the denominator from a rational number.
    >>> den(make_rat(2, 4))
    2
    """
    return rat[1]

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
    return make_rat(num(a) * num(b), den(a) * den(b))

def prod_rats(rats):
    """Returns a rational number that is the product of the rational
    numbers in rats.
    >>> x = prod_rats([make_rat(2, 4), make_rat(5, 9), make_rat(6, 4)])
    >>> num(x)
    5
    >>> den(x)
    12
    """
    total, i = [1, 1], 0
    while i < len(rats):
        total = [total[0]*rats[i][0], total[1]*rats[i][1]]
        i += 1
    g = gcd(total[0], total[1])
    return [total[0] // g, total[1] // g]



#Question 8

def insert_at_end(lst, elem):
    """Return a linked list that is the same as lst with elem added at the end.

    >>> lst1 = link(1, link(2, empty))
    >>> print_linked_list(lst1)
    < 1 2 >
    >>> lst2 = insert_at_end(lst1, 3)
    >>> print_linked_list(lst2)
    < 1 2 3 >
    """
    "*** YOUR CODE HERE ***"


#Question 9

def reverse(lst):
    """Returns a new list that contains the elements of lst in reverse order.

    >>> lst = link(1, link(2, link(3, empty)))
    >>> print_linked_list(lst)
    < 1 2 3 >
    >>> reversed_lst = reverse(lst)
    >>> print_linked_list(reversed_lst)
    < 3 2 1 >
    """
    "*** YOUR CODE HERE ***"


#Question 12

def catchphrase(say, person):
    """
    >>> say = lambda a: 'Darknesss' if a == 'Nocturne' else 'Mundo'
    >>> phrase = catchphrase(say, None)
    Welcome to Summoner's Rift!
    >>> phrase 
    False
    >>> catchphrase(say, 'Mundo')
    'Mundo'
    >>> catchphrase(say, 'Nocturne')
    'report feeder'
    """

    if ______:
        print("Welcome to Summoner's Rift!")
        return ______
    if say(person) == 'Darknesss':
        return 'report feeder'
    else:
        _____



#These functions are given to you
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
    >>> print_linked_list(link(1, link(link(2, link(3, empty)), link(4, link(link(5, link(6, link(7, empty))), empty)))))
    < 1 < 2 3 > 4 < 5 6 7 > >
    """
    print(linked_list_to_str(lst))
