class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        res = 0
        tmp = prices[0]
        for i in range(1, len(prices)):
            res = max(prices[i]-tmp, res)
            tmp = min(prices[i], tmp)

        return res


s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
