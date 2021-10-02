def pClosest(points, K):
 
    points.sort(key = lambda K: K[0]**2 + K[1]**2)
 
    return points[:K]
 
# Driver program
points = [[3, 3], [5, -1], [-2, 4]]
 
K = 2
 
print(pClosest(points, K))