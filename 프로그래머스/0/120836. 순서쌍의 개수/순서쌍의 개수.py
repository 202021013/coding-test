def solution(n):
    answer =0 
    for i in range(n):
        if n % (i+1) ==0: # 약수의 개수
            answer +=1
    return answer