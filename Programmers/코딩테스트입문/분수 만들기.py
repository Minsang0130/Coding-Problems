import math


def solution(numer1, denom1, numer2, denom2):
    if denom1 % denom2 == 0:
        m_num = denom1 // denom2
        numer2 *= m_num
        denom2 *= m_num
    elif denom2 % denom1 == 0:
        m_num = denom2 // denom1
        numer1 *= m_num
        denom1 *= m_num
    else:
        numer1 *= denom2
        temp = denom1
        denom1 *= denom2
        numer2 *= temp
        denom2 *= denom1

    numer, denom = numer1 + numer2, denom1

    # 기약분수로 변환
    gcd = math.gcd(numer, denom)  # 최대공약수
    numer //= gcd
    denom //= gcd

    return [numer, denom]
