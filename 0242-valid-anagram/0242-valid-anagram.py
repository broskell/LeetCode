class Solution(object):
    def isAnagram(self, s, t):
        freq_lst = [0]*256
        if len(s) != len(t):
            return False
        else:
            for i in range(0, len(s), +1):
                index = ord(s[i])
                freq_lst[index]+=1
            for j in range(0, len(t), +1):
                index = ord(t[j])
                freq_lst[index]-=1
            if freq_lst == [0]*256:
                return True
            else:
                return False