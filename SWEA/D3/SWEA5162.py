#두빵 딜레마
T = int(input())
for tc in range(1, T+1):
    A, B, C = map(int, input().split())
    D = min(A, B)
    print('#{} {}'.format(tc, C//D))