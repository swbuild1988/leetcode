class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        if n == 0:
            return 0

        heights = [0 for _ in range(n)]
        res = 0
        for i in range(m):
            # 计算好所有的heights
            for j in range(n):
                print(i, j, heights)
                heights[j] = 0
                if matrix[i][j] == "1":
                    index = 0
                    while i-index >= 0 and matrix[i-index][j] == "1":
                        index+=1
                    heights[j] = index
                
            # 利用前一道题的方法，求最大面积
            res = max(res, self.largestRectangleArea(heights))

        return res


    
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        heights2 = [0] + heights + [0]
        stack = []
        res = 0

        for i in range(len(heights2)):
            while stack and heights2[stack[-1]] > heights2[i]:
                tmp = stack.pop()
                res = max(res, heights2[tmp] * (i-stack[-1]-1))
            stack.append(i)

        return res

        

s = Solution()
print(s.maximalRectangle([["1"],["0"],["1"],["1"],["1"],["1"],["0"]]))
