class Solution:
    def groupAnagrams(self, strs):

        dic = dict()
        for w in strs:
            key = tuple(sorted(w))
            dic[key] = dic.get(key,[])+ [w]

        return list(dic.values())