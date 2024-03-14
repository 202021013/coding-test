def solution(numbers):
    answer = ''
    # 숫자를 문자열로 변환하여 저장할 리스트
    str_numbers = list(map(str, numbers))
    # 각 숫자를 문자열로 변환한 뒤, 두 수를 이어붙여 비교하여 정렬합니다.
    str_numbers.sort(key=lambda x: x*3, reverse=True)
    # 만약 결과가 "0"으로 시작한다면, 모든 숫자가 0인 경우이므로 "0"을 반환합니다.
    return str(int(''.join(str_numbers)))