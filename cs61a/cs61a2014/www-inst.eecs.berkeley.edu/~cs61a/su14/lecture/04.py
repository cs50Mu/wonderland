def countup(n):
    if n == 0:
        return
    else:
        countup(n-1)
        print(n)

def sum_linked_list(lst):
    if lst == empty:
        return 0
    else:
        return first(lst) + sum_linked_list(rest(lst))

sum_linked_list(link(1, link(2, link(3, empty))))


# Functional pairs

def cons(a, b):
    def pair(m):
        if m == 'car':
            return a
        else:
            return b
    return pair

def car(p):
    return p('car')

def cdr(p):
    return p('cdr')


# Implementation of linked lists using cons

empty = lambda: 42

def link(element, list):
    return cons(element, list)

def first(list):
    return car(list)

def rest(list):
    return cdr(list)

def print_linked_list(list):
    s = '<'
    while list != empty:
        s = s + repr(first(list)) + ' '
        list = rest(list)
    return s[:-1] + '>'
