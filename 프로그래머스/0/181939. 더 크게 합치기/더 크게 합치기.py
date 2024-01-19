def solution(a, b):
    a = str(a)
    b = str(b)
    if a+b > b+a:
        return int(a+b)
    elif a+b < b+a:
        return int(b+a)
    else:
        return int(a+b)

