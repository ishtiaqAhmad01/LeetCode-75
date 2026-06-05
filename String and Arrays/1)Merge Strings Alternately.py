class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res = ""
        isl1 = True
        l1 = 0
        l2 = 0

        while l1 < len(word1) or l2 < len(word2):
            if isl1:
                if l1 < len(word1):
                    res+= word1[l1]
                    l1+=1
                else:
                    res+= word2[l2]
                    l2+=1
                isl1 = False
            else:
                if l2 < len(word2):
                    res+= word2[l2]
                    l2+=1
                else:
                    res += word1[l1]
                    l1+=1
                isl1 = True

        return res