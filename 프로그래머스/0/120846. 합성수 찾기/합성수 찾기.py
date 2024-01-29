def divisor(a):
    divisor_list = []
    for d in range(1,a+1):
        if a % d == 0:
            divisor_list.append(d)
    return divisor_list

def solution(n):
    answer = 0
    for i in range(1,n+1):
        if len(divisor(i)) >= 3:
            answer += 1
    return answer
