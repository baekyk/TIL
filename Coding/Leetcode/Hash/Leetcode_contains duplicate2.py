class Solution:
    def containsNearbyDuplicate(self, nums, k):
        dic = dict()

        for i,c in enumerate(nums):
            if c in dic and abs(dic[c]-i) <=k:
                    return True
            dic[c] = i
        return False

