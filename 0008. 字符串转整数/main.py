class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.lstrip()

        if len(str) == 0:
            return 0

        index = 1 if (str[0] == '+' or str[0] == '-') else 0
        dir = -1 if str[0] == '-' else 1

        whiteList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        res = 0
        for i in range(index, len(str)):
            if (str[i] not in whiteList):
                break

            res = res * 10 + int(str[i]) * dir

            if res < -2147483648:
                return -2147483648
            if res > 2147483647:
                return 2147483647

        return res


s = Solution()
print(s.myAtoi('  -42'))
