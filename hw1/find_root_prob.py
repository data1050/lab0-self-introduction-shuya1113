# This is a stencil file, make a COPY without the _prob suffix
# and create your solution there.  That way you can refer back
# to this file without the need to figure how to get it off 
# git while not destroying your work. 

import math
import pytest

#%% [markdown]
""" ### Task hw1.4.1
Use a variant of Test-First Design to figure out what's wrong with this 
function and fix it. Add all your test cases to the function below that 
`pytest` will use.
"""

""" TFD Steps 
1. Inputs
2. Outputs
3. Special Cases
4. Usual Cases
5. Function Specification
6. Implement Test Cases
7. Implement the Function
8. Add/improve/fix test cases and function as needed
"""

def find_root(f, L, H, tol):
    """
    Finds a root of f
    """
    x = (L + H) / 2
    print(f"[{L},{H}] f({x}) = {f(x)}")
    while abs(L - H) > tol:
        x = (L + H) / 2
        if f(L) * f(H) < 0:
            H = x
        else:
            L = x
        print(f"[{L},{H}] f({x}) = {f(x)}")
    return x


""" 
TODO: Remember to add test cases below, and run them with Pytest
"""
def test_find_root():
    pass # remove this when you're ready to start coding your test cases

#%% [markdown]
""" Task hw1.4.2
In in a numbered list, describe each of the problems you found with the current
implementation. Provide example inputs that reproduce each one.

1.
"""

# %%
