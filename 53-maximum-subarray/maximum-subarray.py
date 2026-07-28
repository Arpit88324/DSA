class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = nums[0]

        total = 0

        for i in nums:
            if total <  0:
                total = 0
            total  += i
            m = max(m,total)
        return m
        