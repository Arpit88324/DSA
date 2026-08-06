class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        start = 0
        middle = 0
        end = len(nums) -1 

        while middle <= end:
            for i in range(len(nums)):
                if nums[middle] == 0:
                    nums[start],nums[middle] = nums[middle],nums[start]
                    middle += 1
                    start += 1
                elif nums[middle] == 1:
                    middle += 1
                else:
                    nums[end],nums[middle] = nums[middle],nums[end]
                    end -= 1
                
        return nums

        