class Solution:
    def minSubArrayLen(self, target, nums):
        cnt = len(nums)+1
        p = 0
        sub = 0
        for i in range(len(nums)):
            sub += nums[i]
            while sub >= target:
                cnt = min(cnt, i-p+1)
                sub -= nums[p]
                p +=1
        return cnt if cnt != len(nums)+1 else 0