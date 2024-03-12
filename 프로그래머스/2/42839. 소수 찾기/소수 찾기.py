from itertools import permutations

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    number_list = list(numbers)
    
    # numbers로 나오는 숫자 만듬.
    candidate_set = set()
    for i in range(1, len(number_list) + 1):
        permutations_list = permutations(number_list, i)
        for p in permutations_list:
            candidate_set.add(int(''.join(p)))
    
    # 그 숫자들에서 소수만 뽑아서 리스트에 담음.
    prime_list = [num for num in candidate_set if is_prime(num)]
    
    # 그 리스트에 들어있는 수 갯수.
    answer = len(prime_list)
    return answer