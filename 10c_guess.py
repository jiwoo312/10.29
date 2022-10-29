# 10c_guess.py
# 숫자 맞히기

import random
c = 0 #시도수

#1~30 사이의 수 만들기
com = random.randint(1,30)
#print(f'com: {com}')
while True:
    u = int(input('1~30사이의 수: '))
    c = c + 1
    if u < com:
        print('up')
    elif u > com:
        print('Down')
    else:
        print('정답!')
        break

print(f'시도 수: {c}번')
    
