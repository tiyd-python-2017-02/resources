from cache import Cache


def test_get_when_not_set_returns_none():
    c = Cache()
    assert c.get("foo") is None


def test_get_when_set_returns_value():
    c = Cache()
    c.set("foo", "bar")
    assert c.get("foo") == "bar"


def test_clear_empties_cache():
    c = Cache()
    c.set("foo", "bar")
    c.clear()
    assert c.get("foo") is None


def test_has_key_when_not_set_returns_false():
    c = Cache()
    assert not c.has_key("foo")


def test_has_key_when_set_returns_true():
    c = Cache()
    c.set("foo", "bar")
    assert c.has_key("foo")


def test_in_when_not_set_returns_false():
    c = Cache()
    assert "foo" not in c

#
def test_in_when_set_returns_true():
    c = Cache()
    c.set("foo", "bar")
    assert "foo" in c
#

def test_iteration():
    c = Cache()
    c.set("foo", "bar")
    c.set("baz", "quux")
    results = []
    for key, value in sorted(c):
        results.append("{}={}".format(key, value))
    result = ', '.join(results)
    assert result == "baz=quux, foo=bar"


def test_len():
    c = Cache()
    c.set("foo", "bar")
    c.set("baz", "quux")
    assert len(c) == 2
#
