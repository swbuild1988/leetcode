class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x // 10 == 0:
            return True
        if x % 10 == 0:
            return False

        # tmp 为除以10的余数， y为后一半倒过来的数
        tmp , y = 0 , 0
        while y < x:
            tmp = x % 10
            x = x // 10
            if x == y: 
                return True
            y = y * 10 + tmp
            if x == y:
                return True
        
        return False
            


s = Solution()
print(s.isPalindrome(10))
