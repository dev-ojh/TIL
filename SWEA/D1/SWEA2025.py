# 1부터 주어진 숫자만큼 모두 더한 값을 출력

N = int(input())    # 입력받는 N값
total = 0       # 합계를 저장하기 위해 초기화
for i in range(1, N+1): #N까지 더하기 위해 반복문 진행
    total += i  #합계에 누적해서 저장

print(total)