class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        a, res = 1, 1
        for i in range(2, n+1):
            tmp = res
            res = res + a
            a = tmp
        
        return res

s = Solution()
print(s.climbStairs(1))
