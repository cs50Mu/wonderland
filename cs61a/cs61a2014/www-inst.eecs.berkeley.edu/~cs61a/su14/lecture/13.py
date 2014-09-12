# Aliasing
x = ['cs', 61, 'a']
y = x
y[2] = 'awesome'
x

a = ['cs', 61, 'a']
b = ['cs', 61, 'a']
b[2] = 'awesome'
a

# is vs. == (related to Aliasing)
x is y
x == y
x is b
x == b
a is b
a == b
a is a
a == a

# Mutating Lists
lst = [4, 8, 12]
lst.append(16)
lst
lst + [20]
lst
lst.append(24)
lst
lst[-1] = 20
lst[2:] = [16, 32]
lst.insert(2, 0)
lst.remove(0)
lst.insert(0, 2)
lst[5] = 64
lst.append(64)
lst

# Dictionaries
menu = {}
menu
menu = {'pizza': 15, 'penne': 8}
menu
menu['garlic bread'] = 6
menu
menu['risotto'] = 12
menu
for key in menu.keys():
    print(key, 'costs', menu[key], 'dollars')
menu.keys()
items = list(menu.keys())
items
items.sort()
items
for key in items:
    print(key, 'costs', menu[key], 'dollars')
pizzas = {}
pizzas['small'] = 7
pizzas['medium'] = 10
pizzas['large'] = 15
pizzas
menu['pizza'] = pizzas
menu
del menu['garlic bread']
menu
menu[['garlic', 'bread']] = 6
menu[('garlic', 'bread')] = 6
menu
