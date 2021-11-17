#민석이의 과제 체크
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    result =[]
    for i in range(1, N+1):
        if i not in arr:
            result.append(i)
    print('#{}'.format(tc), *sorted(result))