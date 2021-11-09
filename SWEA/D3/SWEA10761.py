#신뢰
T = int(input())
for tc in range(1, T+1):
    arr = list(input().split())
    N = int(arr[0])
    orange = []
    blue = []
    time = 0
    for i in range(1, len(arr), 2):
        if arr[i] == 'B':
            blue.append(int(arr[i+1]))
        else:
            orange.append(int(arr[i+1]))
    orange_position = 1
    blue_position = 1
    orange_time = 0
    blue_time = 0
    stack = 0
    for i in range(len(orange)):
        for j in range(len(blue)):
            if orange[i] == blue[j]:
                stack += 1
    while orange:
        tmp = orange.pop(0)
        orange_time += abs(orange_position - tmp) + 1
        orange_position = tmp
    while blue:
        tmp = blue.pop(0)
        blue_time += abs(blue_position - tmp) + 1
        blue_position = tmp
    time = max(blue_time, orange_time) + stack
    print('#{} {}'.format(tc, time))