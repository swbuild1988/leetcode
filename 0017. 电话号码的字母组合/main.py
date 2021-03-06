class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        def backtrack(preStr, digits):
            if len(digits) == 0:
                res.append(preStr)
                return

            for letter in phone[digits[0]]:
                backtrack(preStr+letter, digits[1:])

        res = []
        if (digits):
            backtrack("", digits)

        return res


s = Solution()
print(s.letterCombinations("23"))
