class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        n = len(digits)
        if n == 0:
            return [1]

        digits[n-1] += 1

        while n > 1:
            if digits[n-1] == 10:
                digits[n-1] = 0
                digits[n-2] += 1
            n -= 1

        if digits[0] == 10:
            digits[0] = 0
            digits = [1] + digits

        return digits



s = Solution()
print(s.plusOne([9,9,9]))
