# 구독자 전쟁

T = int(input())
for tc in range(1, T+1):
    N, A, B = map(int, input().split())
    min_cnt = A+B-N if A+B > N else 0
    print('#{} {} {}'.format(tc, min(A, B), min_cnt))
