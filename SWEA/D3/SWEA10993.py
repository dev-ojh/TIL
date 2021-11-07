#군주제와 공화제
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0.0]*N for _ in range(N)]
    info = [list(map(int, input().split())) for _ in range(N)]
    parent = [0] * N
    gov = []
    for i in range(N):
        for j in range(N):
            if i != j:
                arr[i][j] = info[j][2] / ((info[i][0] - info[j][0])**2 + (info[i][1] - info[j][1])**2)
    for i in range(N):
        tmp = 0
        result = i
        for j in range(N):
            if i != j:
                if arr[i][j] > info[i][2]:
                    if tmp < arr[i][j]:
                        tmp = arr[i][j]
                        result = j
                    elif tmp == arr[i][j]:
                        result = -1
        parent[i] = result
    for i in range(N):
        if parent[i] == i:
            gov.append('K')
        elif parent[i] == -1:
            gov.append('D')
        else:
            idx = i
            while True:
                child = parent[idx]
                if parent[child] == child:
                    gov.append(child+1)
                    break
                else:
                    idx = parent[child]
    print("#{}".format(tc), *gov)