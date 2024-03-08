# def solution(array, commands):
#     answer = []
#     for i in commands:
#         answer += array[i[0]-1:i[1]-1]
#         sorted.answer()
#     return answer

def solution(array, commands):
    answer = []
    
    for command in commands:
        i, j, k = command
        # 배열을 자르고 정렬하여 k번째 원소를 구하여 answer에 추가
        answer.append(sorted(array[i-1:j])[k-1])
    
    return answer