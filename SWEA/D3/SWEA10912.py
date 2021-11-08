#외로운 문자

T = int(input())
for tc in range(1, T+1):
    words = input()
    check = [0] * len(words)
    result = []
    fin = ''
    for i in range(len(words)-1):
        if not check[i]:
            for j in range(i+1, len(words)):
                if words[i] == words[j]:
                    check[j] = 1
                    break
            else:
                result.append(words[i])
    if check[-1] == 0:
        result.append(words[-1])
    for i in range(len(result)-1):
        for j in range(i+1, len(result)):
            if result[i] > result[j]:
                result[i], result[j] = result[j], result[i]
    for i in range(len(result)):
        fin += result[i]
    if len(fin) == 0:
        fin = 'Good'
    print('#{} {}'.format(tc, fin))
