# %%
# BEGIN SOLUTION
"""
Following **Test-First Design Steps**  
1. Inputs - what are arguments?  
A: One string called st.

2. Outputs - what should be returned? 
A: A boolean. i.e. True if the string is a palindrome, False if the string is not a palindrome.

# 3. Special cases
A: An empty string. i.e. is_palindrome('') == True
   A single string. i.e. is_palindrome('a') == True

# 4. Usual cases     
A: A string that is palindrome. i.e. 'racecar'
   A string that is not palindrome. i.e. 'apple'
"""

# 5. Develop a function signature (def + docstring)


def is_palindrome(st):
	'''
	This function takes a single string as the argument and return a Boolean
	to identify whether the input is a palindrome.
	'''
	pass

# 6) Implement tests for each cases

def test_is_palindrome():
	assert is_palindrome('') == True, 'Empty string test failed!'
	assert is_palindrome('a') == True, 'Single string test failed!'
	assert is_palindrome('racecar') == True, 'Palindrome test failed!'
	assert is_palindrome('apple') == False, 'Not palindrome test failed!'

# 7) Implement function

def is_palindrome(st):
	if len(st) == 0 or len(st) == 1:
		return True
	else:
		return st == st[::-1]

# 8) add/improve tests as needed
# A: No additional tests needed

# END SOLUTION