
'''this is code to check if list contains zero in or not'''

def check(l):
    n=len(l)
    if(n==0):
        return 0
    if(l[0]==0):
        return 1
    else:
        return(check(l[1:n-1]))
    



l=[1,2,0,3,4,5]
print(check(l))
