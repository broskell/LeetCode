class Solution(object):
    def findAndReplacePattern(self, words, pattern):
		def find(w): 
			l = []
			m = defaultdict(int)
			i = 0
			for c in w:
				if c in m:
					l.append(m[c])
				else:
					i+=1
					m[c]=i
					l.append(m[c])
			return l
		ans = []
		pfind = find(pattern)
		for w in words:
			wfind = find(w)
			if wfind == pfind: ans.append(w) 
		return ans