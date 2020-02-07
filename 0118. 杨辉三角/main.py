class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []

        for i in range(numRows):
            tmp = [1]
            for j in range(i):
                if j == i-1:
                    tmp.append(res[i-1][j])
                else:
                    tmp.append(res[i-1][j] + res[i-1][j+1])
            res.append(tmp)
        
        return res

s = Solution()
print(s.generate(5))
