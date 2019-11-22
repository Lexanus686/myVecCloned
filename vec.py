class Point:
    def __init__(self, *args):
        self.values = args

    def __add__(self, other):
        return self.values + other.values

    def __sub__(self, other):
        return (self.values - other.values)

Point c = Point(2,5)

class Vec:
    def __init__(self, *args):
        self.values = args