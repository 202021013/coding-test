def solution(my_string):
    # 결과를 저장할 52개의 원소를 가진 배열 초기화
    count_array = [0] * 52
    
    # 문자열을 순회하면서 알파벳 개수 카운트
    for char in my_string:
        # 대문자인 경우
        if 'A' <= char <= 'Z':
            count_array[ord(char) - ord('A')] += 1
        # 소문자인 경우
        elif 'a' <= char <= 'z':
            count_array[ord(char) - ord('a') + 26] += 1
    
    return count_array
