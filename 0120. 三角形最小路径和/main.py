class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        res = []

        for i in range(n):
            if i == 0:
                res = [triangle[i][0]]
            else:
                for j in range(i+1):
                    if j == 0:
                        res = [triangle[i][0] + res[0]] + res
                    elif j == i:
                        res[j] = triangle[i][j] + res[j]
                    else:
                        res[j] = triangle[i][j] + min(res[j], res[j+1])
                    
        return min(res)


s = Solution()
print(s.minimumTotal([
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]))
