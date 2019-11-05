class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []

        def solve(index, l):
            res.append(l)

            for i in range(index, len(nums)):
                solve(i+1, l+[nums[i]])
                
        solve(0, [])

        return res



s = Solution()
print(s.subsets([1,2,3]))
