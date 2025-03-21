import sys
import itertools

# 조합을 활용한 최대값 계산
def find_winner(N, cards):
    max_value = 0  # 가장 큰 일의 자리 값
    winner = 0  # 우승자 번호
    
    for i in range(N):
        best_value = 0  # 현재 참가자의 최댓값
        
        # 5장 중 3장을 선택하는 모든 조합을 생성
        for comb in itertools.combinations(cards[i], 3):
            value = sum(comb) % 10  # 일의 자리 값 계산
            best_value = max(best_value, value)
        
        # 최대값을 가진 참가자 출력 , 동점이면 참가자 번호가 큰 사람 출력
        if best_value > max_value or (best_value == max_value and i + 1 > winner):
            max_value = best_value
            winner = i + 1  # 1번부터 시작하므로 인덱스+1
    
    return winner

# 입력 처리
N = int(sys.stdin.readline().strip())  # 참가자 수
cards = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] # 각 참가자의 5장의 카드 숫자 입력받기

# 결과 출력
print(find_winner(N, cards))
