# 가위바위보 문제
# 가위:1, 바위:2, 보:3 누가 이겼는지 판별
# 단 비기는 경우가 없음

A, B  = map(int, input().split())

if A - B == 1 or A - B == -2:
    print('A')
elif A - B == -1 or A - B == 2:
    print('B')