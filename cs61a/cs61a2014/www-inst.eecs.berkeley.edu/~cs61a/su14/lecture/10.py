# Black magic to find the name of a function.
def name(fn):
    return fn.__name__

def args_to_string(args):
    string = ''
    for arg in args:
        string += str(arg) + ' '
    return string

# Meant to be used as a decorator
def trace(fn):
    def new_fn(*args):
        print(name(fn) + ' called with ' + args_to_string(args))
        result = fn(*args)
        print(name(fn) + ' returns ' + str(result))
        return result
    return new_fn

# Using trace as a decorator.
@trace
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

@trace
def better_fib(n, a=0, b=1):
  if n == 0:
    return a
  else:
    return better_fib(n-1, b, a+b)

# If you uncomment these and run
# python3 10.py
# It will print out the trace.
# Beware:  fib(20) prints out tens of thousands of lines.

# fib(3)
# fib(20)
# better_fib(20)

# Iterative improvement.  Used in Newton's method.
def iter_improve(guess, done, update):
    while not done(guess):
        guess = update(guess)
    return guess

tolerance = 1e-14

def find_zero(f, df, x=1):
    def done(x):
        return abs(f(x)) < tolerance
    def update(x):
        return x - ( f(x) / df(x) )
    return iter_improve(x, done, update)

def sqrt(a):
    return find_zero(lambda x: x*x - a, lambda x: 2*x)

def root(n, a):
    return find_zero(lambda x: pow(x, n) - a, lambda x: n*pow(x, n-1))

dx = 1e-6
def deriv(f):
    def df(x):
        return (f(x + dx) - f(x)) / dx
    return df

def easy_find_zero(f, x=1):
    return find_zero(f, deriv(f), x)

def fixed_point(f):
    return easy_find_zero(lambda x: x - f(x))

def sqrt2(a):
    return fixed_point(lambda x: a / x)
