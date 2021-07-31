# 연속된 N일동안 물건 매매가를 알고 있다.
# 하루에 최대 하나만 구입할 수있다.
# 판매는 얼마든지 할수 있다. 각 케이스별 최대 이익출력

# 1 재귀함수 사용
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
def find_profit(price, profit):
    
    max_priceindex = price.index(max(price))
    
    for i in range(max_priceindex):
        profit += max(price) - price[i] 
    new_list = price[max_priceindex + 1 : -1]
    result = profit
    if len(new_list) < 2:
        return result
    else :
        return find_profit(new_list, result)

for test_case in range(1, T + 1):
    day = int(input())
    price = list(map(int, input().split())) # 시세를 리스트로 입력받는다.
    
    profit = 0  # 최대이익을 0으로 초기화
    result = find_profit(price, profit)

    print(f'#{test_case} {result}')
