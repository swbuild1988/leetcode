class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = ""

        l = [i for i in range(1, n+1, 1)]
        jie = [1]
        for i in range(1, n+1, 1):
            jie.append(jie[i-1]*i)

        for i in range(n, 1, -1):
            j = (k-1) // jie[i-1]
            res += str(l[j])
            l = l[:j] + l[j+1:]
            k = k - j * jie[i-1]
        res += str(l[0])

        return res


s = Solution()
print(s.getPermutation(4, 9))
