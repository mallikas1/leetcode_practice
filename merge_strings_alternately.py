class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = []
        l1 = len(word1)
        l2 = len(word2)
        if l1==l2:
            for i, j in zip(word1, word2):
                merged.append(i)
                merged.append(j)
            return ''.join(merged)
        else:
            if l1>l2:
                for i in range(l2):
                    merged.append(word1[i])
                    merged.append(word2[i])
                for i in range(l2,l1):
                    merged.append(word1[i])
            else:
                for i in range(l1):
                    merged.append(word1[i])
                    merged.append(word2[i])
                for i in range(l1,l2):
                    merged.append(word2[i])
            return ''.join(merged)

            
