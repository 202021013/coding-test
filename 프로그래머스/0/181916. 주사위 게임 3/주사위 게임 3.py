def solution(a, b, c, d):
    # 입력 값을 리스트에 저장
    origin = [a, b, c, d]
    
    # 고유한 원소를 찾음
    unique_elements = list(set(origin))
    
    # Case 1: 모든 네 개의 원소가 고유한 경우
    if len(unique_elements) == 4:
        answer = min(unique_elements)
        
    # Case 2: 세 개의 고유한 원소가 있는 경우
    elif len(unique_elements) == 3:
        # 가장 빈도가 높은 원소 찾기
        most_frequent = max(origin, key=origin.count)
        # 나머지 두 원소의 곱 계산
        other_elements = [num for num in unique_elements if num != most_frequent]
        answer = other_elements[0] * other_elements[1]
    
    # Case 3: 두 개의 고유한 원소가 있는 경우
    elif len(unique_elements) == 2:
        # 한 원소가 두 번 이상 반복되는지 확인
        if max([origin.count(num) for num in unique_elements]) > 2:
            # 가장 빈도가 높은 원소와 가장 낮은 빈도의 원소 찾기
            most_frequent = max(origin, key=origin.count)
            least_frequent = min(origin, key=origin.count)
            # 지정된 공식을 사용하여 답 계산
            answer = pow(((10 * most_frequent) + least_frequent), 2)
        else:
            # 다른 공식을 사용하여 답 계산
            answer = ((unique_elements[0] + unique_elements[1]) * abs(unique_elements[0] - unique_elements[1]))  
            
    # Case 4: 모든 원소가 동일한 경우
    elif len(unique_elements) == 1:
        answer = int(str(unique_elements[0]) * 4)
    
    return answer
