# 프리셀 게임
T = int(input())
for tc in range(1, T+1):
    N, pd, pg = map(int, input().split())
    result = 'Broken'
    if pg == 100 and pd == 100:
        result = 'Possible'
    else:
        for i in range(N+1):
            if (i*pd/100) - (i*pd//100) <= 0.0:
                pg/100 *