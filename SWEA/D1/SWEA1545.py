# 주어진 숫자부터 0까지 순서대로 찍는것.
# 큰 숫자에서 작은숫자로 차례로 출력

N = int(input())

for i in range(N, -1, -1):
    print(i, end = ' ')