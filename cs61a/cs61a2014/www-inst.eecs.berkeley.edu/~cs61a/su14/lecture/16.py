# Demo: ALL the for loops
# All the different things for which we can use for loops

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
# for color in colors:  # colors is a list object.
#     print(color)

instructors = 'Rohin', 'Andrew'
# for instructor in instructors:  # instructors is a tuple object.
#     print(instructor)

odds = range(1, 10, 2)
# for num in odds:  # odds is a range object.
#     print(num)

glookup = { 'hw' : 2, 'lab' : 1, 'proj1' : 17, 'proj2' : 12, 'test1' : 50 }
# for key in glookup:  # glookup is a dictionary object.
#     print('{0} has a maximum score of {1}'.format(key, glookup[key]))

vowels = 'aeiou'
# for vowel in vowels:  # vowels is a string object.
#     print(vowel)






# Demo: Implementing the Interface
class Foo:
    # Adding this method wouldn't make any difference.
    # def __len__(self):
    #     return 2

    def __getitem__(self, i):
        if i < 3:
            return 1
        raise IndexError

# for i in Foo():
#     print(i)



# Demo: Implementing __next__
class RangeIterator:
    def __init__(self, start, end):
        self.val = start
        self.end = end
    def __next__(self):
        if self.val >= self.end:
            raise StopIteration
        value_to_return = self.val
        self.val += 1
        return value_to_return

teens = RangeIterator(13, 20)
# next(teens)
# try:
#     while True:
#         print(next(teens))
# except StopIteration:
#     pass

# teens = RangeIterator(13, 20)
# for i in teens:
#     print(i)





# Demo: Fixing the code
# class RangeIterator:
#     def __init__(self, start, end):
#         self.val = start
#         self.end = end

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.val >= self.end:
#             raise StopIteration
#         value_to_return = self.val
#         self.val += 1
#         return value_to_return

# teens = RangeIterator(13, 20)
# for i in teens:
#     print(i)

# x = RangeIterator(1, 6)
# iter1 = iter(x)
# next(iter1)
# next(iter1)
# iter2 = iter(x)
# next(iter2)
# next(iter1)
# next(iter2)
# next(iter2)

# one_to_five = RangeIterator(1, 6)
# for num1 in one_to_five:
#     for num2 in one_to_five:
#         print(num1, num2)

# Demo:  Why do we have __iter__?
class PrefixIterator:
    def __init__(self, string):
        self.string = string
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= len(self.string):
            raise StopIteration
        self.i += 1
        return self.string[:self.i]

# abc = PrefixIterator('abc')
# for i in abc:
#     for j in abc:
#         print(i, j)

# Note that this class does not have a __next__
class PrefixString(str):
    def __iter__(self):
        return PrefixIterator(self)

# abc = PrefixString('abc')
# for i in abc:
#     for j in abc:
#         print(i, j)





# Demo: Mutation in For Loops
# lst = list(range(10, 20))
# for item in lst:
#     print(item)
#     lst.remove(item)
# lst

class BetterList(list):
    def __iter__(self):
        return list.__iter__(self[:])






# Demo: Generators, Generator Expressions
def generate_range(start, end):
    while start < end:
        yield start
        start += 1

# teens = generate_range(13, 20)
# teens
# next(teens)
# next(teens)
# for num in teens:
#     print(num)

# [i for i in range(30) if i % 3 == 0]
# (i for i in range(30) if i % 3 == 0)
# multiples_of_three = (i for i in range(30) if i % 3 == 0)
# next(multiples_of_three)
# for i in multiples_of_three:
#     print(i)

def infinite_range_with_step(start, step):
    while True:
        yield start
        start += step

odds = infinite_range_with_step(1, 2)
evens = infinite_range_with_step(2, 2)

def alternate():
    print(next(odds))
    print(next(evens))

# alternate()
# for i in range(5):
#     alternate()






# Demo: All Hail Generators!

def subsets(lst, n):
    """
    >>> subsets([5, 6, 7, 8], 2)
    [[5, 6], [5, 7], [5, 8], [6, 7], [6, 8], [7, 8]]
    """
    if n == 0:
        return [[]]
    elif len(lst) == n:
        return [ lst ]
    results = []
    # Either we take the first element:
    for subset in subsets(lst[1:], n - 1):
        results.append([lst[0]] + subset)
    # ... or we don't.
    without_first = subsets(lst[1:], n)
    return results + without_first

def generate_subsets(lst, n):
    """
    >>> for sub in generate_subsets([5, 6, 7, 8], 2):
    ...     print(sub)
    ... 
    [5, 6]
    [5, 7]
    [5, 8]
    [6, 7]
    [6, 8]
    [7, 8]
    """
    if n == 0:
        yield []
    elif len(lst) == n:
        yield lst
    else:
        # Either we take the first element:
        for subset in generate_subsets(lst[1:], n - 1):
            yield [lst[0]] + subset
        # ... or we don't.
        for subset in generate_subsets(lst[1:], n):
            yield subset
