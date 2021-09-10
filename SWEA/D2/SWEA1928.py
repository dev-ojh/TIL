#Base64 Decoder
#이문제를 위해 알아야할 것. 아스키 코드로 표현된 표
# ord chr 함수
# format을 통해 이진수로 나타내면서 자릿수로 표현할수 있는것.

T = int(input())
for tc in range(1, T+1):
    string = input()
    result = str()
    finish = str()
    for i in string:
        if ord(i)==43:
            result += format(ord(i)+19, '06b')
        elif ord(i)==47 :
            result += format(ord(i)+16, '06b')
        elif ord(i)>=48 and ord(i)<=57:
            result += format(ord(i)+4, '06b')
        
        elif ord(i)>=65 and ord(i)<=90:
            result += format(ord(i)-65, '06b')
        elif ord(i)>=97 and ord(i)<=122:
            result += format(ord(i)-71, '06b')
        
    
    for i in range(0, len(result), 8):
        finish += chr(int(result[i:i+8], 2))
    
    print('#{} {}'.format(tc, finish))
    
