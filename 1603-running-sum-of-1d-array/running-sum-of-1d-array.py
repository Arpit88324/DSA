class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = list()
        s = 0

        for i in range(len(nums)):
            s += nums[i]
            l.append(s)
        return l

        