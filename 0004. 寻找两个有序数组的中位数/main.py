
# 时间复杂性 O(m+n)


class Solution2(object):
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

# 时间复杂性O(log(m+n))
# 参考：https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/4-xun-zhao-liang-ge-you-xu-shu-zu-de-zhong-wei-shu/

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        m = len(nums1)
        n = len(nums2)
        if m > n:
            m, n = n, m
            nums1, nums2 = nums2, nums1

        l, r = 0, 2 * m
        while l <= r:
            m1 = (l + r) // 2
            m2 = len(nums1) + len(nums2) - m1
            left1 = nums1[(m1 - 1) // 2] if m1 != 0 else float("-inf")
            right1 = nums1[m1 // 2] if m1 != 2 * len(nums1) else float("+inf")
            left2 = nums2[(m2 - 1) // 2] if m2 != 0 else float("-inf")
            right2 = nums2[m2 // 2] if m2 != 2 * len(nums2) else float("+inf")
            if left1 > right2:
                r = m1 - 1
            elif left2 > right1:
                l = m1 + 1
            else:
                return (max(left1, left2) + min(right1, right2)) / 2.0


s = Solution()
print(s.findMedianSortedArrays([1, 3], [2,3,4]))
