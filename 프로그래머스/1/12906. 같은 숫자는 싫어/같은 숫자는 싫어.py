def solution(arr):
    answer =[]
    pre_ans = None
    
    for i in arr:
        if i != pre_ans: # 다음숫자랑 비교해서 똑같으면 추가안하고 다르면 추가
            answer.append(i)
            pre_ans = i
            
    return answer