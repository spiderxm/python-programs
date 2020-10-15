class Solution(object):
   def isAnagram(self, s, t):
      """
      :type s: str
      :type t: str
      :rtype: bool
      """
      return "".join(sorted(s)) == "".join(sorted(t))
ob1 = Solution()
print(ob1.isAnagram("ANAGRAM","NAAGARM"))
