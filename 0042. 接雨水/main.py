class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        size = len(height)
        res = 0
        maxLeft = [0 for i in range(size)]
        maxRight = [0 for i in range(size)]
        maxLeft[0] = height[0]
        maxRight[size-1] = height[size-1]

        for i in range(1, size, 1):
            maxLeft[i] = max(height[i], maxLeft[i-1])
        for i in range(size-2, -1, -1):
            maxRight[i] = max(height[i], maxRight[i+1])

        for i in range(size):
            minHeight = min(maxLeft[i], maxRight[i])
            if minHeight > height[i]:
                res += minHeight - height[i]

        return res


s = Solution()
print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
