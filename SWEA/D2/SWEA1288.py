#양세기

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tmp = str(N)
    check = set()
    while len(check)<10:
        num = list(map(int,tmp))
        for i in num:
            check.add(i)
        tmp = str(int(tmp)+N)
    print('#{} {}'.format(tc, int(tmp)-N))