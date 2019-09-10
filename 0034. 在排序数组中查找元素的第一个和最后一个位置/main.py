class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                i, j = mid, mid
                while i-1 >= 0 and nums[i-1] == nums[i]:
                    i -= 1
                while j+1 <len(nums) and nums[j] == nums[j+1]:
                    j += 1
                return [i, j]
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        
        return [-1, -1]

s = Solution()
print(s.searchRange([5,7,7,8,8,10], 8))
