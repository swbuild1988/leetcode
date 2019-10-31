class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        res = []
        start, end, n = 0, 0, len(path)

        while start < n-1:
            start = path.find('/', start)
            end = path.find('/', start+1)
            print(start, end)
            s = path[start+1:end] if end != -1 else path[start+1:]
            start = end if end != -1 else n
            print(s)
            if (s == '' or s == '.'):
                continue
            elif (s == '..'):
                if (len(res) > 0):
                    res.pop()
            else:
                res.append(s)
                
        s = ''
        for i in range(len(res)):
            s += '/' + res[i]
        if len(s) == 0:
            s = '/'

        return s


s = Solution()
print(s.simplifyPath("/home/"))
