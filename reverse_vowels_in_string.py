class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = list('aeiouAEIOU')
        
        index = []
        v_in_s = []
        v_without_s = list(s)

        for i in range(len(s)):
            if s[i] in vowels:
                v_in_s.append(s[i])
                index.append(i)
        v_in_s.reverse()
        for i, letter in zip(index, v_in_s):
            v_without_s[i] = letter
        return ''.join(v_without_s)
