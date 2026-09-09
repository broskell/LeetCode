class Solution(object):
    def maximumWealth(self, accounts):
        maxi = sum(accounts[0])
        for i in range(1, len(accounts) - 1, +1):
            if sum(accounts[i]) > maxi:
                maxi = sum(accounts[i])
        return maxi