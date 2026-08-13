class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        water = 0

        left  = 1
        right = len(height) - 2

        leftmax = height[0]
        rightmax = height[len(height) - 1]


        while left <= right:

           
            leftmax = max(height[left],leftmax)
            rightmax = max(height[right],rightmax)

            if rightmax < leftmax:
                water  = water + (rightmax - height[right])
                right -= 1
            else:
                water = water + (leftmax - height[left])
                left += 1
        return water

        