class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        if len(intervals) == 0:
            return [newInterval]

        res = []
        index = 0

        # 先找到第一个有接触的区域
        while index < len(intervals) and intervals[index][1] < newInterval[0]:
            res.append(intervals[index])
            index += 1

        # 如果已经到了最后了
        if (index == len(intervals)):       
            res.append(newInterval)
            return res
        
        # 否则记录下来
        left, right = min(intervals[index][0], newInterval[0]), newInterval[1]
        while index < len(intervals) and intervals[index][1] <= right:
            index += 1

        # 如果已经到最后了
        if (index == len(intervals)):
            res.append([left, right])
            return res

        if (intervals[index][0] <= right):
            res.append([left,intervals[index][1]])
        else:
            res.append([left,right])
            res.append(intervals[index])

        # 将后面的加进来
        res += intervals[index+1:]
        return res



s = Solution()
print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
