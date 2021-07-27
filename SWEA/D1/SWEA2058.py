N = int(input())
total = 0
for i in range(N):
    total += N%10
    N = N//10
    if N < 1:
        break
print(total)
