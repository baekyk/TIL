class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num = max(nums)
        idx = nums.index(max_num)
        cnt = 0
        for i, x in enumerate(nums):
            if i == idx:
                continue
            elif x*2 <= max_num:
                cnt += 1
        
        if cnt == len(nums) -1:
            return idx
        else:
            return -1
                