class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def solve(tmpS):
            if (int(tmpS) > 255):
                return False
            if (len(tmpS) > 1 and tmpS[0] == '0'):
                return False
            return True

        res = []
        n = len(s)
        for i in range(1, 4):
            for j in range(1, 4):
                for k in range(1, 4):
                    for l in range(1, 4):
                        if (i+j+k+l == n):
                            s1 = s[:i]
                            s2 = s[i:i+j]
                            s3 = s[i+j:i+j+k]
                            s4 = s[i+j+k:i+j+k+l]

                            if (solve(s1) and solve(s2) and solve(s3) and solve(s4)):
                                res.append(s1 + '.'+s2 + '.'+s3 + '.'+s4)

        return res


s = Solution()
print(s.restoreIpAddresses("25525511135"))
