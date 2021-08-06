#10개 수를 입력받아, 최대수와 최소수를 제외한 나머지 평균값 출력

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    number = list(map(int, input().split()))
    min = 10000
    max = 0
    total = 0
    for num in number:
        total += num
        if num < min:
            min = num
        if num > max:
            max = num
    total -= max+min
       
    average = round(total/8)

    print(f'#{test_case} {average}')