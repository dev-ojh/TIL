# 통역사 성경이
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    words = input()
    cnt = 0
    result = [0] * N
    k = 0
    i = 0
    while i < len(words):
        if 90 >= ord(words[i]) >= 65:
            j = 1
            while True:
                if 97 <= ord(words[i+j]) <= 122:
                    j += 1
                elif 65 <= ord(words[i+j]) <= 90:
                    i += j+1
                    break
                elif ord(words[i+j]) == 32:
                    cnt += 1
                    i += j+1
                    break
                elif ord(words[i+j]) == 33 or ord(words[i+j]) == 63 or ord(words[i+j]) == 46:
                    cnt += 1
                    result[k] = cnt
                    k += 1
                    cnt = 0
                    i += j + 1
                    break
                else:
                    i += j + 1
                    break
        elif ord(words[i]) == 33 or ord(words[i]) == 63 or ord(words[i]) == 46:
            i += 1
            k += 1
        else:
            i += 1
    print('#{}'.format(tc), *result)

# print(ord('a')) =>97
# print(ord('z'))=>122
# print(ord(' ')) =>32
# print(ord('!')) =>33
# print(ord('?')) =>63
# print(ord('.')) =>46

