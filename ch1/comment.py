# 주석
"""
여러 줄 주석 처리
"""
'''
여러 줄 주석 처리
'''

# 화면출력 - print() / 변수 타입 확인 - type() 
print("Hello Python!!!")
print("100")
print(25.3)
print(type(100)) # <class 'int'>
print(type("100")) # <class 'str'>
print(type(100.15)) # <class 'float'>
print(type(True)) # <class 'bool'>

# sep: 문자열 사이 구분자(기본값 spacebar 없애기)
print('t','e','s','t') # t e s t
print('t','e','s','t',sep='') # test
print('t','e','s','t',sep='-') # t-e-s-t

# end: 기본값은 엔터, 줄바꿈하지 않고 연결해서 출력하고 싶을 때 사용 
print("Welcome To",end=' ')
print("the black prade")

# format: %s(문자열, 정수, 실수), %d(정수), %f(실수), %c(문자열 하나)
print("%d" % 100)
print("%5d" % 100) # 5자리 맞춰서 출력
print("%05d" % 100) # 5자리 맞춰서 출력(자릿수 없는 것은 0으로 채우기)
print()
print("%s" % "hi")
print("%5s" % "hi")
print()
print("%-8.2f" % 123.21)
print("%8.2f" % 123.21)
print("%8.2f" % 123.213456)

# 변수 선언(타입 선언 안함 - 값에 따라 타입 결정)
number=3
print("I eat %d apples" % number)
print("I eat", number, "apples")

print("%d : %s" % (1, "홍길동")) # 대입되는 것이 2개 이상이면 ()로 묶어줘야 한다.

print("I eat %s apples" % 2)
print("I eat %s apples" % 3.156)
print("I eat %s apples" % "two")

# 98% => %%
print("Error is %d%%" % 98)

# format() 함수
print("\nformat 함수 : {}")
print("{} and {}".format("You", "Me"))
print("I eat {} apples".format(3))
print("I eat {0} apples".format(3))
print("{0} and {1} and {0}".format("You", "Me")) # index 사용
print("{var1} and {var2}".format(var1="You", var2="Me"))
print("{0} and {var2}".format("You", var2="Me")) # 혼합의 형태도 가능

# 이스케이프 문자: \n, \t
print("\n줄바꿈\n연습")
print("\\ 역슬래시") # 2번 써야 역슬래시로 인식한다.
print(r"\n \t \\ 그대로 출력") # \n, \t, \\ 반영하지 않고 텍스트 자체로 출력하고 싶을 때 r을 써준다.
print("글자가 '강조'되는 효과") # 문자 표현시 "", '' 허용
print('글자가 "강조"되는 효과') # 문자 표현시 "", '' 허용
