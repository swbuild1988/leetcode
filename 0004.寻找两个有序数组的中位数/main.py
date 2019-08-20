class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        index1, index2 = 0, 0
        res = []
        while index1 < len(nums1) or index2 < len(nums2):
            if index1 == len(nums1):
                res.append(nums2[index2])
                index2 += 1
            elif index2 == len(nums2):
                res.append(nums1[index1])
                index1 += 1
            elif nums1[index1] < nums2[index2]:
                res.append(nums1[index1])
                index1 += 1
            else:
                res.append(nums2[index2])
                index2 += 1

        print(res)
        len_res = len(res)
        if (len_res % 2 == 1):
            return res[len_res // 2] * 1.0
        else:
            return (res[len_res // 2 - 1] + res[len_res // 2])/2.0


s = Solution()
print(s.findMedianSortedArrays([1, 2], [3, 4]))
