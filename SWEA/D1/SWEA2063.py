N = int(input())
number = list(map(int, input().split()))

numbers = sorted(number)

print(numbers[len(number)//2])