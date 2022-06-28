def solution(numbers, hand):
    answer = ''
    
    left = [1,4,7,10]
    middle = [2,5,8,0]
    right = [3,6,9,12]

    l= 10
    r= 12

    for i in numbers:
        if i in left:
            answer += 'L'
            l = i
        elif i in right:
            answer += 'R'
            r = i

        # 좌우로 이동시 +1 or -1 이고
        # 위아래로 이동시 +3 or -3 이므로 3으로 나눈 몫과 나머지를 이용
        elif i in middle:
            i = 11 if i ==0 else i
            left_dist = abs(i-l)
            right_dist = abs(i-r)
            if left_dist //3 + left_dist % 3 < right_dist // 3 + right_dist % 3:
                l = i
                answer += 'L'
            elif left_dist //3 + left_dist % 3 > right_dist // 3 + right_dist % 3:
                r = i
                answer += 'R'
            elif left_dist //3 + left_dist % 3 == right_dist // 3 + right_dist % 3:
                if hand == 'left':
                    l = i
                    answer += 'L'
                else:
                    r = i
                    answer += 'R'
    return answer