# 점수 최빈수 구하기

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    arr = [0]*101
    max_cnt = 0
    max_pt = 0
    for i in range(1000):
        arr[num_list[i]] += 1
    for i in range(101):
        if arr[i] >= max_cnt:
            max_cnt = arr[i]
            max_pt = i
    print(f'#{tc} {max_pt}')