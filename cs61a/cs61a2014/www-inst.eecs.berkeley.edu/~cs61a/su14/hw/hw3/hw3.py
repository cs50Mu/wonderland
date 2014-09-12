# CS 61A Spring 2014
# Name:
# Login:


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
    return p('car')

def cdr(p):
    return p('cdr')


# Implementation of linked lists using cons

empty = lambda: 42

def link(element, lst):
    return cons(element, lst)

def first(lst):
    return car(lst)

def rest(lst):
    return cdr(lst)

def print_linked_list(lst):
    print(linked_list_to_str(lst))

def linked_list_to_str(lst):
    s = '< '
    while lst != empty:
        s = s + repr(first(lst)) + ' '
        lst = rest(lst)
    return s[:-1] + ' >'


def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.
    
    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    "*** YOUR CODE HERE ***"



def starts_with(lst, sublst):
    """Returns True if sublst is a prefix of lst, False otherwise.
    Note that it is possible for sublst to be larger than lst.

    >>> x = link(3, link('foo', link(6, link(6, empty))))
    >>> print_linked_list(x)
    < 3 'foo' 6 6 >
    >>> starts_with(x, empty)
    True
    >>> starts_with(x, link(3, empty))
    True
    >>> starts_with(x, link(6, empty))
    False
    >>> starts_with(x, x)
    True
    >>> starts_with(link(2, empty), link(2, link(3, empty)))
    False
    """
    "*** YOUR CODE HERE ***"



def has_sublist(lst, sublst):
    """Returns True if sublst is present anywhere in lst, False otherwise.

    >>> has_sublist(empty, empty)
    True
    >>> x = link('A', link('G', link('T', link('T', link('G', link('C', empty))))))
    >>> print_linked_list(x)
    < 'A' 'G' 'T' 'T' 'G' 'C' >
    >>> has_sublist(x, empty)
    True
    >>> has_sublist(x, link(2, link(3, empty)))
    False
    >>> has_sublist(x, link('A', link('T', empty)))
    False
    >>> has_sublist(x, link('G', link('T', link('T', empty))))
    True
    >>> has_sublist(link(1, link(2, link(3, empty))), link(2, empty))
    True
    >>> has_sublist(x, link('A', x))
    False
    """
    "*** YOUR CODE HERE ***"



def has_jhh_gene(dna_seq):
    """Returns True if dna_seq contains the J.H.H. gene 'CATCAT'.
    >>> dna = link('C', link('A', link('T', empty)))
    >>> dna = link('C', link('A', link('T', link('G', dna))))
    >>> print_linked_list(dna)
    < 'C' 'A' 'T' 'G' 'C' 'A' 'T' >
    >>> has_jhh_gene(dna)
    False
    >>> dna = link('T', link('C', link('A', link('T', link('G', empty)))))
    >>> dna = link('G', link('T', link('A', link('C', link('A', dna)))))
    >>> print_linked_list(dna)
    < 'G' 'T' 'A' 'C' 'A' 'T' 'C' 'A' 'T' 'G' >
    >>> has_jhh_gene(dna)
    True
    """
    jhh = link('C', link('A', link('T', link('C', link('A', link('T', empty))))))
    return has_sublist(dna_seq, jhh)



def count_change(amount, denominations):
    """Returns the number of ways to make change for amount.

    >>> denominations = link(50, link(25, link(10, link(5, link(1, empty)))))
    >>> print_linked_list(denominations)
    < 50 25 10 5 1 >
    >>> count_change(7, denominations)
    2
    >>> count_change(100, denominations)
    292
    >>> denominations = link(16, link(8, link(4, link(2, link(1, empty)))))
    >>> print_linked_list(denominations)
    < 16 8 4 2 1 >
    >>> count_change(7, denominations)
    6
    >>> count_change(10, denominations)
    14
    >>> count_change(20, denominations)
    60
    """
    "*** YOUR CODE HERE ***"

def towers_of_hanoi(n, start, end):
    """Print the moves required to solve the towers of hanoi game if we start
    with n disks on the start pole and want to move them all to the end pole.

    The game is to assumed to have 3 poles (which is traditional).

    >>> towers_of_hanoi(1, 1, 3)
    Move 1 disk from rod 1 to rod 3
    >>> towers_of_hanoi(2, 1, 3)
    Move 1 disk from rod 1 to rod 2
    Move 1 disk from rod 1 to rod 3
    Move 1 disk from rod 2 to rod 3
    >>> towers_of_hanoi(3, 1, 3)
    Move 1 disk from rod 1 to rod 3
    Move 1 disk from rod 1 to rod 2
    Move 1 disk from rod 3 to rod 2
    Move 1 disk from rod 1 to rod 3
    Move 1 disk from rod 2 to rod 1
    Move 1 disk from rod 2 to rod 3
    Move 1 disk from rod 1 to rod 3
    """
    "*** YOUR CODE HERE ***"

def move_disk(start, end):
    print("Move 1 disk from rod", start, "to rod", end)

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    """
    return YOUR_EXPRESSION_HERE


