# 변수: 타입 없음, 값을 삽입할 때 타입이 결정된다.
# 타입: 숫자형 - int, float / 문자형 - str / 불 - bool / 
# 여러가지 데이터 한꺼번에 처리 - list, set, dict, tuple

# 문자열 - "", '', '''한글''', """한글"""

str1="Life is too short, You need Python"
str2='Life is too short, You need Python'
str3="""Life is too short, You need Python"""
str4='''Life is too short, You need Python'''

print(str1)
print(str2)
print(str3)
print(str4)

print()
num1=num2=10 # 2개의 변수에 같은 값 대입
print(num1, num2)

num1, num2=10, 15
print(num1, num2)
num1, num2=num2, num1 # 2개의 변수에 들어있는 값 바꾸기
print(num1, num2)

num1="한글"
print(num1)

# 한글 + 10 => 오류
# print(num1 + num2) # TypeError: can only concatenate str (not "int") to str

# 타입변환 숫자 => 문자열: str()
print(num1 + str(num2))

# 연산자
a, b=5, 4
print("a + b = %d" % (a+b))
print("a - b = %d" % (a-b))
print("a * b = %d" % (a*b))
print("a / b = %f" % (a/b)) # 스크립트와 같은 개념
print("a // b = %f" % (a//b)) # 자바와 같은 개념(몫)
print("a % b = ", (a%b))
print("a ** b = ", (a**b))

# type(): 변수 타입 확인
# str(): 문자열로 변환, int(): 숫자로 변환, float(): 실수로 변환, bool(): boolean 타입으로 변환
print(str(3.5), type(str(3.5)))
print(int(True), type(int(True)))
print(int(False), type(int(False)))
print(bool(0.1), type(bool(0.1))) # 0이 아니면 True
print(float("98.99"), type(float("98.99")))
# print(int("98.99"), type(int("98.99"))) # 오류: 소수점이 있는 것은 int로 바꿀 수 없다. 단, 쌍따음표 제거하면 가능하다.
print(int(98.99), type(int(98.99)))
print(int("98"), type(int("98")))

# 동전교환
money, c500, c100, c50, c10=0,0,0,0,0
money=7777

#500원: 15개
#100원: 2개
#50원: 1개
#10원: 2개
#나머지돈: 7원
c500=money//500
money %= 500
print("500원 : {}개".format(c500))

c100=money//100
money %= 100
print("100원 : {}개".format(c100))

c50=money//50
money %= 50
print("50원 : {}개".format(c50))

c10=money//10
money %= 10
print("10원 : {}개".format(c10))

print("나머지돈: {}원".format(money))

# ||, &&, ! => 못 씀 ==> or, and, not
a, b, c=100, 60, 15
print("and : ", a>b and a>c)
print("or : ", a>b or a>c)
print("not : ", not(a>b))
