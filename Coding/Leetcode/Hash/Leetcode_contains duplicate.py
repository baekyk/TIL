class Solution:
    def containsDuplicate(self, nums):
        h = set()
        for i in nums:
            if i in h:
                return True
            h.add(i)
        return False