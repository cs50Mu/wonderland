from operator import add, sub, mul
from pairs_and_lists import *
                                 # MINICALC FOR LECTURE
def repl():                      # FOR TEACHING PURPOSES,
    while True:                  # NO ERROR CHECKING
        print(calc_eval(read())) # FOR LECTURE, FIRST 27 LINES ARE IMPORTANT

def read():
    exp, extra = read_exp(tokenize(input('minicalc> ')))
    return exp

def calc_eval(exp):
    if is_linked_list(exp):
        return calc_apply(first(exp), map_linked_list(calc_eval, rest(exp)))
    return exp

def calc_apply(op, args):
    if op == '+':
        return do_addition(args)
    elif op == '*':
        return do_multiplication(args)
    elif op == '-':
        return do_subtraction(args)
    elif op == '/':
        return do_division(args)
    else:
        raise NameError('unknown operator {}'.format(op))

# LEXER
def tokenize(s):
    s = s.replace('(', ' ( ')
    s = s.replace(')', ' ) ')
    return s.split()

# PARSER
def read_exp(tokens):
    if tokens == []:
        raise SyntaxError('unexpected end of input')
    token, rest = tokens[0], tokens[1:]
    if token == ')':
        raise SyntaxError('unexpected )')
    elif token == '(':
        if rest == []:
            raise SyntaxError('mismatched parentheses')
        elif rest[0] == ')':
            raise SyntaxError('empty combination')
        return read_until_close(rest)
    else:
        return numberize(token), rest

# MUTUAL RECURSION WITH read_exp
def read_until_close(tokens):
    if tokens[0] == ')':
        return empty, tokens[1:]
    first, remaining = read_exp(tokens)
    rest, remaining = read_until_close(remaining)
    return link(first, rest), remaining

# HELPER FUNCTIONS
def numberize(atomic_exp):
    try:
        return int(atomic_exp)
    except ValueError:
        try:
            return float(atomic_exp)
        except ValueError:
            return atomic_exp

def do_addition(args):
    return reduce_linked_list(add, 0, args)

def do_multiplication(args):
    return reduce_linked_list(mul, 1, args)

def do_subtraction(args):
    length = len_linked_list(args)
    if length == 0:
        raise TypeError('not enough arguments')
    elif length == 1:
        return -first(args)
    else:
        return first(args) - reduce_linked_list(add, 0, rest(args))

def do_division(args):
    length = len_linked_list(args)
    if length == 0:
        raise TypeError('not enough arguments')
    elif length == 1:
        return 1 / first(args)
    else:
        return first(args) / reduce_linked_list(mul, 1, rest(args))

if __name__ == '__main__': # ALLOWS US TO DO 'python calc.py'
    repl()
