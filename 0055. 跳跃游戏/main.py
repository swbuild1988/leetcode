class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        maxpos = 0
        for i in range (len(nums)):
            if i > maxpos:
                return False
            maxpos = max(maxpos, i + nums[i])
        return True

s = Solution()
print(s.canJump([2,3,1,1,4]))
