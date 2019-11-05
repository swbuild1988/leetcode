class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        rowNum = len(board)
        if rowNum == 0:
            return False
        colNum = len(board[0])
        if colNum == 0:
            return False

        def solve(index, x, y):
            print("------------")
            print(index, x, y)
            if index == len(word):
                return True

            for i in range(0, 4):
                dir_x = (-1 if i // 2 == 0 else 1) if i % 2 == 0 else 0
                dir_y = (-1 if i // 2 == 0 else 1) if i % 2 == 1 else 0
                if 0 <= x+dir_x < colNum and 0 <= y+dir_y < rowNum and board[y+dir_y][x+dir_x] == word[index]:
                    board[y+dir_y][x+dir_x] = ""
                    print(x+dir_x,y+dir_y,board)
                    if solve(index+1, x+dir_x, y+dir_y):
                        return True
                    board[y+dir_y][x+dir_x] = word[index]
                    print(x+dir_x,y+dir_y,board)

            return False

        for i in range(rowNum):
            for j in range(colNum):
                if board[i][j] == word[0]:
                    board[i][j] = ""
                    if solve(1, j, i):
                        return True
                    board[i][j] = word[0]
        return False


s = Solution()
print(s.exist([["a","a"]], "aaa"))
