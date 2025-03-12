# 1. 0층 초기화, 누적 계산하는 함수 만들기
def apartment_residents_optimized(k, n):
    residents = list(range(1, n+1))  # 0층 초기화
    
    for _ in range(k):
        for i in range(1, n):
            residents[i] += residents[i-1]  # 이전 값 누적 합 계산
    
    return residents[-1]

# 2. T, k, n 입력받기
T = int(input())  
for _ in range(T):
    k = int(input())
    n = int(input())
    # 3. 입력받은 k, n 값을 함수에 적용하여 결과 출력하기
    print(apartment_residents_optimized(k, n))