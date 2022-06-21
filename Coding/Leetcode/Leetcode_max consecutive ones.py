class Solution:
    def findMaxConsecutiveOnes(self, nums):
        k = 0
        result = []
        for i in nums:
            if i == 1:
                k+=1
            elif i == 0:
                result.append(k)
                k = 0
        result.append(k)
        return max(result)