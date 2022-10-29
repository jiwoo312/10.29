# 12b_sum.py
# 1~n 합 구하기

# 1~n 합 구하기
def sum_n(n):
    s = n
    for x in range(1,n+1):
        s = s + x
        return s

# 1~10 까지 합 구하기
s = sum_n(10)
print(s)

# 1~100 까지 합 구하기
s = sum_n(100)
print(s)

# 1~1000 까지 합 구하기
s = sum_n(1000)
print(s)
