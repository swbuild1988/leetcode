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
                na[n-1-row+i]= True
                solve(row+1)
                col[row] = -1
                shu[i] = False
                pie[row+i] = False
                na[n-1-row+i]= False

        ts = time.time()
        solve(0)
        te = time.time()
        print("total time: %f seconds" % (te - ts))
        return self.res

s = Solution2()
print(s.solveNQueens(4))
