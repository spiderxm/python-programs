# Python 3 program to check if the characters in the given string forms a Palindrome in O(1) extra space 

# Utilty function to get the position of first character in the string 
def firstPos(str, start, end): 

	firstChar = -1

	# Get the position of first character in the string 
	for i in range(start, end + 1): 
		if (str[i] >= 'a' and str[i] <= 'z') : 
			firstChar = i 
			break

	return firstChar 

# Utilty function to get the position of last character in the string 
def lastPos(str, start, end): 

	lastChar = -1

	# Get the position of last character in the string 
	for i in range(start, end - 1, -1) : 
		if (str[i] >= 'a' and str[i] <= 'z') : 
			lastChar = i 
			break

	return lastChar 

# Function to check if the characters in the given string forms a Palindrome in O(1) extra space 
def isPalindrome(str): 

	firstChar = 0
	lastChar = len(str) - 1
	ch = True

	for i in range(len(str)) : 
		firstChar = firstPos(str, firstChar, lastChar); 
		lastChar = lastPos(str, lastChar, firstChar); 

		# break, when all letters are checked 
		if (lastChar < 0 or firstChar < 0): 
			break
		if (str[firstChar] == str[lastChar]): 
			firstChar += 1
			lastChar -= 1
			continue

		# if mismatch found, break the loop 
		ch = False
		break

	return (ch) 

# Driver code 
if __name__ == "__main__": 
	
	str = "m	 a 343 la y a l am"
	if (isPalindrome(str)): 
		print("YES") 
	else: 
		print("NO") 
