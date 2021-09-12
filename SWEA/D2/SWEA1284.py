# 수도요금 계산

T = int(input())

for tc in range(1, T+1):
    P, Q, R, S, W = map(int,(input().split()))
    spend_A = P * W
    if W > R:
        spend_B = Q + (W - R) * S
    else:
        spend_B = Q
    if spend_A > spend_B:
        result = spend_B
    else:
        result = spend_A
    
    print(f'#{tc} {result}')