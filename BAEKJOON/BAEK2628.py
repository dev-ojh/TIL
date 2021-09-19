# 종이 자르고 난 후 최대 넓이

row, col = map(int, input().split())
N = int(input())
row_list = [0, row]
col_list = [0, col]
max_col = 0
max_row = 0
for i in range(N):
    direction, num = map(int, input().split())
    if direction == 0:
        col_list.append(num)
    if direction == 1:
        row_list.append(num)
c = len(col_list)
r = len(row_list)
for i in range(c-1):
    for j in range(i+1, c):
        if col_list[i] > col_list[j]:
            col_list[i], col_list[j] = col_list[j], col_list[i]
for i in range(r-1):
    for j in range(i+1, r):
        if row_list[i] > row_list[j]:
            row_list[i], row_list[j] = row_list[j], row_list[i]
for i in range(c-1):
    if col_list[i+1] - col_list[i] > max_col:
        max_col = col_list[i+1] - col_list[i]
for i in range(r-1):
    if row_list[i+1] - row_list[i] > max_row:
        max_row = row_list[i+1] - row_list[i]
print(f'{max_col * max_row}')




