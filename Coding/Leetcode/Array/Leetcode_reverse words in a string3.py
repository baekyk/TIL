class Solution:
    def reverseWords(self, s):
        temp = []
        for i in s.split():
            temp.append(''.join(reversed(i)))
        return ' '.join(temp)