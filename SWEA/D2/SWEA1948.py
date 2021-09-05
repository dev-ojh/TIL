# 날짜 계산기

T = int(input())
for tc in range(1, T+1):
    num = list(map(int, input().split()))
    day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    result = 0
    if num[0] == num[2]:
        result += num[3]-num[1] + 1
    else:
        result += num[3] + day[num[0]]-num[1] + 1
        for i in range(num[0]+1, num[2]):
            result += day[i]
    print('#{} {}'.format(tc,result))
