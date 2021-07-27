number = int(input())

for i in range(number):
    if number%(i+1)==0:
        print(f'{i+1}(은)는 {number}의 약수입니다.')
