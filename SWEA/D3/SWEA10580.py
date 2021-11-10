#전봇대
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N-1):
        for j in range(i+1, N):
            if arr[i][0] < arr[j][0] and arr[i][1] > arr[j][1]:
                cnt += 1
            elif arr[i][0] > arr[j][0] and arr[i][1] < arr[j][1]:
                cnt += 1
    print('#{} {}'.format(tc, cnt))