class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        columns = [set(range(1, 10)) for i in range(9)]
        rows = [set(range(1, 10)) for i in range(9)]
        boxs = [set(range(1, 10)) for i in range(9)]
        empty = []

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    val = int(board[i][j])
                    columns[i].remove(val)
                    rows[j].remove(val)
                    k = i // 3 * 3 + j // 3
                    boxs[k].remove(val)
                else:
                    empty.append((i, j))

        def solve(index):
            if index == len(empty):
                return True

            i, j = empty[index]
            k = i//3*3 + j // 3
            for val in columns[i] & rows[j] & boxs[k]:
                columns[i].remove(val)
                rows[j].remove(val)
                boxs[k].remove(val)
                board[i][j] = str(val)
                if solve(index + 1):
                    return True
                columns[i].add(val)
                rows[j].add(val)
                boxs[k].add(val)
            return False

        solve(0)
        print(board)



s = Solution()
print(s.solveSudoku([
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]))
