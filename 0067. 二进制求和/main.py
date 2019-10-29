class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ""
        m, n = len(a), len(b)
        if (m < n):
            m, n = n, m
            a, b = b, a

        index, tmp = 0, 0

        while index < m:
            k = int(a[m-1-index])+tmp+(int(b[n-1-index]) if index < n else 0)
            tmp = k // 2
            res = str(k % 2) + res
            index += 1

        if tmp == 1:
            res = str(1) + res
        
        return res

s = Solution()
print(s.addBinary("11", "1"))
