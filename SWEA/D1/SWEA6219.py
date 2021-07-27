number = int(input())
cnt = 0

for i in range(number):
    if number%(i+1)==0:
        print(f'{i+1}(은)는 {number}의 약수입니다.')
        cnt +=1
if cnt == 2 :
    print(f'{number}(은)는 1과 {number}로만 나눌 수 있는 소수입니다.')