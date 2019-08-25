class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = 2000000
        nums.sort()

        for i in range(len(nums)-2):
            head, tail = i+1, len(nums)-1
            while head < tail:
                sum = nums[i] + nums[head]+nums[tail]
                if (abs(target - sum) < abs(target-res)):
                    res = sum
                if sum < target:
                    head += 1
                elif sum > target:
                    tail -= 1
                else:
                    return res

        return res

s = Solution()
print(s.threeSumClosest([-1, 2, 1, -4], 1))
