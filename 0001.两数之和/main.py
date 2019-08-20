class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i, val in enumerate(nums):
            if hashmap.__contains__(target - val):
                return [hashmap.get(target-val), i]
            hashmap[val] = i


s = Solution()
print(s.twoSum([2, 7, 21, 212], 9))
