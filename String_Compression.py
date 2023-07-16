class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        length = len(chars)

        i = 0

        j = 0
        for pos, char in enumerate(chars):
            # print(length, pos, char, j, i)
            if (pos+1) == length or char != chars[pos+1]:
                chars[j] = char
                j += 1

                if pos > i:
                    repeat = pos - i + 1
                    print('repeat:', repeat)

                    for num in str(repeat):
                        chars[j] = num
                        j += 1
                i = pos + 1
        return j

