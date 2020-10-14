# Python3 program to remove consecutive duplicates from a given string. 

# A iterative function that removes consecutive duplicates from string S 

def removeDuplicates(S): 
		
	n = len(S) 
	
	# We don't need to do anything for empty or single character string. 
	if (n < 2) : 
		return
		
	# j is used to store index is result string (or index of current distinct character) 
	j = 0
	
	# Traversing string 
	for i in range(n): 
		
		# If current character S[i] is different from S[j] 
		if (S[j] != S[i]): 
			j += 1
			S[j] = S[i] 
	
	# Putting string termination character. 
	j += 1
	S = S[:j] 
	return S 
	
# Driver Code 
if __name__ == '__main__': 
		
	S1 = "Solluttions"
	S1 = list(S1.rstrip()) 
	S1 = removeDuplicates(S1) 
	print(*S1, sep = "") 
		
	S2 = "aabccadseeefff"
	S2 = list(S2.rstrip()) 
	S2 = removeDuplicates(S2) 
	print(*S2, sep = "") 
