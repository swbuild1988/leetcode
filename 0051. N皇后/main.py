import time

# 回溯，每次都判断


class Solution1(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        col = [-1 for _ in range(n)]
        self.res = []

        def solve(row):

            if row == n:
                tmp = []
                for i in range(n):
                    s = ""
                    for j in range(n):
                        if j == col[i]:
                            s += "Q"
                        else:
                            s += "."
                    tmp.append(s)

                self.res.append(tmp)
                return

            # 将第row行的皇后放在第i列，col[row] = i
            for i in range(n):
                ok = True
                # 判断是否与之前的点冲突了
                for j in range(row):
                    if col[j] == i or row-j == abs(col[j]-i):
                        ok = False
                        break

                if ok:
                    col[row] = i
                    solve(row+1)
                    col[row] = -1

        ts = time.time()
        solve(0)
        te = time.time()
        print("total time: %f seconds" % (te - ts))
        return self.res


# 回溯，每放一个，做一个标记
class Solution2(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        col = [-1 for _ in range(n)]
        shu = [False for _ in range(n)]
        pie = [False for _ in range(2*n-1)]
        na = [False for _ in range(2*n-1)]
        self.res = []

        def solve(row):

            if row == n:
                tmp = []
                for i in range(n):
                    s = ""
                    for j in range(n):
                        if j == col[i]:
                            s += "Q"
                        else:
                            s += "."
                    tmp.append(s)

                self.res.append(tmp)
                return

            # 将第row行的皇后放在第i列，col[row] = i
            for i in range(n):
                # 判断能放不能放
                if shu[i] or pie[row+i] or na[n-1-row+i]:
                    continue

                col[row] = i
                shu[i] = True
                pie[row+i] = True
                na[n-1-row+i] = True
                solve(row+1)
                col[row] = -1
                shu[i] = False
                pie[row+i] = False
                na[n-1-row+i] = False

        ts = time.time()
        solve(0)
        te = time.time()
        print("total time: %f seconds" % (te - ts))
        return self.res

# 用位运算做标记，位运算说明

# 与 (and):                      5 & 6 = 4        (101 & 110 = 100)
# 或 (or):                       5 | 6 = 7        (101 | 110 = 111)
# 异或 (xor):                    5 ^ 6 = 3        (101 ^ 110 = 011)
# 取反 (not / complement):       ~5 = -6          (~00000101 = 11111010)
# 左移 (shift left):             5 << 2 = 20      (101 << 2 = 10100)
# 右移 (shift right):            5 >> 2 = 1       (101 >> 2 = 1)

# 把第 i 位置 1：a |= (1 << i)
# 把第 i 位置 0：a &= ~(1 << i)
# 把第 i 位取反：a ^= (1 << i)
# 读取第 i 位的值：(a >> i) & 1
class Solution3(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        col = [-1 for _ in range(n)]
        self.shu = self.pie = self.na = 0
        self.res = []

        def solve(row):

            if row == n:
                tmp = []
                for i in range(n):
                    s = ""
                    for j in range(n):
                        if j == col[i]:
                            s += "Q"
                        else:
                            s += "."
                    tmp.append(s)

                self.res.append(tmp)
                return

            # 将第row行的皇后放在第i列，col[row] = i
            for i in range(n):
                # 判断能放不能放
                j = row + i
                k = n-1-row+i
                if ((self.shu >> i) | (self.pie >> j) | (self.na >> k)) & 1:
                    continue

                col[row] = i
                self.shu |= (1<<i)
                self.pie |= (1<<j)
                self.na |= (1<<k)
                solve(row+1)
                col[row] = -1
                self.shu &= ~(1 << i)
                self.pie &= ~(1 << j)
                self.na &= ~(1 << k)

        ts = time.time()
        solve(0)
        te = time.time()
        print("total time: %f seconds" % (te - ts))
        return self.res


s = Solution3()
print(s.solveNQueens(4))
