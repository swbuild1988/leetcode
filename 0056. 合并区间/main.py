class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0:
            return []

        intervals.sort()

        res = []
        left, right = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= right:
                right = max(intervals[i][1],right)
            else:
                res.append([left, right])
                left, right = intervals[i][0], intervals[i][1]
        
        res.append([left, right])

        return res


s = Solution()
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))
