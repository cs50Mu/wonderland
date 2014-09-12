# Unrelated
'Germany' > 'Argentina'


# This is an object
12

# This is also an object
2.3

# This float object has a function is_integer
(2.3).is_integer

# we call the is_integer method
(2.3).is_integer()

# This int object does not have an is_integer method
(12).is_integer()

# by Googling "python3 built in types", I get
# https://docs.python.org/3/library/stdtypes.html
# which provides me more info

# Here is another object
x = "Troy and Abed in the morning"

# Let's try calling its string methods
x.split()
x.count('e')
x.count('in')
x.islower()
x.swapcase()

# I can also make new objects

# This breaks
'12' + 8

# Here I am making the actual integer object 12 
# from the string '12'
int('12')

int('12') + 8

# Garbage in => garbage out
# The int constructor cannot take in strings
# that don't describe integers
int('foo')


# Some examples of mutating lists:
# Try this out in pythontutor:
# http://pythontutor.com/composingprograms.html#mode=edit
x = [1, 2, 3]
y = x
x[2] = 4
y

x = [1, 2, 3]
y = [1, 2, 3]

x == y
x is y

x[2] = 4
y


z = [1, [2, 3], 4]
k = z[1]
k[1] = 9
z
k

a = [1, 2, 3]
b = a + [4]
a == b
