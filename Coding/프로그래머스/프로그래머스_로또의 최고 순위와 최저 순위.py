def solution(lottos, win_nums):
    answer = []
    
    cor = 0
    zero = 0
    for i in lottos:
        if i in win_nums:
            cor+=1
        elif i == 0:
            zero +=1

    def rank(a, b):
        return list((a+b,a))

    for i in rank(cor,zero):
        if i ==6:
            answer.append(1)
        elif i ==5:
            answer.append(2)
        elif i ==4:
            answer.append(3)
        elif i ==3:
            answer.append(4)
        elif i ==2:
            answer.append(5)
        elif i <2:
            answer.append(6) 
            
    return answer