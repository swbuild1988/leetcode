class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        res = []
        hashmap = {}

        for i in range(len(strs)):
            s = "".join((lambda x:(x.sort(),x)[1])(list(strs[i])))
            if s in hashmap:
                hashmap.get(s).append(strs[i])
            else:
                hashmap[s] = [strs[i]]

        for key in hashmap.keys():
            res.append(hashmap.get(key))

        return res


s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
