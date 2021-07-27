cha = input()

if ord(cha)>=97 and ord(cha)<122:
    print(f'{cha} 는 소문자 입니다.')
elif ord(cha)<91 and ord(cha)>=65 :
    print(f'{cha} 는 대문자 입니다.')
else :
    print(f'{cha} 는 알파벳이 아닙니다.')
