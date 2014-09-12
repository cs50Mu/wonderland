x = 10 # This is true the entire time

def foo(x):
  x = 4
  x += 8
  return x

def bar():
  return x + 4

def baz():
  x = 8
  return x

# What is the value of x at this point?

def garply(): # This will break... why?
  x += 4
  return x

def snafu(): # This will break... why?
  x = x + 4
  return x

def xyzzy(): # This will also break... why?
  y = x
  x = y + 4
  return x
