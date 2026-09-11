class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        output1, output2 = "", ""
        for i in range(0, len(word1), +1):
            output1 += word1[i]
        
        for i in range(0, len(word2), +1):
            output2 += word2[i]
        
        return output1 == output2