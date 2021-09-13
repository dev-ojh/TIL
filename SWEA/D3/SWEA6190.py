#단조 증가수 판별(십의자리 한자리 낮아질때 각 자리수가 크거나 같아지는 경우)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    result = 0
    for i in range(N-1):
        for j in range(i+1, N):
            tmp = num_list[i] * num_list[j]
            while tmp > 0:
                k = tmp % 10
                tmp //= 10
                if k >= tmp % 10:
                    continue
                else:
                    break
            if tmp <= 0:
                if result < num_list[i] * num_list[j]:
                    result = num_list[i] * num_list[j]
    if result == 0:
        result = -1
    print(f'#{tc} {result}')