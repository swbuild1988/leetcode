class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        print(len(nums))
        index = len(nums)-1
        while index > 0:
            if nums[index-1] < nums[index]:
                break
            else:
                index -= 1
        print(index)

        if index == 0:
            nums.sort()
        else:
            j, max = index-1, 9999999
            for i in range(index, len(nums)):
                if nums[i]-nums[index-1] > 0 and max > nums[i]-nums[index-1]:
                    max = nums[i]-nums[index-1]
                    j = i
            nums[index-1], nums[j] = nums[j], nums[index-1]
            for i in range(index, len(nums)-1):
                for j in range(i+1, len(nums)):
                    if (nums[i] > nums[j]):
                        nums[i], nums[j] = nums[j], nums[i]
        print(nums)


s = Solution()
# print(s.nextPermutation([1,3,3,2,1]))
print(s.nextPermutation([16,27,25,23,25,16,12,9,1,2,7,20,19,23,16,0,6,22,16,11,8,27,9,2,20,2,13,7,25,29,12,12,18,29,27,13,16,1,22,9,3,21,29,14,7,8,14,5,0,23,16,1,20]))
