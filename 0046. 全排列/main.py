class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        n = len(nums)
        usedPos = [-1 for _ in range(n)]
        
        res = []
        
        def solve(index):
            if index == n:
                res.append([])
                for i in range(n):
                    res[-1].append(nums[usedPos[i]])
                return
            
            for i in range(n):
                if usedPos[i] == -1:
                    usedPos[i] = index
                    solve(index+1)
                    usedPos[i] = -1
        
        solve(0)
        
        return res

s = Solution()
print(s.permute([1,2,3]))
