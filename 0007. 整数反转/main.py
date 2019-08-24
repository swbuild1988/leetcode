class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = 0
        dir = 1 if x >= 0 else -1
        x = x if x >= 0 else (x * -1)
        while (x != 0):
            y = y * 10 + x % 10 * dir
            x = x // 10

            if (y < -2147483648 or y > 2147483647):
                return 0
        return y


s = Solution()
print(s.reverse(-120))
