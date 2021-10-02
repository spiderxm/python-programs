'''code for recursuve binary search '''


def rbinarysearch(l, k, begin, end):

    if(begin == end):
        if(l[begin] == k):
            return 1
        else:
            return 0
    if(end-begin == 1):
        if(l[end] == k) or (l[begin] == k):
            return 1
        else:
            return 0

    if(end-begin > 1):
        mid = (end+begin)//2
        if(l[mid] > k):
            end = mid-1
        if(l[mid] < k):
            begin = mid+1
        if(l[mid] == k):
            return 1
    if(end-begin < 0):
        return 0

    return rbinarysearch(l, k, begin, end)


print(rbinarysearch([1,2,3,4,5], -1, 0,4))
