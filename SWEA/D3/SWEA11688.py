#Calkin-Wilf tree

T = int(input())
for tc in range(1, T+1):
    words = input()
    a, b = 1, 1
    for word in words:
        if word == 'L':
            b = a + b
        elif word == 'R':
            a = a + b
    print('#{} {} {}'.format(tc, a, b))