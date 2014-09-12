
## Commented out so that the entire file doesn't error
# ValueError('Andrew made a ValueError')

## Break the program by raising the actual error
# raise ValueError('Andrew made a ValueError')

while True:
  try:
    x = int(input('Type in an Integer: '))
    print(x+10)
  except ValueError:
    print('Not a valid integer! :(')
