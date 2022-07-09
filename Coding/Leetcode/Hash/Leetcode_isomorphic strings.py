class Solution:
    def isIsomorphic(self, s, t):
        s_ = {}
        t_ = {}
        for i in range(len(s)):
            if (s[i] not in s_) and (t[i] not in t_):
                s_[s[i]] = t[i]
                t_[t[i]] = s[i]
            elif (s_.get(s[i]) != t[i]) or (t_.get(t[i]) != s[i]):
                return False
        return True