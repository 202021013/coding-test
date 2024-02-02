# 시간초과
# def solution(phone_book):
#     for i in range(len(phone_book)):
#         for j in range(i+1,len(phone_book)):
#             if phone_book[i] in phone_book[j]:
#                 return bool(0)
#     return bool(1)


def solution(phone_book):
    phone_book.sort()  # 전화번호를 정렬하여 비교를 쉽게 함
    
    for i in range(len(phone_book) - 1):
        # 현재 번호가 다음 번호의 접두어인지 확인
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            return False 
    
    return True