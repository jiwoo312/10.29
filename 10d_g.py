# 10d_g.py
# 1~100 숫자 맞히기

import random
c = 0
#1~100 사이의 난수
com = random.randint(1,100)
#시도 횟수 변수 c 초기화

while True:
    u = int(input('1~100사이의 수: '))
    c = c + 1
    if u < com:
        print('up')
    elif u > com:
        print('Down')
    else:
        print('정답!')
        break

print(f'시도수:{c}번')     
    
