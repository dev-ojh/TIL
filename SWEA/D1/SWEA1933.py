# N은 1이상 1,000이하의 정수
# N의 약수를 오름차순으로 출력하라.
N = int(input())

for i in range(1,N+1):
    if N%i == 0:
        print(i,end=' ')