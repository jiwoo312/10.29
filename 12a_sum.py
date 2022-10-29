# 12a_sum.py
# 1~n 합 구하기

#1~10 합 구하기
s = 0
for x in range(1, 11):
    s = s + x
print(f'1~10합: {s}')

#1~100 합 구하기
s = 0
for x in range(1, 101):
    s = s + x
print(f'1~100합: {s}')

#1~1000합 구하기
s = 0
for x in range(1, 1001):
    s = s + x
print(f'1~1000합: {s}')
