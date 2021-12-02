#성공적 공연기획
T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input()))
    # print(arr)
    p1 = arr[0]
    result = 0
    for i in range(1, len(arr)):
        if i > p1:
            result += i - p1
            p1 += i - p1
        p1 += arr[i]
    print('#{} {}'.format(tc, result))