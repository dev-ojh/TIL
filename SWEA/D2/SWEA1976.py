#사각덧셈

T = int(input())

for tc in range(1, T+1):
    a, b, c, d = map(int, input().split())
    m = b+d
    h = a+c
    if m>59:
        m -= 60
        h += 1
    if h>12:
        h -= 12
    print('#{} {} {}'.format(tc, h, m))

