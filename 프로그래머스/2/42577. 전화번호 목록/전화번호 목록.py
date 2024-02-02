# 시간초과
# def solution(phone_book):
#     for i in range(len(phone_book)):
#         for j in range(i+1,len(phone_book)):
#             if phone_book[i] in phone_book[j]:
#                 return bool(0)
#     return bool(1)

def solution(phone_book):
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        # 현재 번호와 다음 번호 중 작은 길이로 슬라이싱하여 비교
        min_len = min(len(phone_book[i]), len(phone_book[i + 1]))
        if phone_book[i][:min_len] == phone_book[i + 1][:min_len]:
            return False

    return True