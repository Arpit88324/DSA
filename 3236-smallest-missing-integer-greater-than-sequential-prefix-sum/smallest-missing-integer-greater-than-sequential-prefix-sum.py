class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Find sequential prefix sum
        total = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break
        
        # Find smallest missing integer >= total
        s = set(nums)
        
        while total in s:
            total += 1
        
        return total