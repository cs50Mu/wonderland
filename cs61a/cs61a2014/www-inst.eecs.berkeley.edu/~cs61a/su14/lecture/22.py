# from ucb import trace

def fib_iterative(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def fib(n, a=0, b=1):
  if n == 0:
    return a
  return fib(n-1, b, a+b)

# fib_iterative(10)
# fib(10)
# fib_iterative(1000)
# fib(1000)
