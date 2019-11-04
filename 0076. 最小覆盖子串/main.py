class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        hash_t = {}
        for x in t:
            hash_t[x] = hash_t.get(x, 0) + 1
        hash = {}
        
        # 判断tmp中是否包含所有的t中字母
        def solve():   
            print("=============")         
            print(hash, hash_t)
            for x in hash_t.keys():
                if x not in hash:
                    print(False)
                    return False
                if hash.get(x) < hash_t.get(x):
                    print(False)
                    return False
            
            print(True)
            return True


        left,right = 0,1
        res = ""
        while right <= len(s):
            hash[s[right-1]] = hash.get(s[right-1], 0) + 1
            while solve():
                if res == "" or right - left < len(res):
                    res = s[left: right]
                    
                hash[s[left]] = hash.get(s[left]) - 1
                left += 1

            right += 1

        return res


s = Solution()
print(s.minWindow("ADOBECODEBANC","ABC"))
