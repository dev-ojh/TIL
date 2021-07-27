lst=[]
for i in range(200):
    if i%7==0 and i%5!=0:
        lst.append(i)
print(*lst, sep = ',')

