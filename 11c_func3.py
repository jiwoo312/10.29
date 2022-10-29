# 11c_func3.py
# 결과값이 있는 함수

def square(a):
    c = a * a
    return c

# 밑변이 b, 높이가 h인 삼각형 넓이 구하는 함수
def tri(b, h):
    a = b * h / 2
    return a
# 두 수의 합을 구하는 add 함수
def add(n1, n2):
    s = n1 + n2
    return s

# 가로 w, 세로 h사각형 넓이 구하는 rect 함수
def rect(w, h):
    a = w * h
    return a
s1 = 4
s2 = square(s1)
print(s1, s2)

a = tri(3, 4)
print(a)

s = add(5, 10)
print(s)

a = rect(5, 10)
print(a)

