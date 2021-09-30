# Python3 program to implement
# the above approach

# Stores the sorted
# array elements
temp = [0] * 100000

# Function to count the number of
# swaps required to merge two sorted
# subarray in a sorted form
def merge(A, left, mid, right):
	
	# Stores the count of swaps
	swaps = 0

	i, j, k = left, mid, left
	
	while (i < mid and j <= right):
		
		if (A[i] <= A[j]):
			temp[k] = A[i]
			k, i = k + 1, i + 1
		else:
			temp[k] = A[j]
			k, j = k + 1, j + 1
			swaps += mid - i

	while (i < mid):
		temp[k] = A[i]
		k, i = k + 1, i + 1

	while (j <= right):
		temp[k] = A[j]
		k, j = k + 1, j + 1

	while (left <= right):
		A[left] = temp[left]
		left += 1

	return swaps

# Function to count the total number
# of swaps required to sort the array
def mergeInsertionSwap(A, left, right):
	
	# Stores the total count
	# of swaps required
	swaps = 0
	
	if (left < right):

		# Find the middle index
		# splitting the two halves
		mid = left + (right - left) // 2

		# Count the number of swaps
		# required to sort the left subarray
		swaps += mergeInsertionSwap(A, left, mid)

		# Count the number of swaps
		# required to sort the right subarray
		swaps += mergeInsertionSwap(A, mid + 1, right)

		# Count the number of swaps required
		# to sort the two sorted subarrays
		swaps += merge(A, left, mid + 1, right)

	return swaps

# Driver Code
if __name__ == '__main__':
	
	A = [ 2, 1, 3, 1, 2 ]
	N = len(A)
	
	print (mergeInsertionSwap(A, 0, N - 1))

# This code is contributed by mohit kumar 29
