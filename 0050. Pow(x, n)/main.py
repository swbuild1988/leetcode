class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        def solve(x, n):

            res = 1
            while n:
                print(n, res)
                if n & 1:
                    res = res * x
                n >>= 1
                x *= x

            return res

        if n == 0:
            return 1
        elif n > 0:
            return solve(x, n)
        else:
            return 1 / solve(x, -n)


s = Solution()
print(s.myPow(2.00000, 9))
