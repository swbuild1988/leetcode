class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        columns = [{} for i in range(9)]
        rows = [{} for i in range(9)]
        boxs = [{} for i in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != '.':
                    if val in columns[i]:
                        return False
                    columns[i][val] = 1 

                    if val in rows[j]:
                        return False
                    rows[j][val] = 1

                    k = i // 3 * 3 + j // 3
                    if val in boxs[k]:
                        return False
                    boxs[k][val] = 1
        return True


s = Solution()
print(s.isValidSudoku([
 ["8","3",".",".","7",".",".",".","."],
 ["6",".",".","1","9","5",".",".","."],
 [".","9","8",".",".",".",".","6","."],
 ["8",".",".",".","6",".",".",".","3"],
 ["4",".",".","8",".","3",".",".","1"],
 ["7",".",".",".","2",".",".",".","6"],
 [".","6",".",".",".",".","2","8","."],
 [".",".",".","4","1","9",".",".","5"],
 [".",".",".",".","8",".",".","7","9"]
]))
