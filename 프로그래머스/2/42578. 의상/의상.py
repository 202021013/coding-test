from collections import Counter
from functools import reduce

# reduce에 사용될 함수 정의
def multiply(x, y):
    return x * (y + 1)

def solution(clothes):
    # 의상 종류별로 갯수를 세기
    counts = Counter(category for _, category in clothes)

    # 각 종류별 의상의 갯수에 1을 더한 후 모든 종류를 곱하여 모든 의상을 입지 않은 경우까지 고려
    answer = reduce(multiply, counts.values(), 1)

    # 아무 의상도 입지 않은 경우는 제외
    return answer - 1
