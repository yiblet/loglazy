from ..interp import Interp


def test_on_simple_functions():
    interp = Interp(lambda: 2)
    assert repr(interp) == "2"
    assert str(interp) == "2"

    interp = Interp(lambda: "string")
    assert repr(interp) == "'string'"
    assert str(interp) == "string"

    values = [2, "string", (4, 2), [3, 2, 1], {4}]
    for test_value in values:
        interp = Interp(lambda: test_value)
        assert repr(interp) == repr(test_value)
        assert str(interp) == str(test_value)


def test_on_complex_objects():
    values = [
        (4, 2), [3, 2, 4, 1], {4}, {
        2: 2,
        3: ""
    }, "", Interp, object, Exception,
              ValueError("231231"), ValueError]
    for test_value in values:
        interp = Interp(lambda: test_value)
        assert repr(interp) == repr(test_value)
        assert str(interp) == str(test_value)
