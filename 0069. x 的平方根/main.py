class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        left, right = 1, x
        while left < right:
            mid = (left + right) // 2
            if (mid == left):
                return left

            s = mid*mid
            if (s < x):
                left = mid
            elif s > x:
                right = mid
            else:
                return mid

        # x = 0 的情况
        return right

s = Solution()
print(s.mySqrt(8))
