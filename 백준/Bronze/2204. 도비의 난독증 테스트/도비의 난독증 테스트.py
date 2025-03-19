import sys

# 1. 입력받기
while True:
    n = int(sys.stdin.readline().strip())
    if n == 0: # 0 만날 때 까지 반복
        break

    words = [sys.stdin.readline().strip() for _ in range(n)]
    # 2. 대소문자 무시하고 정렬하기
    words.sort(key=str.lower)
    
    # 3. 가장 첫번째 단어 출력하기
    print(words[0])
