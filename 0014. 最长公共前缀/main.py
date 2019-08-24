class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if (len(strs) == 0):
            return ''
        l = 0
        f = True
        res = ''
        while f and l < len(strs[0]):
            for i in range(1, len(strs)):
                if not (l < len(strs[i]) and strs[i][l] == strs[0][l]):
                    f = False
                    break
            if f:
                res+= strs[0][l]
            l += 1
        return res


s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))
