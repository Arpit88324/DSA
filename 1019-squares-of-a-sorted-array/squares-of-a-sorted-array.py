class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = list()

        for i in range(len(nums)):
            l.append(nums[i]*nums[i])
            
        return sorted(l)