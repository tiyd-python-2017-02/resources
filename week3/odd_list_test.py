from odd_list import OddList

def test_create():
    ol = OddList([1, 3])

def test_append_item():
    ol = OddList([])
    ol.append(7)

def test_append_works():
    ol = OddList([1])
    ol.append(3)
    assert 3 in ol

def test_insert_item():
    ol = OddList([1,5])
    ol.insert(3,1)
    assert list(ol) == [1,3,5]

def test_index():
    ol = OddList([1,3])
    assert ol[0] == 1

def test_add_list():
    ol = OddList([1,3])
    ol2 = OddList([5,7])
    print(ol+ol2)
    print(OddList([1,3,5,7]))
    assert ol + ol2 == OddList([1,3,5,7])


