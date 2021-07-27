game = ["가위","바위","보"]

Man1 = input()
Man2 = input()

for i in range(3):
    if game[i]==Man1:
        Man1id = i
for i in range(3):
    if game[i]==Man2:
        Man2id = i

if Man1id-Man2id==1:
    print('Result : Man1 Win!')
elif Man1id-Man2id==0:
    print('Result : Draw')
else :
    print('Result : Man2 Win!')