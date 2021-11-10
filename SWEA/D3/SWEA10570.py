#팰린드롬 수 = 회문
import math


def palendom(n):
    if n < 10:
        return 1
    else:
        tmp = n
        result = 0
        while tmp > 0:
            result = result*10 + tmp % 10
            tmp //= 10
        if n == int(result):
            return 1
        else:
            return 0


T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())
    cnt = 0
    for i in range(A, B+1):
        if math.sqrt(i) - int(math.sqrt(i)) <= 0:
            if palendom(i) and palendom(math.sqrt(i)):
                cnt += 1
    print('#{} {}'.format(tc, cnt))