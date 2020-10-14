# Python3 program to print stair case pattern. 

# Function definition 
def pattern(n): 

	# for loop for rows 
	for i in range(1, n + 1): 
		
		# conditional operator 
		k = i + 1 if (i % 2 != 0) else i 

		# according to value of k carry 
		# out further operation 
		for j in range(0, k): 
			if j == k - 1: 
				print(" * ") 
			else: 
				print(" * ", end = " ") 
			
# Driver code 
n = 6
pattern(n) 
