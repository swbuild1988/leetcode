class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.strip()
        n = len(s)
        for i in range(n-1, -1, -1):
            print(s[i])
            if (s[i] == ' '):
                return n-1-i
        return n
            
s = Solution()
print(s.lengthOfLastWord("Hello World  "))
