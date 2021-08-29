
for tc in range(1, 11):
    len_rec = int(input())
    
    cnt = 0
    arr = [list(map(int, input().split())) for _ in range(len_rec)]
    for i in range(len_rec):
        result = []
        for j in range(len_rec):
            if arr[j][i]:
                result.append(arr[j][i])
        
        while result:
            if result[0] == 2:
                result.pop(0)
            if result[-1] == 1:
                result.pop()
            if result[0] == 1 and result[-1] == 2:
                break
        for k in range(len(result)-1):
            if result[k] == 1 and result[k+1] == 2:
                cnt += 1
    print('#{} {}'.format(tc, cnt))





            
