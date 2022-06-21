def solution(s):
    nums=['zero','one','two','three','four','five','six','seven','eight','nine']    
    temp = ''
    answer = ''
    for i in s:
        if i.isdigit():
            answer = answer+i
        elif i.isalpha():
            temp = temp + i
            if temp in nums:
                answer = answer+str(nums.index(temp))
                temp = ''
    return int(answer)