class Solution(object):
    def subtractProductAndSum(self, n):
        sum, pdt = 0, 1
        while n > 0:
            rem = n % 10
            pdt *= rem
            sum += rem
            n //= 10
        return pdt - sum