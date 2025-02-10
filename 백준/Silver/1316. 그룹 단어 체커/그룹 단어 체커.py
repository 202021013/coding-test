N = int(input())
count = 0

for _ in range(N):
    word = input()
    save = set() # 중복제거 효율성 높이기
    prev = ''
    is_group_word = True
    
    for char in word:
        if char != prev: # 연속된 단어가 x
            if char in save: # 이전의 나온 단어라면
                is_group_word = False
                break
            save.add(char)
        prev = char

    if is_group_word:
        count += 1

print(count)