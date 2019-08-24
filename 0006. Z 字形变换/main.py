# 中心扩展法
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        store = ['' for i in range(numRows)]
        
        print('---------------------')
        print(store)
        curIndex, direct = 0, 1
        for i in range(len(s)):
            print('**************************')
            print(curIndex, direct)
            store[curIndex] += s[i]

            tmp = curIndex + direct
            if (tmp >= numRows or tmp < 0): direct = direct * -1
            curIndex = curIndex + direct

        res = ''
        for i in range(numRows):
            res = res + store[i]
        return res



s = Solution()
print(s.convert('LEETCODEISHIRING', 3))
