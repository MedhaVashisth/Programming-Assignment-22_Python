#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Python3 code to find sum of all
# divisor of number up to 'n'

# Utility function to find sum of
# all divisor of number up to 'n'
def divisorSum( n ):
	sum = 0
	
	for i in range(1, n + 1):
		
		# Find all divisors of i
		# and add them
		j = 1
		while j * j <= i:
			if i % j == 0:
				if i / j == j:
					sum += j
				else:
					sum += j + i / j
			j = j + 1
	return int(sum)

# Driver code
n = 4
print( divisorSum(n))
n = 5
print( divisorSum(n))



# In[3]:


def common_data(list1, list2):
     result = False
     for x in list1:
         for y in list2:
             if x == y:
                 result = True
                 return result
print(common_data([1,2,3,4,5], [5,6,7,8,9]))
print(common_data([1,2,3,4,5], [6,7,8,9]))


# In[10]:


# Python 3 program to find the string which
# contain the first character of each word
# of another string.

# Function to find string which has first
# character of each word.
def firstLetterWord(str):

	result = ""

	# Traverse the string.
	v = True
	for i in range(len(str)):
		
		# If it is space, set v as true.
		if (str[i] == ' '):
			v = True

		# Else check if v is true or not.
		# If true, copy character in output
		# string and set v as false.
		elif (str[i] != ' ' and v == True):
			result += (str[i])
			v = False

	return result

# Driver Code
if __name__ == "__main__":
	
	str = "geeks for geeks"
	print(firstLetterWord(str))


# In[6]:


# Python program to check
# if a word is isogram or not


def is_isogram(word):

	# Convert the word or sentence in lower case letters.
	clean_word = word.lower()

	# Make an empty list to append unique letters
	letter_list = []

	for letter in clean_word:

		# If letter is an alphabet then only check
		if letter.isalpha():
			if letter in letter_list:
				return False
			letter_list.append(letter)

	return True

# Driver code
if __name__ == '__main__':

	# Function call
	print(is_isogram("Machine"))
	print(is_isogram("isogram"))
	print(is_isogram("GeeksforGeeks"))
	print(is_isogram("Alphabet "))


# In[8]:


# Python 3 implementation of above approach

# Function that checks whether
# the string is in alphabetical
# order or not
def isAlphabaticOrder(s):
	
	# length of the string
	n = len(s)

	# create a character array
	# of the length of the string
	c = [s[i] for i in range(len(s))]

	# sort the character array
	c.sort(reverse = False)

	# check if the character array
	# is equal to the string or not
	for i in range(n):
		if (c[i] != s[i]):
			return False
		
	return True

# Driver code
if __name__ == '__main__':
	s = "aabbbcc"

	# check whether the string is
	# in alphabetical order or not
	if (isAlphabaticOrder(s)):
		print("Yes")
	else:
		print("No")



# In[ ]:




