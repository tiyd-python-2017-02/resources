class ShapeError(Exception):
    pass


class Vector:
    def __init__(self, data):
        """ This is a docstring...  you can think of it as a guide to how to use a function (or class)
        I like to see preconditions and postconditions (inputs/outputs, domain/range)
        """
        self.data = data

    @staticmethod
    def test_shapes(*args):
        if not all([isinstance(curr, Vector) for curr in args]):
            raise ValueError
        if not all([curr.shape() == args[0].shape() for curr in args]):
            raise ShapeError

    def shape(self):
        return (len(self.data),)

    def __eq__(self, other):
        return self.data == other.data

    def __add__(self, other):
        Vector.test_shapes(self, other)
        return Vector([sum(tup) for tup in zip(self.data, other.data)])

    def __sub__(self, other):
        Vector.test_shapes(self, other)
        return Vector([lhs - rhs for lhs, rhs in zip(self.data, other.data)])

    def __repr__(self):
        return repr(self.data)

    def __radd__(self, other):
        # you probably don't actually want to hack this to make it work...
        if type(other) == int and other == 0:
            return Vector(self.data)
        Vector.test_shapes(self, other)
        return Vector([sum(tup) for tup in zip(self.data, other.data)])

    def __mul__(self, other):
        if type(other) not in [int, float]:
            raise TypeError
        return Vector([a*other for a in self.data])

    def dot(self, other):
        Vector.test_shapes(self, other)
        return sum([a*b for a, b in zip(self.data, other.data)])

    def magnitude(self):
        return sum([a**2 for a in self.data])**.5
