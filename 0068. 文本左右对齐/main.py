class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        record = []
        index, n, rowLen = 0, len(words), 0
        res = []

        while index < n:
            if rowLen + len(words[index]) + len(record) <= maxWidth:
                record.append(words[index])
                rowLen += len(words[index])
                index += 1
            else:
                spaceNum = maxWidth - rowLen
                s = ""
                for i in range(len(record)):
                    s += record[i]
                    if i == len(record) -1 :
                        continue

                    tmpSpace = spaceNum // (len(record)-1-i) + (0 if spaceNum % (len(record)-1-i) == 0 else 1)
                    for j in range(tmpSpace):
                        s += " "
                    spaceNum = spaceNum - tmpSpace

                while len(s) < maxWidth:
                    s += " "
                res.append(s)                
                rowLen, record = len(words[index]), [words[index]]
                index += 1

        s = ""
        for i in range(len(record)):
            s += record[i] + ("" if i == len(record) -1 else " ")
        while len(s) < maxWidth:
            s += " "
        res.append(s)

        return res



s = Solution()
print(s.fullJustify(["What", "must", "be",
                     "acknowledgment", "shall", "be"], 16))
