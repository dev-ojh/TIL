#다이아 장식
T = int(input())
for tc in range(1, T+1):
    words = input()
    row = len(words)*4 + 1
    arr = [['.'] * row for _ in range(5)]
    for i in range(5):
        if i % 4 == 0:
            for j in range(2, row, 4):
                arr[i][j] = '#'
        elif i % 2 == 1:
            for j in range(1, row, 2):
                arr[i][j] = '#'
        else:
            k = 0
            for j in range(row):
                if j % 4 == 0:
                    arr[i][j] = '#'
                elif j % 2:
                    pass
                else:
                    arr[i][j] = words[k]
                    k += 1
    for i in range(5):
        for j in range(row):
            print(arr[i][j], end='')
        print()