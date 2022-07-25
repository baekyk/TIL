class Solution:
    def lengthOfLongestSubstring(self, s):
        out = set()
        r = 0
        cnt = 0
        result = 0
        for i in range(len(s)):
            while (r < len(s)):
                if s[r] not in out:
                    out.add(s[r])
                    r+=1
                    cnt = len(out)
                    if cnt >result:
                        result = cnt
                elif s[r] in out:
                    out.clear()
                    r = i
                    cnt = 0
                    break


        return result  