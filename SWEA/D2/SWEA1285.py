# 아름이의 돌던지기
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    min_result = 100001
    cnt = 0
    for i in range(N):
        if abs(arr[i]) <= min_result:
            min_result = abs(arr[i])
    for i in range(N):
        if abs(arr[i]) == min_result:
            cnt += 1
    print(f'#{tc} {min_result} {cnt}')
            