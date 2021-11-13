# USB꽂기
T = int(input())
for tc in range(1, T+1):
    p, q = map(float, input().split())
    s1 = (1-p) * q
    s2 = p*(1-q) * q
    if s1 < s2:
        print('#{} YES'.format(tc))
    else:
        print('#{} NO'.format(tc))