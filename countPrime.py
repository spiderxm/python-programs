class Solution(object):
   def countPrimes(self, n):
      """
      :type n: int
      :rtype: int
      """
      count = 0
      primes = [False for i in range(n+1)]
      for i in range(2,n):
         if primes[i] == False:
            count+=1
            j = 2
            while j*i<n:
               primes[j*i] = True
               j+=1
      return count
ob1 = Solution()
print(ob1.countPrimes(50))
print(ob1.countPrimes(10))
