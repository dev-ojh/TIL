# 최대성적표
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt_sum = sum(sorted(arr, reverse=True)[:K])
    print('#{} {}'.format(tc, cnt_sum))
