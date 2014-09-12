# Try this out and try drawing the environment diagram for it.

def make_counter():
  counter = 0
  def func():
    nonlocal counter
    counter += 1
    return counter
  return func

c1 = make_counter()
c1()
c1()
c2 = make_counter()
c2()
c1()
