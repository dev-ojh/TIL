# 학점 계산기
# 중간 35% 기말 45% 과제 20%
# 학생수/10명에게 동일평점 평점이 총 10개
# A+ A0 A- B+ B0 B- C+ C0 C- D0
# K번째 학생의 학점은?
# N은 10의배수만입력된다함

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N , K = map(int, input().split())
    total_list = []

    for i in range(N):  # 한명의 점수를 입력받아 합계점수 리스트를 받고 K번째 학생의 점수 기록
        mid_test, fin_test, hws = map(int, input().split())
        total_list.append(mid_test * 0.35 + fin_test * 0.45 + hws * 0.2)
        if i == K - 1:
            record = total_list[i]
       
    result = sorted(total_list, reverse = True) # 점수 내림차순으로 정렬
    for i in range(N):  #K번째 학생의 학점을 순위화 하여 확인
        if record == result[i]:
            rank = i // (N / 10) #K번째 학생이 학점 순서중 몇번째 위치할지 확인
            break
    if rank == 0: # 확인된 순위에 따른 학점 출력
        print(f'#{test_case} A+')
    elif rank == 1:
        print(f'#{test_case} A0')
    elif rank == 2:
        print(f'#{test_case} A-')
    elif rank == 3:
        print(f'#{test_case} B+')
    elif rank == 4:
        print(f'#{test_case} B0')
    elif rank == 5:
        print(f'#{test_case} B-')
    elif rank == 6:
        print(f'#{test_case} C+')
    elif rank == 7:
        print(f'#{test_case} C0')
    elif rank == 8:
        print(f'#{test_case} C-')
    else:
        print(f'#{test_case} D0')    


