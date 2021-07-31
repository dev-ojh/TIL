# 3 for문 사용
T = int(input())

for test_case in range(1, T + 1):
    day = int(input())
    price = list(map(int, input().split())) # 시세를 리스트로 입력받는다.
    list_length = day
    profit = 0  # 최대이익을 0으로 초기화
    
    for i in range(day):
        max_price = max(price)
        max_priceindex = price.index(max_price)
        for i in range(max_priceindex):
            profit += max_price - price[i]
        price = price[max_priceindex + 1: list_length]
        list_length = len(price)
        if list_length < 2:
            break
    
    
    print(f'#{test_case} {profit}')