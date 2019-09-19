#  使用回溯
class Solution(object):
    def combinationSum(self, candidates, target):
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
                if candidates[i] > curTarget:
                    break
                else:
                    solve(i, curList + [candidates[i]], curTarget - candidates[i])
        
        solve(0, [], target)
        return res

# 动规
class Solution2(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """    

        candidates.sort()
        length = len(candidates)
        dp = [[] for i in range(target+1)]

        for i in range(1, target+1):
            for j in range(length):
                if i-candidates[j] < 0:
                    break
                elif i-candidates[j] == 0:
                    dp[i].append([candidates[j]])
                else:
                    if len(dp[i-candidates[j]]) > 0:
                        for k in range(len(dp[i-candidates[j]])):
                            if (candidates[j] >= dp[i-candidates[j]][k][-1]):
                                dp[i].append(dp[i-candidates[j]][k] + [candidates[j]])
        
        return dp[target]


s = Solution2()
print(s.combinationSum([2,3,6,7], 7))
