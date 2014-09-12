from ucb import trace
from time import time

def timer_generator(n):
    def timer(fn):
        def new_fn(*args):
            start = time()
            for i in range(n):
                result = fn(*args)
            end = time()
            return end - start
        return new_fn
    return timer

@timer_generator(10000)
def make_list(n):
    lst = []
    for i in range(n):
        lst = [ i ] + lst
    return lst

@timer_generator(10000)
def mutating_make_list(n):
    lst = []
    for i in range(n):
        lst.append(i)
    return lst

@timer_generator(10000)
def make_linked_list(n):
    lst = empty
    for i in range(n):
        lst = link(i, lst)
    return lst

def list_item_experiment(n):
    lst = list(range(n))
    @timer_generator(100000)
    def get_middle_item():
        return lst[n // 2]
    return get_middle_item()

def linked_list_item_experiment(n):
    lst = enumerate_linked_list(n)
    @timer_generator(100000)
    def get_middle_item():
        return get_item(lst, n // 2)
    return get_middle_item()

























def link(a, b):
    return [a, b]

def first(lst):
    return lst[0]

def rest(lst):
    return lst[1]

empty = lambda: 42

def get_item(lst, i):
    if i == 0:
        return first(lst)
    else:
        return get_item(rest(lst), i - 1)

def enumerate_linked_list(n):
    lst = empty
    for i in range(n):
        lst = link(i, lst)
    return lst
