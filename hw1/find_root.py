# %%
# BEGIN SOLUTION
"""
Following **Test-First Design Steps**  
1. Inputs - what are arguments?  
A: A function f, a lower value L, a higher value H, a tolerance tol.

2. Outputs - what should be returned? 
A: The root of the function x.

# 3. Special cases
A: L ≠ H but tol is not << |L - H|.


# 4. Usual cases     
A: f(L)·f(H) < 0 and tol << |L - H|
"""

# 5. Develop a function signature (def + docstring)

def find_root(f, L, H, tol):
    """
    Finds a root of f
    """
    pass

# 6) Implement tests for each cases

def test_find_root():
	assert find_root(lambda x: x**2 - 1, -2, 2, 5) == 0, 'Too large tol failed'
	assert find_root(lambda x: x**2 , -2, 2, 0.01) == 0, ' Find root failed'
	pass
	
# 7) Implement function


def find_root(f, L, H, tol):
    """
    Finds a root of f
    """
    x = (L + H) / 2
    print(f"[{L},{H}] f({x}) = {f(x)}")
    while abs(L - H) > tol:
        x = (L + H) / 2
        if f(L) * f(x) < 0:
            H = x
        else:
            L = x
        print(f"[{L},{H}] f({x}) = {f(x)}")
    return x

# 8) add/improve tests as needed
# A: No additional tests needed

# END SOLUTION