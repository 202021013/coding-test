def solution(s):
    count_num = 0
    # '('나오면 +1 ')'나오면 -1해서 0되면 true로!!
    for i in s:
        if i == '(':
            count_num += 1
        elif i == ")":
            count_num -= 1
        if count_num < 0:      # 음수로 시작하면 )로 해서 안됨
            return False
        
    if count_num == 0:
        return True
    else:
        return False