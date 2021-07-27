T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    data = input()
    year = int(data[0:4])
    month = int(data[4:6])
    day =  int(data[6:8])
    if  month < 1 or month > 12:
        print(f'#{test_case} -1')
    elif month < 8:
        if month % 2 == 1:
            if day < 32 and day >0:
                print(f'#{test_case} {year:04d}/{month:02d}/{day:02d}')
            else:
                print(f'#{test_case} -1')
        elif month == 2:
            if day < 29 and day >0:
                print(f'#{test_case} {year:04d}/{month:02d}/{day:02d}')
            else:
                print(f'#{test_case} -1')
        else:
            if day < 31 and day >0:
                print(f'#{test_case} {year:04d}/{month:02d}/{day:02d}')
            else:
                print(f'#{test_case} -1')
    else:
        if month % 2 == 1:
            if day < 31 and day >0:
                print(f'#{test_case} {year:04d}/{month:02d}/{day:02d}')
            else:
                print(f'#{test_case} -1')
        else:
            if day < 32 and day >0:
                print(f'#{test_case} {year:04d}/{month:02d}/{day:02d}')
            else:
                print(f'#{test_case} -1')

