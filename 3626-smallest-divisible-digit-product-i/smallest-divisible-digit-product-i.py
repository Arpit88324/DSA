class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        while True:
            product = 1
            temp = n

            while temp > 0:
                product *= temp % 10
                temp //= 10

            if product % t == 0:
                return n

            n += 1