# List based implementation of Tree

def tree(x, y=[]):
    return [x, y]

def datum(t):
    return t[0]

def children(t):
    return t[1]

berkeley_tree = tree('Berkeley')
ca_tree = tree('CA', [ tree('LA'), berkeley_tree ])
usa_tree = tree('USA', [ ca_tree, tree('CO') ])
mh_tree = tree('MH', [ tree('Mumbai'), tree('Pune') ])
india_tree = tree('India', [ mh_tree ])
world_tree = tree('World', [ usa_tree, india_tree ])

def explore_tree(tree, fn, level=0):
    fn(datum(tree), level)
    for subtree in children(tree):
        explore_tree(subtree, fn, level+1)

def print_tree(tree):
    explore_tree(tree, lambda datum, level: print('  ' * level + str(datum)))
