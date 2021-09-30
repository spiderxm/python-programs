# Python3 implementation to print 
# reverse wave form of matrix 
  
R = 4
C = 4
  
# function to print reverse wave  
# form for a given matrix 
def wavePrint(m, n, arr): 
    j = n - 1
    wave = 1
      
    # m     - Ending row index 
    # n     - Ending column index 
    # i, j     - Iterator 
    # wave     - for Direction 
    # wave = 1 - Wave direction down 
    # wave = 0 - Wave direction up  
    while j >= 0: 
          
        # Check whether to go in 
        # upward or downward 
        if wave == 1: 
      
            # Print the element of the  
            # matrix downward since the 
                        # value of wave = 1 
            for i in range(m): 
                print(arr[i][j], end = " "), 
            wave = 0
            j -= 1
              
              
        else: 
            # Print the elements of the  
            # matrix upward since the  
            # value of wave = 0 
            for i in range(m - 1, -1, -1): 
                print(arr[i][j], end = " "), 
                  
            wave = 1
            j -= 1
  
# Driver code 
arr = [ [ 1, 2, 3, 4 ], 
        [ 5, 6, 7, 8 ], 
        [ 9, 10, 11, 12 ], 
        [ 13, 14, 15, 16 ] ] 
          
wavePrint(R, C, arr) 
