import operator

from jboc import collect, composed, squeeze


def test_composed():
    @composed(dict)
    def f(n):
        for i in range(n):
            yield i, i + 1

    assert f(4) == {0: 1, 1: 2, 2: 3, 3: 4}

    @composed(', '.join)
    def g(n):
        for i in range(n):
            yield str(i)

    assert g(3) == '0, 1, 2'

    # additional args
    @composed(operator.add, 1)
    def h():
        return 2

    assert h() == 3

    @composed(pow, 2)
    def p():
        return 5

    assert p() == 25


def test_collect():
    @collect
    def f(n):
        for i in range(n):
            if i != 3:
                yield i ** 2

    assert f(5) == [0, 1, 4, 16]


def test_squeeze():
    assert squeeze([]) == []
    assert squeeze([1]) == 1
    assert squeeze([1, 2]) == [1, 2]
