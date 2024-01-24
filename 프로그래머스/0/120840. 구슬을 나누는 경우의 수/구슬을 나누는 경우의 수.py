def factorial(num):
    result = 1
    for i in range(1,num+1):
        result *= i
    return result

def solution(balls, share):
    return factorial(balls) / (factorial(balls - share) * factorial(share))