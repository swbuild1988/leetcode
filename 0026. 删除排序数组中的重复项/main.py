class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        index = 0
        while index < len(nums)-1:
            if nums[index] == nums[index+1]:
                nums.pop(index+1)
            else:
                index += 1
        return len(nums)


s = Solution()
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
