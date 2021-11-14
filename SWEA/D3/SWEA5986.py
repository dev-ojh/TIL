# 세 소수
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    result = 0
    arg = 0
    for i in range(2, N):
        for k in range(2, i):
            if i % k == 0:
                break
        else:
            for j in range(2, N-i):
                for k in range(2, j):
                    if j % k == 0:
                        break
                else:
                    z = N - i - j
                    for k in range(2, z):
                        if z % k == 0:
                            break
                    else:
                        if z != 1:
                            cnt +=1
                            if i==j or i==z or j==z:
                                result += 1
                            else:
                                arg += 1
    cnt -= (result*2//3) + (arg*5//6)
    print('#{} {}'.format(tc, cnt))

