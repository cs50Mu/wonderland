from ucb import main, trace

# Question Node ADT

# Constructor
# question must be a string representing a yes/no question.
# yes_node and no_node are either question nodes or strings
def make_node(question, yes_node, no_node):
    return [question, yes_node, no_node]

# Selectors
def get_question(node):
    return node[0]

def get_yes_node(node):
    return node[1]

def get_no_node(node):
    return node[2]

# Mutators
def set_yes_node(node, new_node):
    node[1] = new_node

def set_no_node(node, new_node):
    node[2] = new_node


animals = make_node('Does it have wings?', 'penguin', 'panda')

def yorn():
    while True:
        answer = input('Answer yes or no: ')
        if answer and answer[0] == 'y':
            return True
        elif answer and answer[0] == 'n':
            return False
        else:
            print('Invalid answer')

def add_new_node(parent_node, which_child, animal1, animal2):
    print('What question can distinguish between', animal1, 'and', animal2 + '?')
    question = input('')
    print('Is the answer to the question yes for', animal1 + '?')
    if yorn():
        yes_animal, no_animal = animal1, animal2
    else:
        yes_animal, no_animal = animal2, animal1

    if which_child:
        set_yes_node(parent_node, make_node(question, yes_animal, no_animal))
    else:
        set_no_node(parent_node, make_node(question, yes_animal, no_animal))

@main
def play_game():
    print("Think of an animal, and I'll try to guess it.")
    curr_node, prev_node = animals, None
    while type(curr_node) != str:
        print(get_question(curr_node))
        prev_node = curr_node
        choice = yorn()
        if choice:
            curr_node = get_yes_node(curr_node)
        else:
            curr_node = get_no_node(curr_node)

    # At this point, curr_node is a string representing an animal
    print('Is', curr_node, 'your animal?')
    if yorn():
        print('Yay!  I win!')
    else:
        print('What was your animal?')
        new_animal = input('')
        add_new_node(prev_node, choice, curr_node, new_animal)
