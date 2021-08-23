x1 = list(map(int, input().split()))
x2 = list(map(int, input().split()))
x3 = list(map(int, input().split()))
x4 = list(map(int, input().split()))

cnt = [[0] * 101 for _ in range(102)]

for i in range(x1[1], x1[3]):
    for j in range(x1[0], x1[2]):
        cnt[i][j] = 1
for i in range(x2[1], x2[3]):
    for j in range(x2[0], x2[2]):
        cnt[i][j] = 1
for i in range(x3[1], x3[3]):
    for j in range(x3[0], x3[2]):
        cnt[i][j] = 1
for i in range(x4[1], x4[3]):
    for j in range(x4[0], x4[2]):
        cnt[i][j] = 1
result = 0
for i in range(101):
    for j in range(101):
        if cnt[i][j] == 1:
            result += 1
print(result)