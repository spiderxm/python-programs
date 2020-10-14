def printPascal(n):
    for line in range(1,n+1): 
        D = 1
        for i in range(1,line+1): 
            print D,
            D = D * (line - i) / i 
        print "\n"

#main() 
n = 5
printPascal(n)
