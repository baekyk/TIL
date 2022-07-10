class Solution:
    def findRestaurant(self, list1, list2):
        cnt = float('inf')
        rest = []
        for i in list1:
            if i in list2:
                if cnt > (list1.index(i) + list2.index(i)):
                    cnt = list1.index(i) + list2.index(i)
                    rest = [i]
                elif cnt == (list1.index(i) + list2.index(i)):
                    rest.append(i)
        return rest