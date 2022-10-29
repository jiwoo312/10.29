# 12d_fact.py
# factorial 함수

def fact(n):
    f = 1
    for x in range(1, n + 1):
        f = f * x
    return f
print(fact(3))
print(fact(5))
print(fact(10))



