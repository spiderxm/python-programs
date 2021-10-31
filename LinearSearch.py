def linearsearch(listl, n, target):
    for i in range (0,n):
      if(list[i]==target):
        return i
      return -1
    
list1 = [1 ,3, 5, 4, 7, 9]  
key = 7 

n=len(list1)
res = linearsearch(list1,n,key)

if(res==-1):
  print("Element not found")
else:
  print("Element is found at index"+res)
