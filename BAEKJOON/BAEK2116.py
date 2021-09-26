# 주사위 탑 쌓기
def work(dice_num, top):
    
    if dice[dice_num][top]

    work(dice[])


N = int(input())

dice = [list(map(int, input().split())) for _ in range(N)]
(0,5) (1,3) (2,4)
for j in range(6):
    i = 0
    result = 0
    top = j
    while i < N:
        top_val = dice[i][j]
        if j == 0 or j ==5:
            bot = (j+5) % 10
        else:
            bot = (j+2) % 4
        tmp = dice[i].copy()
        tmp.remove(tmp[top], tmp[bot])
        result += max(tmp)
        i += 1
        bot = dice[i].index(top_val)
        top = 
a=[1,2,3]
b=a.copy()
b.remove(b[2])
print(b,a)