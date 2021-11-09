#문자열 거울로 보기
T = int(input())
for tc in range(1, T+1):
    words = input()
    result = ''
    for i in range(len(words)-1, -1, -1):
        if words[i] == 'b':
            result += 'd'
        elif words[i] == 'd':
            result += 'b'
        elif words[i] == 'p':
            result += 'q'
        else:
            result += 'p'
    print('#{} {}'.format(tc, result))