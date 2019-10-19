import time
import math

# 回溯，每次都判断


class Solution1(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        col = [-1 for _ in range(n)]
        self.res = 0

        def solve(row):

            if row == n:
                self.res += 1
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
        self.res = 0

        def solve(row):

            if row == n:
                self.res += 1
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
        self.res = 0

        def solve(row):

            if row == n:
                self.res += 1
                return

            # 将第row行的皇后放在第i列，col[row] = i
            for i in range(n):
                # 判断能放不能放
                j = row + i
                k = n-1-row+i
                if ((self.shu >> i) | (self.pie >> j) | (self.na >> k)) & 1:
                    continue

                col[row] = i
                self.shu |= (1 << i)
                self.pie |= (1 << j)
                self.na |= (1 << k)
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

# 通过位运算改进算法，解决方法三种，需要判断每一列的问题（ for i in range(n) ），而是直接去找可以放置皇后的列

# a & -a。它称为 lowbit 操作，可以提取出 a 中最右边一个 1 的位置。原理如下：
# a = 00110100
# ~a = 11001011
# -a = 11001100
# a & -a = 00000100
# 「-a」其实是个算术运算，上文中说过，它等于把 a 取反再加 1。

#   当试探到第 row 行时，如果能用一个 bit array 表示出这一行上能放置皇后的位置，就可以用上述循环直接枚举它们，跳过那些已经不能放置皇后的位置了。
# 显然，shu 这个 bit array 中值为 1 的那些位是不能放的。那么 pie 和 na 这两个 bit array 对当前行有什么影响呢？注意到第 row 行的各列对应的撇
# 编号为 row 至 row + n - 1，捺编号为 n - 1 - row 至 2n - 2 - row。如果把 pie 右移 row 位，把 na 右移 n - 1 - row 位，那么它们的最右 n 位
# 中值为 1 的那些位就也不能放置皇后了。把三者或起来再取反：~(shu | (pie >> row) | (na >> (n - 1 - row)))，得到的结果中的最右 n 位就代表了
# 能够放置皇后的位置。注意这个结果中，除了最右 n 位以外，左边的位中也会有一些 1，这些 1 是多余的，应当去掉。怎么去掉呢？可以用一个最右 n 位为 1、
# 其它位为 0 的 bit array 与上述结果进行与运算，而这个 bit array 可以用 (1 << n) - 1 这个表达式制造出来。


class Solution4(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        col = [-1 for _ in range(n)]
        self.shu = self.pie = self.na = 0
        self.res = 0

        def solve(row):

            if row == n:
                self.res += 1
                return

            # 当前可放皇后的列
            available = ((1 << n) - 1) & ~(self.shu |
                                           (self.pie >> row) | (self.na >> (n - 1 - row)))
            # 将所有可放的列全部搜一遍
            while available:
                # 从最后一个开始试
                p = available & -available
                available ^= p

                col[row] = math.log(p, 2)
                self.shu ^= p
                self.pie ^= (p << row)
                self.na ^= (p << (n - 1 - row))  # 设置标记
                solve(row + 1)
                col[row] = -1
                self.shu ^= p
                self.pie ^= (p << row)
                self.na ^= (p << (n - 1 - row))  # 清除标记

        ts = time.time()
        solve(0)
        te = time.time()
        print("total time: %f seconds" % (te - ts))
        return self.res

# 利用形参
class Solution5(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        self.res = 0

        def solve(row, shu, pie, na):

            if row == n:
                self.res += 1
                return

            # 当前可放皇后的列
            available = ((1 << n) - 1) & ~(shu | pie | na)
            # 将所有可放的列全部搜一遍
            while available:
                # 从最后一个开始试
                p = available & -available
                available ^= p

                solve(row + 1, shu | p, (pie | p) >> 1, (na | p) << 1)  # 设置标记

        ts = time.time()
        solve(0, 0, 0, 0)
        te = time.time()
        print("total time: %f seconds" % (te - ts))
        return self.res


s = Solution5()
print(s.solveNQueens(8))
