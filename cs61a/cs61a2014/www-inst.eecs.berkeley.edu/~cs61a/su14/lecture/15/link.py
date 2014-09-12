class Link:
    """A recursive list, with Python integration."""
    empty = None

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is Link.empty:
            rest = ''
        else:
            rest = ', ' + repr(self.rest)
        return 'Link({}{})'.format(self.first, rest)

    def __str__(self):
        if self.rest is Link.empty:
            rest = ''
        else:
            rest = ', ' + str(self.rest)[1:-1]
        return '< {}{} >'.format(self.first, rest)

    def __len__(self):
        if self.rest is Link.empty:
            return 1
        return 1 + len(self.rest)  # self.rest.__len__()

    def __getitem__(self, index):
        if index == 0:
            return self.first
        elif self.rest is Link.empty:
            raise IndexError
        return self.rest[index - 1]  # self.rest.__getitem__(index - 1)

    def __add__(self, other):
        return list_to_link(list(self) + list(other))


def list_to_link(lst):
    ll = Link.empty
    for elem in lst[::-1]:
        ll = Link(elem, ll)
    return ll


my_lst = Link(1, Link(2, Link(3)))

