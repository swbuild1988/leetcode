class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        p0, p2 = 0, len(nums)-1
        while nums[p0] == 0 and p0 < len(nums)-1:
            p0 += 1
        while nums[p2] == 2 and p2 > 0:
            p2 -= 1

        p1 = p0
        while p1 < p2:
            print(p0,p1,p2,nums)
            if nums[p1] == 0:
                nums[p0], nums[p1] = nums[p1], nums[p0]
                p0 += 1
                if p1 < p0:
                    p1 += 1
            elif nums[p1] == 1:
                p1 += 1
            elif nums[p1] == 2:
                nums[p2], nums[p1] = nums[p1], nums[p2]
                p2 -= 1
                if p1 > p2:
                    p1 -= 1
            # print(nums)



s = Solution()
print(s.sortColors([2]))
