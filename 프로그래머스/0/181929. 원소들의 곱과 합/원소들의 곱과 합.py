def solution(num_list):
    m = 1
    s = 0
    for i in num_list:
        m *= i
        s += i
    if m < s**2:
        return 1
    else:
        return 0
        