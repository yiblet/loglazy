from ..interp import Interp


def test_on_simple_functions():
    interp = Interp(lambda: 2)
    assert repr(interp) == "2"
    assert str(interp) == "2"
