class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0:
            return []
        
        res=[]

        len1 = len(words[0])
        length = len(words) * len1
        dic = {}
        for word in words:
            dic[word] = dic.get(word, 0) + 1
        print(length)
        print(dic)
        for i in range(len(s)-length+1):
            tmpdic = dic.copy()
            f = True
            for j in range(len(words)):
                tmpstr = s[i+j*len1: i+(j+1)*len1]
                if tmpstr in tmpdic:
                    tmpdic[tmpstr] -= 1
                    if tmpdic[tmpstr] < 0:
                        f = False
                        break
                else:
                    f = False
                    break
            if f:
                res.append(i)
        
        return res
        


s = Solution()
print(s.findSubstring("barfoothefoobarman", ["foo","bar"]))
