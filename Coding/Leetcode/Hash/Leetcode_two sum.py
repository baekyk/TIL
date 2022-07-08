class Solution:
    def twoSum(self, nums, target):
        temp = {}
        for i in range(len(nums)):
            if target-nums[i] in temp:
                return ([temp[target-nums[i]],i])
            temp[nums[i]]=i