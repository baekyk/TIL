class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[-k:] , nums[:0] = [] , nums[-k:]