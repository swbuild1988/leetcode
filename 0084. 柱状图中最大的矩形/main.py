# 暴力搜索，时间复杂度n^2，最后超时
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        res = 0
        for i in range(len(heights)):
            left, right = i, i
            while left > 0 and heights[left-1] >= heights[i]:
                left -= 1
            while right < len(heights)-1 and heights[right+1] >= heights[i]:
                right += 1
            
            res = max(res, heights[i]*(right-left+1))
        
        return res

# 优化暴力法
class Solution2(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """


s = Solution()
print(s.largestRectangleArea([2, 1, 5, 6, 2, 3]))
