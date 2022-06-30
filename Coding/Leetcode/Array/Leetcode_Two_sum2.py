class Solution:
    def twoSum(self, numbers, target):
        for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                if numbers[j] == (target-numbers[i]):
                    return [i+1,j+1]
                elif numbers[j] == numbers[i]:
                    break