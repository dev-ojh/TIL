#모음이 보이지 않는 사람
T = int(input())

for tc in range(1, T+1):
    words = input()
    result =''
    tmp = ['a', 'e', 'i', 'o', 'u']
    for i in words:
        if i not in tmp:
            result += i
    print('#{} {}'.format(tc, result))