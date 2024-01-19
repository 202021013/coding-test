def solution(str1, str2):
    answer = ''
    for i,j in zip(str1,str2):   # zip() = 두 개 이상의 순회 가능한(iterable) 객체를 받아 각 객체에서 동일한 인덱스의 요소들을 순서대로 튜플로 묶어주는 내장 함수
        answer += i+j
    return answer