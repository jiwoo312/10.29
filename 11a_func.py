# 11a_func.py
# 인사말 출력함수 hello()

#함수 정의
def hello():
    print('hello.python')

def hello2(name):
    print(f'hello {name}!')

def hello3(name, age):
    print(f'{name}님은 {age}살입니다.')
#함수 호출
hello()
hello()

hello2('kim')
hello2('park')
hello2('python')

hello3('홍길동', '100')
