# 1부터 주어진 횟수까지 2를 곱한 값들을 출력
# 2를 몇번 제곱했는지 리스트를 출력하는 문제.

N = int(input())

for i in range(N + 1):  # 주어진횟수까지 2의 제곱이므로
    print(2**i, end = ' ')  # space하나씩 띄어 출력