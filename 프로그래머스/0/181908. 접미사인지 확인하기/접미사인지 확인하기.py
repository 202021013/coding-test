def solution(my_string, is_suffix):
    for i in range(len(my_string)):
        if my_string[i:] == is_suffix:
            return 1
    return 0 # for문과 if문이 해당되지 않으면 0반환
