# 2개의 자연수를 입력받아 사칙연산을 수행하는 프로그램
# 두개 자연수는 1~9까지 자연수
# 사칙연산 순서로 연산한 결과 출력
# 나누기 연산 결과 소수점 이하 숫자 버림

a, b = map(int, input().split())

print(a + b)
print(a - b)
print(a * b)
print(a // b)