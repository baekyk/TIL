class Solution:
    def firstUniqChar(self, s):
        m = {}
        for i, c in enumerate(s):
            if c not in m:
                m[c]=1
            elif c in m:
                m[c]+=1
        for i in m:
            if m[i]==1:
                return s.index(i)
        return -1
