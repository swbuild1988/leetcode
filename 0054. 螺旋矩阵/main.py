class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        res = []
        index, i, j, dir_x, dir_y = 0, 0, 0, 1, 0

        n = len(matrix)
        if n == 0:
            return res
        m = len(matrix[0])

        while index < m*n:
            index += 1
            res.append(matrix[i][j])
            matrix[i][j] = 0

            # x 方向移动
            if dir_x != 0:
                if (j+dir_x >= 0 and j+dir_x < m and matrix[i][j+dir_x] != 0):
                    j += dir_x
                else:
                    dir_y = dir_x
                    dir_x = 0
                    i += dir_y
            else:
                if (i+dir_y >=0 and i+dir_y < n and matrix[i+dir_y][j] != 0):
                    i+= dir_y
                else:
                    dir_x = -dir_y
                    dir_y = 0
                    j += dir_x
        
        return res


s = Solution()
print(s.spiralOrder([
    [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]))
