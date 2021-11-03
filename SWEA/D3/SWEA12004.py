#구구단1
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    result = 'No'
    for i in range(1, 10):
        if N % i == 0:
            if N//i < 10:
                result = 'Yes'
                break
    print('#{} {}'.format(tc, result))