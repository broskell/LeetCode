class Solution(object):
    def totalFruit(self, fruits):
        bucket = {}
        j = 0
        result = 0
        for i in range(len(fruits)):
            a = fruits[i]
            bucket[a] = bucket.get(a,0)+1
            while len(bucket)>2:
                bucket[fruits[j]] -= 1
                if  bucket[fruits[j]] == 0:
                    del bucket[fruits[j]]
                j += 1
            nowlen = i-j+1
            result = max(result, nowlen)
        return result