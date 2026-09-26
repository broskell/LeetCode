class Solution(object):
    def evaluate(self, s, knowledge):
        dictMap = dict(knowledge)
        result, i = [], 0

        while i < len(s):
            if s[i] == '(':
                j = s.find(')', i + 1)
                result.append(dictMap.get(s[i+1:j], '?'))
                i = j
            else:
                result.append(s[i])
            i += 1
        return ''.join(result)