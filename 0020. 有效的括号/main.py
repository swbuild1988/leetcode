class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        chars1 = {'(': -1, '[': -2, '{': -3}
        chars2 = {')': 1, ']': 2, '}': 3}

        res = []
        for char in s:
            if (char in chars1):
                res.append(char)
            else:
                if len(res) > 0 and chars1[res[len(res)-1]] + chars2[char] != 0:
                    return False
                else:
                    res.pop()
        return len(res) == 0


s = Solution()
print(s.isValid("]"))
