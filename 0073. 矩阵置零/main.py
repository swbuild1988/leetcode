class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        x = len(matrix)
        y = len(matrix[0])

        for i in range(x):
            for j in range(y):
                if matrix[i][j] == 0:
                    for k in range(x):
                        if matrix[k][j] != 0:
                            matrix[k][j] = True
                    for k in range(y):
                        if matrix[i][k] != 0:
                            matrix[i][k] = True
        
        for i in range(x):
            for j in range(y):
                if isinstance(matrix[i][j], bool):
                    matrix[i][j] = 0
        print(matrix)


s = Solution()
print(s.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
