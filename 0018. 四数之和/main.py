class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        res = []
        length = len(nums)
        if length < 4:
            return res
        nums.sort()
        print("*****************************")
        print(nums)

        index1, index2 = 0, 1
        while index1 < length-3:
            while index2 < length-2:
                print("+++++++++++++++++++++++++++++++")
                tmp = target - nums[index1] - nums[index2]
                print(index1, index2, tmp)
                print("------------------------------")
                print(tmp)
                l, r = index2+1, length-1
                while (l < r):
                    if (tmp == nums[l] + nums[r]):
                        res.append(
                            [nums[index1], nums[index2], nums[l], nums[r]])
                        r -= 1
                        while (l < r and nums[r+1] == nums[r]):
                            r -= 1
                        l += 1
                        while (l < r and nums[l-1] == nums[l]):
                            l += 1
                    elif tmp < nums[l]+nums[r]:
                        r -= 1
                        while (l < r and nums[r+1] == nums[r]):
                            r -= 1
                    else:
                        l += 1
                        while (l < r and nums[l-1] == nums[l]):
                            l += 1

                while index2 < length-2 and nums[index2] == nums[index2+1]:
                    index2 += 1
                index2 += 1

            while index1 < length-3 and nums[index1] == nums[index1+1]:
                index1 += 1
            index1 += 1
            index2 = index1+1

        return res


s = Solution()
print(s.fourSum([-1,0,-5,-2,-2,-4,0,1,-2], -9))
