# 수 이어가기 뒤의 숫자가 추가될 숫자의 앞 2번째에서 앞 1번째를 빼서 양수일때 수가 추가될때 최대 길이는?!

N = int(input())
max_length = 0
arr = [N]
for i in range(N, 0, -1):
    arr.append(i)
    while arr[-2] >= arr[-1]:
        arr.append(arr[-2] - arr[-1])
    if max_length < len(arr):
        max_length = len(arr)
        result = arr
    arr = [N]
print('{}'.format(max_length))
print(*result)
