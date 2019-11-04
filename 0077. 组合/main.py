class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        res = []

        def solve(index, l):
            if index == k:
                res.append(l[1:])
                return

            for i in range(l[-1]+1, n-k+index+2):
                l.append(i)
                solve(index+1, l)
                l.pop()

        solve(0, [0])

        return res



s = Solution()
print(s.combine(4,2))
