class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        maxpos, curpos, step = 0,0,0
        
        for i in range(0, n):
            if i>curpos:
                curpos=maxpos
                step+=1
            maxpos = max(maxpos, i+nums[i])
        
        return step


s = Solution()
print(s.jump([2,3,1,1,4]))
