class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []

        def solve(index, l):
            res.append(l)

            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                solve(i+1, l+[nums[i]])
                
        solve(0, [])

        return res



s = Solution()
print(s.subsets([1,2,2]))
