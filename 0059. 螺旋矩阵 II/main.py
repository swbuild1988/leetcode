class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        res = [[0 for _ in range(n)] for _ in range(n)]
        index, i, j, dir_x, dir_y = 0, 0, 0, 1, 0

        while index < n*n:
            index += 1
            res[i][j] = index

            # x 方向移动
            if dir_x != 0:
                if (j+dir_x >= 0 and j+dir_x < n and res[i][j+dir_x] == 0):
                    j += dir_x
                else:
                    dir_y = dir_x
                    dir_x = 0
                    i += dir_y
            else:
                if (i+dir_y >=0 and i+dir_y < n and res[i+dir_y][j] == 0):
                    i+= dir_y
                else:
                    dir_x = -dir_y
                    dir_y = 0
                    j += dir_x
        
        return res
            
s = Solution()
print(s.generateMatrix(3))
