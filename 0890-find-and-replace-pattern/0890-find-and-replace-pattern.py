class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        def idAssign(word):
            wId = 0
            wordToId = {}
            wordId = []

            for w in word:
                if w not in wordToId:
                    wId += 1
                    wordToId[w] = wId
                wordId.append(wordToId[w])
            return wordId

        target = idAssign(pattern)
        output = []

        for word in words:
            matchedId = idAssign(word)
            if matchedId == target:
                output.append(word)
        return output