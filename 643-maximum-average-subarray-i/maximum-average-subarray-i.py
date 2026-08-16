class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        s = 0
        for i in range(k):
            s += nums[i]
        
        maxsum = s

        start = 0
        end = k

        while end < len(nums):
            s -= nums[start]
            start+= 1
            s += nums[end]
            end += 1

            maxsum = max(s,maxsum)
        
        return float(maxsum)/k


        