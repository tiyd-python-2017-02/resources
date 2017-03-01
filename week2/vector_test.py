from nose.tools import raises
from vector import Vector, ShapeError


def are_equal(x, y, tolerance=0.001):
    """Helper function to compare floats, which are often not quite equal."""
    return abs(x - y) <= tolerance


m = Vector([3, 4])
n = Vector([5, 0])

v = Vector([1, 3, 0])
w = Vector([0, 2, 4])
u = Vector([1, 1, 1])
y = Vector([10, 20, 30])
z = Vector([0, 0, 0])


def test_shape_vectors():
    """shape takes a vector or matrix and return a tuple with the
    number of rows (for a vector) or the number of rows and columns
    (for a matrix.)"""
    assert Vector([1]).shape() == (1,)
    assert m.shape() == (2,)
    assert v.shape() == (3,)


def test_vectors_eq():
    assert Vector([2, 3, 4]) == Vector([2, 3, 4])
    assert Vector([4, 3, 4]) != Vector([2, 3, 4])
    assert Vector([4, 3, 4]) != Vector([2, 3, 4, 5, 6])
    v + 5


def test_vector_add():
    """
    [a b]  + [c d]  = [a+c b+d]
    Matrix + Matrix = Matrix
    """
    assert v + w == Vector([1, 5, 4])
    assert u + y == Vector([11, 21, 31])
    assert u + z == u


def test_vector_add_is_commutative():
    assert w + y == y + w


@raises(ShapeError)
def test_vector_add_checks_shapes():
    """Shape rule: the vectors must be the same size."""
    m + v


def test_vector_sub():
    """
    [a b]  - [c d]  = [a-c b-d]
    Matrix + Matrix = Matrix
    """
    assert v - w == Vector([1, 1, -4])
    assert w - v == Vector([-1, -1, 4])
    assert y - z == y
    assert w - u == z - (u - w)


@raises(ShapeError)
def test_vector_sub_checks_shapes():
    """Shape rule: the vectors must be the same size."""
    m - v


def test_vector_sum():
    """vector_sum can take any number of vectors and add them together."""
    assert v + w + u + y + z == Vector([12, 26, 35])
#   you probably don't actually want to hack this to make it work...
    assert sum([v, w, u, y, z]) == Vector([12, 26, 35])


def test_dot():
    """
    dot([a b], [c d])   = a * c + b * d
    dot(Vector, Vector) = Scalar
    """
    assert w.dot(y) == 160
    assert m.dot(n) == 15
    assert u.dot(z) == 0


@raises(ShapeError)
def test_dot_checks_shapes():
    """Shape rule: the vectors must be the same size."""
    v.dot(m)


def test_vector_multiply():
    """
    [a b]  *  Z     = [a*Z b*Z]
    Vector * Scalar = Vector
    """
    assert v * 0.5 == Vector([0.5, 1.5, 0])
    assert m * 2 == Vector([6, 8])



def test_magnitude():
    """
    magnitude([a b])  = sqrt(a^2 + b^2)
    magnitude(Vector) = Scalar
    """
    assert m.magnitude() == 5
    assert v.magnitude() == 10**.5
    assert y.magnitude() == 1400**.5
    assert z.magnitude() == 0
