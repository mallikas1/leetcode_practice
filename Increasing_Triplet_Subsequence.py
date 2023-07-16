class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i= j = float('inf')
        for num in nums:
            if num <= i:
                i = num
                print(i)
            elif num <= j:
                j = num
                print(j)
            else:
                return True
        return False

