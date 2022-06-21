s = ["h","e","l","l","o"]
def reverse(s):
    i = 0
    j = len(s)-1
    while (i <= j):
        s[i],s[j] = s[j], s[i]
        i+=1
        j-=1
        print(s)
reverse(s)