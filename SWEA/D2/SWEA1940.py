#달려라 RC카

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    s = 0
    v = 0
    for _ in range(N):
        command = list(map(int, input().split()))
        if command[0] == 1:
            v += command[1]
            s += v
        elif command[0] == 2:
            v -= command[1]
            if v < 0:
                v = 0
            s += v
        else:
            s += v
    print('#{} {}'.format(tc, s))