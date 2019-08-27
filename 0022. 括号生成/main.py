class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        if n == 0:
            return []

        res = []
        res.append([None])
        res.append(["()"])

        index = 2
        while index <= n:
            list = []
            for i in range(index):
                j = index - 1 - i
                print("-------------------")
                print(res, i, j)
                for left in res[i]:
                    for right in res[j]:
                        left = "" if left == None else left
                        right = "" if right == None else right
                        list.append("(" + left + ")" + right)
            res.append(list)
            index += 1

        return res[n]


s = Solution()
print(s.generateParenthesis(4))
