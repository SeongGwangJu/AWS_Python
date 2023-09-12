# def(define) -> 함수를 정의한다.
# 오버로딩 X :같은 이름의 함수는 그냥 재정의 될 뿐
def add(x, y):
    result = x + y
    return result


#
def add(a, b, c):
    return a + b + c


# 여러개의 매개변수, 여러개의 리턴은 튜플자료형으로 정의되어진다.
def add(*a):
    print(type(a))
    return a, 10



r = add(20, 10, 5, 30, 40)
r2 = list(add(20, 10, 5, 30, 40))
# 또는 return에 list(a)를 하면 리스트로 변하겠지?
print(r)
print(r2)


# **이면 딕셔너리 자료형으로 매개변수를 변환해준다.
def sub(**data):
    print(type(data))
    print(data)


# sub(a=1, b=2)
# sub({"a": 1, "b": 2})


# 함수 선언 및 디폴트값 설정
# 디폴트값이 없는 애들은 앞으로 온다
def connection(servername, password, ip="127.0.0.1", port="8080",
               username="root"):
    print(f"ip: {ip}")
    print(f"port: {port}")
    print(f"servername: {servername}")
    print(f"username: {username}")
    print(f"password: {password}")

    # 값을 넣어줌
connection(servername="test_server", password="1q2w3e4r", port="3306")

a = 3

def multi(a):
    return a ** 2

a = multi(a)
print(a)

# 전역변수
def div():
    global a
    a = a / 10
div()
print(a)

def add2(a,b):
    return a + b
print(add2(10,20))

# 파이썬에서 람다는 무조건 한줄로 선언 가능
add2= lambda a,b : a + b + 1
print(add2(0,20))