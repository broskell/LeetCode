class Solution(object):
    def maximumWealth(self, accounts):
        maxi = 0
        for acc in accounts:
            maxi = max(maxi, sum(acc))
        return maxi