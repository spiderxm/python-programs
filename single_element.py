# The problem asks that given an array of integers where every element occurs twice except one. Find the element
# Solution: By using the property of XOR, we know that a XOR a = 0 and 0 XOR a = a, thus XOR of all the elements in the list would be equal to the number that only occurred once.
# Time Complexity: O(n)
# Space Complexity: O(1)

'''
Made by: Ansh Gupta(@ansh422)
Date: 02/10/2021
'''
def singleElement(arr):
    ans=0
    for num in arr:
        ans=ans^num
    
    return ans



if __name__ == "__main__":
    arr=list(map(int,input().split()))
    element=singleElement(arr)
    print('Element that occurred only once is', element)
