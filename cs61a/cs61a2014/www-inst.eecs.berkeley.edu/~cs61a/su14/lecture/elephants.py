## First Elephant ADT

def elephant(name, age, can_fly):
    """
    Takes in a string name, an int age, and a boolean can_fly.
    Constructs an elephant with these attributes.
    """
    return link(name, link(age, link(can_fly, empty)))

def elephant_name(elephant):
    return first(elephant)

def elephant_age(elephant):
    return first(rest(elephant))

def elephant_can_fly(elephant):
    return first(rest(rest(elephant)))


## Elephant billing (breaks abstraction barrier)

def elephant_billing_wrong(elephants):
    result = []
    for elephant in elephants:
        result += [first(elephant)] # WRONG
    return result


## But what if we did this?

def elephant(name, age, can_fly):
    return [name, age, can_fly]

def elephant_name(elephant):
    return elephant[0]

def elephant_age(elephant):
    return elephant[1]

def elephant_can_fly(elephant):
    return elephant[2]

## Elephant billing (correct)

def elephant_billing(elephants):
    result = []
    for elephant in elephants:
        result += [elephant_name(elephant)]
    return result

## For testing

chris = elephant('Chris', 37, False)
dumbo = elephant('Dumbo', 72, True)
gambino = elephant('Donald', 30, False)

stars = [chris, dumbo, gambino]


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

