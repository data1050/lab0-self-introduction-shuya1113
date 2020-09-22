# %%
# BEGIN SOLUTION
"""
Following **Test-First Design Steps**  
1. Inputs - what are arguments?  
A: An single array A with integers.

2. Outputs - what should be returned? 
A: The maximum element in the array A.

# 3. Special cases
A: An array with no element.
   An array with only one element.
   An array with all same elements.

# 4. Usual cases     
A: An array with several integers as elements.
"""

# 5. Develop a function signature (def + docstring)

def find_max_element(A):
	'''
	This function takes an array A as a single argument
	and return the maximum element in A
	'''
	pass

# 6) Implement tests for each cases

def test_find_max_element():
	assert find_max_element([]) == 0, 'Empty array test failed!'
	assert find_max_element([1]) == 1, 'Single element array test failed!'
	assert find_max_element([1,1,1,1,1]) == 1, 'All same elements array test failed!'
	assert find_max_element([1,2,3,4,5]) == 5, 'Maximum element test failed!'


# 7) Implement function

def find_max_element(A):
	if A == []:
		return 0
	elif len(A) == 1:
		return A[0]
	else:
		if A[0] > find_max_element(A[1:]):
			return A[0]
		else:
			return find_max_element(A[1:])

# 8) add/improve tests as needed
# A: No additional tests needed

# END SOLUTION
