class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        l = list()

        for i in range(len(accounts)):
            l.append(sum(accounts[i]))
        
        return max(l)

        