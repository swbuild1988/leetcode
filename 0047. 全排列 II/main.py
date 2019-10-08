class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()

        res = []

        def backtrack(nums, l):
            if len(nums) == 0:
                res.append(l)
                return
            
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                backtrack(nums[:i] + nums[i+1:], l + [nums[i]])
            
        backtrack(nums, [])

        return res

        


s = Solution()
print(s.permuteUnique([1,2,1,2]))
