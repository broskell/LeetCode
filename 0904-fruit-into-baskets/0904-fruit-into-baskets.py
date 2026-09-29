import collections

class Solution(object):
    def totalFruit(self, fruits):
        ans = 0
        count = collections.defaultdict(int)
        l = 0
        
        for r in range(len(fruits)):
            count[fruits[r]] += 1
            
            while len(count) > 2:
                count[fruits[l]] -= 1
                if count[fruits[l]] == 0:
                    del count[fruits[l]]
                l += 1  
            ans = max(ans, r - l + 1)
            
        return ans