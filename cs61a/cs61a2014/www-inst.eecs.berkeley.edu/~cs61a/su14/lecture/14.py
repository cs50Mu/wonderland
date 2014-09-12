class Link:

    empty = 'The Void'

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

# x = Link(3)
# x.first
# x.rest
# x.empty

# y = Link(5, Link(10))
# y.first
# y.rest
# y.rest.first
# y.rest.rest
# y.empty
# x.first

# Link.first
# Link.empty

# type(x)
# type(y)

class Link:

    empty = 'The Void'

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def to_str(self):
        s = '< '
        lst = self
        while lst != Link.empty:
            if type(lst.first) == Link:
                s = s + lst.first.to_str() + ' '
            else:
                s = s + str(lst.first) + ' '
            lst = lst.rest
        return s + '>'

# a = Link(5, Link(10))
# a.to_str()
# scheme_exp = Link('+', Link(Link('-', Link(3, Link(2))), Link(9)))
# scheme_exp.to_str()

# a.first += 1
# a.to_str()
# b = a
# b.first = 20
# a.to_str()

# c = Link(2)
# a.empty = None
# a.empty
# Link.empty
# c.empty
# Link.empty = None
# Link.empty
# c.empty
# c.to_str()
