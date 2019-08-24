class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        
        res = 0
        index = 0
        while len(s) > 0:
            l = len(romans[index])
            while (s[:l] == romans[index]):
                res += nums[index]
                s = s[l:]
            index += 1
        return res


s = Solution()
print(s.romanToInt('IV'))
