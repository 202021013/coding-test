def solution(number, k):
    stack = []

    for digit in number:
        # 스택이 비어있지 않고, 스택의 top이 현재 숫자보다 작으며, 아직 제거할 숫자가 남아 있다면 pop
        while stack and stack[-1] < digit and k > 0:
            stack.pop()
            k -= 1
        
        # 현재 숫자를 스택에 추가
        stack.append(digit)

    # 제거할 숫자가 남아있다면 스택에서 뒤에서부터 남은 숫자만큼 pop
    while k > 0:
        stack.pop()
        k -= 1

    answer = ''.join(stack)
    return answer
