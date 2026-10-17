class Solution(object):
    def minSwaps(self, nums):
        def get_sum(num):
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            return total

        n = len(nums)
        arr = [(v, i) for i, v in enumerate(nums)]
        arr.sort(key=lambda x: (get_sum(x[0]), x[0]))
        
        t = {orig_i: new_i for new_i, (v, orig_i) in enumerate(arr)}
        
        swaps = 0
        vis = [False] * n
        
        for i in range(0, n, +1):
            if vis[i] or t[i] == i:
                continue
                
            cnt = 0
            curr = i
            while not vis[curr]:
                vis[curr] = True
                curr = t[curr]
                cnt += 1
                
            if cnt > 0:
                swaps += (cnt - 1)
                
        return swaps