import math

def solution(numer1, denom1, numer2, denom2):
    answer1 = numer1*denom2 + numer2*denom1
    answer2 = denom1*denom2
    gcd = math.gcd(answer1,answer2)
    return [answer1//gcd,answer2//gcd]