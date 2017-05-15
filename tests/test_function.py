"""Test of the base ladder functions and interface."""
import pytest

import ladder.function as fn


def test_Function():
    """Test read-only parameters of the Function base class."""
    assert fn.Function.update_type == fn.UpdateType.ENERGIZED
    with pytest.raises(AttributeError):
        fn.Function.update_type = fn.UpdateType.ENERGIZED


def test_Function_continue_scan():
    """Test the continue_scan method of the Function base class."""
    assert fn.Function.continue_scan()


def test_Function_update():
    """Test the update method of the Function base class."""
    assert fn.Function.update() is None
    assert fn.Function.update(None) is None
    assert fn.Function.update(True) is None


def test_If_continue_scan():
    """Test the continue_scan method of the If function."""
    assert fn.If.continue_scan(True)
    assert not fn.If.continue_scan(False)
    assert fn.If.continue_scan((True))
    assert not fn.If.continue_scan(())
    assert not fn.If.continue_scan(None)
    assert not fn.If.continue_scan("")
    assert fn.If.continue_scan("abcd")
    assert not fn.If.continue_scan(0)
    assert fn.If.continue_scan(1)


def test_IfNot_continue_scan():
    """Test the continue_scan method of the IfNot function."""
    assert not fn.IfNot.continue_scan(True)
    assert fn.IfNot.continue_scan(False)
    assert not fn.IfNot.continue_scan((True))
    assert fn.IfNot.continue_scan(())
    assert fn.IfNot.continue_scan(None)
    assert fn.IfNot.continue_scan("")
    assert not fn.IfNot.continue_scan("abcd")
    assert fn.IfNot.continue_scan(0)
    assert not fn.IfNot.continue_scan(1)


def test_Set_update():
    """Test the update method of the Set function."""
    assert fn.Set.update(True)
    assert not fn.Set.update(False)

    test_var = 0
    test_var = type(test_var)(fn.Set.update(energized=True))
    assert test_var

    test_var = 1
    test_var = type(test_var)(fn.Set.update(energized=False))
    assert not test_var


def test_Latch_update():
    """Test the update method of the Latch function."""
    assert fn.Latch.update(True)
    assert not fn.Latch.update(False)

    test_var = 0
    test_var = type(test_var)(fn.Latch.update(True))
    assert test_var

    test_var = 1
    test_var = type(test_var)(fn.Latch.update(False))
    assert not test_var


if __name__ == "__main__":
    pytest.main()
