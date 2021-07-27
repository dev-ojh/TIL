cha = input()

if ord(cha)>=65 and ord(cha)<91:
    print(f'{cha}(ASCII: {ord(cha)}) => {chr(ord(cha)+32)}(ASCII: {ord(cha)+32})')
elif ord(cha)>=97 and ord(cha)<123:
    print(f'{cha}(ASCII: {ord(cha)}) => {chr(ord(cha)-32)}(ASCII: {ord(cha)-32})')
else :
    print(cha,ord(cha))