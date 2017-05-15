"""Simulate is used to execute ladder projects.

This module provide functions for being able to scan through a project
and execute functions while updating the variable table.
"""

def simulate():
    """Continuously run the given project."""
    pass


def scan_project():
    """Scan and execute programs in a project."""
    pass


def scan_program():
    """Scan and execute rungs in a program."""
    pass


def scan_rung():
    """Scan and execute functions in a rung.

    Return the value of energized if the last item in the rung was still
    energized. By doing so, we can see if a subrung is energized.
    """
    energized = True
    return energized


def scan_function(func, invars, outvars, energized=True, update_vars=True):
    """Scan a function to see if it continues."""
    correct_var_count(func, invars, outvars)
    if outvars:
        func_output = update_function(func, invars, energized)
        if update_vars and False:
            update_variable(outvars, func_output)

    return func.continue_scan(*invars)


def correct_var_count(func, invars, outvars):
    """Given variables match the number of function variables.

    Throw an error if the function is expecting a different number
    of input and output variables than are being provided.
    """
    invalid = None
    if len(invars) != len(func.invars):
        invalid = "input", len(func.invars), len(invars)
    if len(outvars) != len(func.outvars):
        invalid = "output", len(func.outvars), len(outvars)
    if invalid is not None:
        msg = (
            "Invalid number of {1} variables for Function '{0}'. "
            "Required: {2}. Given: {3}.").format(
                str(func), *invalid)
        raise TypeError(msg)
    return True


def update_function(func, invars, energized):
    """Return the output of the a Function's update method."""
    return func.update(*invars, energized=energized)


def update_variable(_outvars, _values):
    """Update the variable to the new value in the variable table."""
    pass


if __name__ == "__main__":
    print("ladder/simulator.py")
