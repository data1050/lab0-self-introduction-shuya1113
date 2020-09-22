# %%
# BEGIN SOLUTION
"""
Following **Test-First Design Steps**  
1. Inputs - what are arguments?  
A: One number n which indicates how many numbers we need to sum up.

2. Outputs - what should be returned? 
A: The sum of 1 to n.

# 3. Special cases
A: n=0. sum_first_n_rec(0)=0.

# 4. Usual cases     
A: n>=1 and n is integer.
examples: sum_first_n_rec(10)=21
"""

# 5. Develop a function signature (def + docstring)

def sum_first_n_rec(n):
    """
    Returns 1+2+3+...+n
    """
    pass

 # 6) Implement tests for each cases

 def test_first_n_rec():
 	assert sum_first_n_rec(0) == 0, 'n=0 test failed!'
 	assert sum_first_n_rec(2) == 3, 'n>=1 test failed!'

 # 7) Implement function


def sum_first_n_rec(n):
    ''' Returns 1+2+3+...+n'''
	if type(n) != int:
    	raise TypeError('n is not an integer!')
    if n < 0:
    	raise ValueError('n is non-positive!')
    if n == 0:
    	return 0
    else:
    	return sum(i for i in range(n+1))

# 8) add/improve tests as needed
# A: No additional tests needed

# END SOLUTION
