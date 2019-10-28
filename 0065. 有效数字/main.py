class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = s.strip()
        # f:符号；p：点；e：指数；d：数字
        states = [
            {"f": 1, "d": 2, "p": 7},
            {"d": 2, "p": 7},
            {"d": 2, "p": 3, "e": 4},
            {"d": 3, "e": 4},
            {"f": 6, "d": 5},
            {"d": 5},
            {"d": 5},
            {"d": 8},
            {"d": 8, "e": 4}
        ]

        state = 0
        for c in s:
            typ = "o"
            if c == "+" or c == "-":
                typ = "f"
            elif c == ".":
                typ = "p"
            elif c == "e":
                typ = "e"
            elif "0" <= c <= "9":
                typ = "d"

            if typ in states[state]:
                state = states[state][typ]
            else:
                return False


        if state == 2 or state == 3 or state == 5 or state == 8:
            return True

        return False


s = Solution()
print(s.isNumber(" 2e10   "))
