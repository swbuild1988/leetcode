class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        if num1=="0" or num2=="0":
            return "0"

        res = [0 for i in range(len(num1) + len(num2))]

        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                res[i+j+1] += int(num1[i]) * int(num2[j])
                if res[i+j+1] >= 10:
                    res[i+j] += res[i+j+1] // 10
                    res[i+j+1] = res[i+j+1] % 10

        print(res)
        
        val = ""
        for i in range(len(num1) + len(num2)):
            if i == 0 and res[i] == 0:
                continue;
            val += str(res[i])
        return val


s = Solution()
print(s.multiply("2", "52"))
