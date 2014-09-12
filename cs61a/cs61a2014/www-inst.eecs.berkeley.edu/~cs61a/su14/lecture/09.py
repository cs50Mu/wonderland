# Try out fib(40) vs better_fib(40)!!!

def fib(n):
  if n < 2:
    return n
  else:
    return fib(n-1) + fib(n-2)

# a and b have default arguments
# of 0 and 1 resp. This means you can
# say better_fib(10) without providing
# erroring. It will instead do the
# same as better_fib(10, 0, 1)

def better_fib(n, a=0, b=1):
  if n == 0:
    return a
  else:
    return better_fib(n-1, b, a+b)


