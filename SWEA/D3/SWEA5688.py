#세제곱근찾기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    if abs(N**(1/3) - round(N**(1/3))) < 0.0000001:
        result = round(N**(1/3))
    else:
        result = -1
    print('#{} {}'.format(tc, result))
