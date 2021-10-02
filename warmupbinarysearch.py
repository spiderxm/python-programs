
''' if the element x is present in a list l'''

def obvious_search(l,k):
    for x in l:
        if(x==k):
            return 1
    return 0 
    '''this is verified way of searching'''


def binary_search(l,k):
    '''this is alternative to obvious search this does same 
    work as in ovbious_search but in an efficient way . this is also known as 
    binary search'''
    begin=0 #! first element in l. l[0]
    end=len(l)-1 #!the last element in l is in len(l). l[lem(l)-1]
    #! we will use while loop to half the list
    while(end-begin>1):
        mid=(begin+end)//2
        if(l[mid]==k):
            return 1
        


        if(l[mid]>k):
            end=mid-1

        if(l[mid]<k):
            begin=mid-1

#! if there is only two element is length 
    if(l[begin]==k)or(l[end]==k):
        return 1
    else:
        return 0

        