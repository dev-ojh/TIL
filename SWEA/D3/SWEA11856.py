# 알파벳 문자열 중 같은 문자가 2개씩 있는지 확인

T = int(input())
for tc in range(1, T+1):
    S = input()
    first = [S[0]]
    second = []
    result = 'No'
    for i in range(1, 4):
        if S[i] in first:
            first.append(S[i])
        elif len(second) == 0 or S[i] in second:
            second.append(S[i])
        else:
            break
    if len(first) == len(second) == 2:
        result = 'Yes'
    print('#{} {}'.format(tc, result))