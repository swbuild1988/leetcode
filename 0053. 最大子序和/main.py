class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res, curMax = nums[0], nums[0]

        for i in range(1, len(nums)):
            if (curMax > 0):
                curMax += nums[i]
            else:
                curMax = nums[i]
            res = max(res, curMax)

        return res


s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
