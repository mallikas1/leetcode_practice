class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_conv = {'I': 1, 'V': 5,
            'X': 10, 'L': 50, 'C': 100,
            'D': 500, 'M': 1000}
        sum = 0
        i = 0
        while i <= (len(s)-2):
            if (s[i] + s[i+1]== 'IV') or (s[i] + s[i+1]== 'IX') or (s[i] + s[i+1]== 'XL') or (s[i] + s[i+1]== 'XC') or (s[i] + s[i+1]== 'CD') or (s[i] + s[i+1]== 'CM'):
                sum = sum - dict_conv[s[i]] + dict_conv[s[i+1]]
                i = i + 2
            else:
                sum = sum + dict_conv[s[i]]
                i = i + 1
        if i == len(s)-1:
            sum = sum + dict_conv[s[i]]
        return sum
