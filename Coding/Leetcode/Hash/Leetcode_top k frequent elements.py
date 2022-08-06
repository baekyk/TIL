class Solution:
    def topKFrequent(self, nums, k):
        dic = {}
        out = list()
        for i ,c in enumerate(nums):
            if c not in dic:
                dic[c] = 1
            elif c in dic:
                dic[c] +=1

        for i in range(k):
            idx = list(dic.values()).index(max(dic.values()))
            out.append(list(dic.keys())[idx])
            dic.pop(list(dic.keys())[idx])
        return out