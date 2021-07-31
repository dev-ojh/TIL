# 369 게임 369가 들어갈때 -를 출력
# N이 입력되면 1~N까지 적용하여 출력하는 문제

N = int(input())

for i in range(1, N+1):
    tmp = str(i)
    tmp = tmp.replace('3', '-')
    tmp = tmp.replace('6', '-')
    tmp = tmp.replace('9', '-')
    count = tmp.count('-')
    if count == 0:
        print(i, end = ' ')
    else:
        print('-' * count, end = ' ')

    
    