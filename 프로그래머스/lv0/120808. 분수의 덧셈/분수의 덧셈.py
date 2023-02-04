from fractions import Fraction
def solution(numer1, denom1, numer2, denom2):
    answer = []
    def gcd(a, b):
        if a < b:
            a, b = b, a
        if a % b == 0:
            return b
        return gcd(b, a % b)
    m, s = denom1 * denom2, numer1 * denom2 + numer2 * denom1
    g = gcd(m, s)
    m //= g
    s //= g
    return s, m