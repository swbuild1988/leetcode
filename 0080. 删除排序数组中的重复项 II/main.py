class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        index = 1
        while index < len(nums)-1:
            if nums[index-1] == nums[index+1]:
                nums.pop(index)
            else:
                index += 1
        
        return len(nums)

s = Solution()
print(s.removeDuplicates([1,1,1,2,2,3]))
