# 遍历查找，速度慢
class Solution2(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        nums.sort()
        print(nums)
        i = 0
        while i < len(nums)-2:
            if (nums[i] > 0):
                break

            l, r = i+1, len(nums)-1
            while (l < r):

                if (nums[i] + nums[l] + nums[r] == 0):
                    res.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    l += 1

                    while (l < r and nums[r] == nums[r+1]):
                        r -= 1
                    while (l < r and nums[l] == nums[l-1]):
                        l += 1
                elif (nums[i] + nums[l] + nums[r] > 0):
                    r -= 1
                    while (l < r and nums[r] == nums[r+1]):
                        r -= 1
                else:
                    l += 1
                    while (l < r and nums[l] == nums[l-1]):
                        l += 1
            i += 1
            while (i < len(nums)-2 and nums[i] == nums[i-1]):
                i += 1

        return res

# 利用字典记录
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # 记录每个数字存在的个数
        dic = {}
        res = []

        for i in nums:
            dic[i] = dic.get(i,0) + 1

        pos = [i for i in dic if i > 0]
        neg = [i for i in dic if i < 0]
        neg.sort()

        if (0 in dic and dic[0] >= 3):
            res.append([0,0,0])
        
        for i in pos:
            for j in neg:
                k = 0-i-j
                if k in dic:
                    if (k == i or k ==j) and dic[k]>=2:
                        res.append([j,k,i])
                    elif j<k<i:
                        res.append([j,k,i])
                    if k < j:
                        break

        return res



s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
