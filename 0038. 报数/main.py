class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        res = ["1"]

        while len(res) < n: 
            head, tail = 0, 0
            tmp = ""
            while head < len(res[-1]):
                while tail < len(res[-1]) and res[-1][head] == res[-1][tail]:
                    tail += 1
                tmp += str(tail - head)+ res[-1][head]
                head = tail
            res.append(tmp)

        return res[-1]       



s = Solution()
print(s.countAndSay(6))
