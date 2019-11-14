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
# 先将每个点的左边和右边算出来，而不是每次都遍历下
class Solution2(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        res = 0
        n = len(heights)
        left = [i for i in range(n)]
        right = [i for i in range(n)]

        for i in range(0, n):
            tmp = i
            while tmp > 0 and heights[tmp-1] >= heights[i]:
                tmp = left[tmp-1]
            left[i] = tmp
        for i in range(n-1, -1, -1):
            tmp = i
            while tmp < n-1 and heights[tmp+1] >= heights[i]:
                tmp = right[tmp+1]
            right[i] = tmp
            print("right", right)
        
        print(left, right)
        for i in range(n):
            res = max(res, heights[i]*(right[i]-left[i]+1))

        return res


s = Solution2()
print(s.largestRectangleArea([2, 3]))
