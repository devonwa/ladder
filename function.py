"""Definititions for all base functions in ladder."""
from enum import Enum


class UpdateType(Enum):
    """Specify when the variables in a function should be updated."""
    ENERGIZED = 0     # Rung scan is true at function
    ON_SCAN_ALL = 1   # Rung scan may be false at function
    # TIMED = 2         # Update after a specified time has passed or on scan
    # RUNG_COUNT = 3    # Update after a specified number of rungs or on scan


class MetaFunction(type):
    """Metaclass for read-only properties of functions."""
    @property
    def update_type(cls):
        """When the function should update its variables."""
        return cls._update_type


class Function(metaclass=MetaFunction):
    """Base class for all functions."""
    _update_type = UpdateType.ENERGIZED
    invars = ()
    outvars = ()

    @staticmethod
    def continue_scan():
        """Determine if rung continues scanning."""
        return True

    @staticmethod
    def update(*args, energized=True):
        """Perform the function of the function."""
        pass


class If(Function):
    """Check if variable is True."""
    invars = (bool,)

    @staticmethod
    def continue_scan(var):
        """Continue scan if a variable is True."""
        return bool(var)


class IfNot(Function):
    """Check if variable is False."""
    invars = (bool,)

    @staticmethod
    def continue_scan(var):
        """Continue scan if a variable is False."""
        return not bool(var)


class Set(Function):
    """Set output variable to scan connection."""
    _update_type = UpdateType.ON_SCAN_ALL
    outvars = (bool,)

    @staticmethod
    def update(energized=True):
        """Return status of rung scan."""
        return bool(energized)


class Latch(Function):
    """Set output variable to True/False."""
    invars = (bool,)
    outvars = (bool,)

    @staticmethod
    def update(truth, energized=True):
        """Return the given bool to set to the output variable.

        Args:
            truth (bool): Outvars will be set as this value.
        """
        return bool(truth)


if __name__ == "__main__":
    print("Function.py")
