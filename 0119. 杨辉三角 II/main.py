class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = []

        for i in range(rowIndex):
            for j in range(i):
                if j == i-1:
                    res[j] = 1
                else:
                    res[j] = res[j] + res[j+1]
            res = [1] + res
        
        return res

s = Solution()
print(s.getRow(6))
