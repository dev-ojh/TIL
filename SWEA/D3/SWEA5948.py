# 7-3-5게임

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    result = []
    for i in range(5):
        for j in range(i+1, 6):
            for k in range(j+1, 7):
                result.append(arr[i] + arr[j] + arr[k])
    print('#{} {}'.format(tc, sorted(set(result))[-5]))