class Solution(object):
   def hammingDistance(self, x, y):
      """
      :type x: int
      :type y: int
      :rtype: int
      """
      ans = 0
      for i in range(31,-1,-1):
         b1= x>>i&1
         b2 = y>>i&1
         ans+= not(b1==b2)
         #if not(b1==b2):
            # print(b1,b2,i)
      return ans
ob1 = Solution()
print(ob1.hammingDistance(7, 15))
