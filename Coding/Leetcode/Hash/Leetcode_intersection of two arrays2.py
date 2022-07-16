class Solution:
    def intersect(self, nums1, nums2):
        its = list(set(nums1).intersection(nums2))
        dic = dict()
        for i in its:
            if nums1.count(i) >= nums2.count(i):
                dic[i]=nums2.count(i)
            elif nums1.count(i) < nums2.count(i):
                dic[i]=nums1.count(i)
        out = []
        for key, value in dic.items():
            for i in range(value):
                out.append(key)
        return out
    

class Solution2:
    def intersect2(self, nums1, nums2):
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        ans = []
        
        i,j = 0,0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                ans.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        
        return ans


class Solution3:
    def intersect3(self, nums1, nums2):
        hashmap = {}
        answer = []
        
        for i in nums1:
            if i not in hashmap:
                hashmap[i] = 1
            elif i in hashmap:
                hashmap[i] += 1
                
        for i in nums2:
            if i in hashmap and hashmap[i] != 0:
                hashmap[i] -= 1
                answer.append(i)
        return answer