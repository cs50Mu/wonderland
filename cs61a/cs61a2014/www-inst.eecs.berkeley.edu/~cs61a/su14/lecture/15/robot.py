class Robot:
    """A friendly robot that implements the string representation protocol."""
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Robot('{}')".format(self.name)

    def __str__(self):
        return 'Beep boop I am ' + self.name

