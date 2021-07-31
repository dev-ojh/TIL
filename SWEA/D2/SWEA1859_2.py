# 2 while문 사용
T = int(input())

for test_case in range(1, T + 1):
    day = int(input())
    price = list(map(int, input().split())) # 시세를 리스트로 입력받는다.
    list_length = day
    profit = 0  # 최대이익을 0으로 초기화

    
    while list_length > 1:
        max_price = max(price)
        max_priceindex = price.index(max_price)
        if max_priceindex == 0:
            continue
        
        for i in range(max_priceindex):
            profit += max_price - price[i]
        
        price = price[max_priceindex + 1: list_length]
        list_length = len(price)
    
    print(f'#{test_case} {profit}')