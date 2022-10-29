# ch04ex01.py
#평균계산기

#합, 개수,변수 초기화
s = 0
c = 0
while True:
    score = int(input('점수를 입력하세요:'))

    if score < 0:
        break #점수가 음수면 종료

    s = s + score
    c = c + 1

print(f'{c}명의 점수 합: {s}점')
print(f'평균: {s/c}점')

    
