class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if len(needle) == 0:
            return 0

        for i in range(len(haystack)-len(needle)+1):
            # f = True
            # for j in range(len(needle)):
            #     if haystack[i+j] != needle[j]:
            #         f = False
            #         break
            # if f:
            #     return i
            if haystack[i: i+len(needle)]== needle:
                return i
        
        return -1


s = Solution()
print(s.strStr("aabb", "bb"))
