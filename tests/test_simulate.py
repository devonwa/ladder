"""Tests for the simulate module."""
import pytest

import ladder.function as fn
import ladder.simulate as sim


def test_scan_function_continue_scan():
    assert sim.scan_function(fn.If, (True,), ())
    assert not sim.scan_function(fn.If, (False,), ())
    assert sim.scan_function(fn.Set, (), (True,))
    with pytest.raises(TypeError):
        assert sim.scan_function(fn.Set, (True,), (True,))
    with pytest.raises(TypeError):
        assert sim.scan_function(fn.Set, (), (True, False))
    
