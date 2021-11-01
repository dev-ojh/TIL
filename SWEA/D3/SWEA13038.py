# 교환학생

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    days = list(map(int, input().split()))
    result = 987654321
    for i in range(7):
        cnt = 0
        j = i
        day_cnt=0
        while cnt < n:
            if days[j]:
                cnt += 1
            day_cnt+=1
            j = (j+1)%7
        if day_cnt < result:
            result = day_cnt
    print('#{} {}'.format(tc, result)) 