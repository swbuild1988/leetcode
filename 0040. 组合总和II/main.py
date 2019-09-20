#  使用回溯
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        candidates.sort()
        res = []

        def solve(start, curList, curTarget):
            if curTarget == 0:
                res.append(curList)
            for i in range(start, len(candidates)):
                if (i > start and candidates[i] == candidates[i-1]):
                    continue

                if candidates[i] > curTarget:
                    break
                else:
                    solve(i + 1, curList + [candidates[i]], curTarget - candidates[i])
        
        solve(0, [], target)
        return res

# # 动规
# class Solution2(object):
#     def combinationSum2(self, candidates, target):
#         """
#         :type candidates: List[int]
#         :type target: int
#         :rtype: List[List[int]]
#         """    

#         candidates.sort()
#         length = len(candidates)
#         dp = [[] for i in range(target+1)]

#         for c in candidates:
#             for i in range(target, c-1, -1):
#                 for k in dp[i-c]:
#                     dp[i].append(c)

#         return dp[target]


s = Solution()
print(s.combinationSum2([10,1,2,7,6,1,5], 8))