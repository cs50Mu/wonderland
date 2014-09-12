# Demo for length and indexing (element selection)
[1, 2, 3, 4]
len([1, 2, 3, 4])
colors = ['red', 'green', 'blue']
colors
len(colors)
colors[0]
colors[1]
colors[2]
colors[3]
colors[-1]
colors[-2]
colors[2 - 5]
colors[-4]
colors[-1 % 3]
colors[-2 % 3]
colors[-3 % 3]
colors + ['yellow', 'purple']
colors
colors = colors + ['yellow']
colors += ['purple']
# End of demo for length and indexing (element selection)
# Demo for slicing
colors[1:4]
colors[1:2]
colors[:3]
colors[3:]
colors[:]
colors[0:5]
colors[0:5:2]
colors[1:5:2]
colors[::3]
colors[::-1]
# End of demo for slicing
# Demo for membership
'red' in colors
'yellow' in colors
'purple' not in colors
'green' not in colors
if 'red' in colors and 'green' in colors:
    print('ahh! color blindness!')
# End of demo for membership
# Demo for ranges
range(3, 10)
x = range(3, 10)
list(x)
x
len(x)
x[0]
x[4]
x[6]
x[7]
x[-3]
5 in x
5.5 in x
list(range(5))
list(range(1, 10, 3))
# End of demo for ranges
# For statements
lst = [5, 1, 6, 8]
for item in lst:
    new_value = item + 3
    print(new_value)
for i in range(len(lst)):
    element = lst[i]
    print(element + i)
# End of For Statements
# List Comprehensions
[item + 1 for item in lst]
[item + 1 for item in lst if item % 2 == 0]
lst = [5, 0, 3, 8, 2, 3]
[item for item in lst if item]
# End of List Comprehensions
# Strings
'hello world'[5]
len('hello world')
# End of Strings
# Cool Demo
from urllib.request import urlopen
shakespeare = urlopen('http://composingprograms.com/shakespeare.txt')
words = list(shakespeare.read().decode().split())
len(words)
words.count(',')
words.count('the')
starting_letters = [word[0] for word in words]
starting_letters.count('a')
starting_letters.count('t')
words.count('t')
palindromes = [word for word in words if word[::-1] == word and len(word) > 4]
palindromes # NOOO
seen_so_far = []
for word in palindromes:
     if word not in seen_so_far:
             seen_so_far += [ word ]
             print(word)
