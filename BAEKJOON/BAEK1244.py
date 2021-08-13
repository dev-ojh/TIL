
switch_cnt = int(input())
switch_list = list(map(int, input().split()))

stu_cnt = int(input())
stu_list = [list(map(int, input().split())) for _ in range(stu_cnt)]

for i in range(stu_cnt):
    sex = stu_list[i][0]
    position = stu_list[i][1] - 1
    if sex == 1:
        for j in range(position, switch_cnt, position + 1):
            switch_list[j] = (switch_list[j] + 1) % 2
        
    else:
        k = 1
        switch_list[position] = (switch_list[position] + 1) % 2
        
        while True:
            if position + k < switch_cnt and position - k > -1:
                if switch_list[position + k] == switch_list[position - k]:
                    switch_list[position + k] = (switch_list[position + k] + 1) % 2
                    switch_list[position - k] = (switch_list[position - k] + 1) % 2
                    k += 1
                else: break
            
            else:
                break
            
    
    i = 0
while i < switch_cnt:
    if i == switch_cnt - 1:
        print(switch_list[i])
        i += 1
    else:
        print(switch_list[i], end=' ')
        i += 1
        if i % 20 == 0:
            print()
    