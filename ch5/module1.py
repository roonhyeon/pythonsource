# 모듈: 함수, 변수, 클래스를 모아놓은 파일

# 파이썬에서 제공하는 모듈 사용
import math # 모듈 전체를 불러오기

# print(dir(math))
# print(math.ceil(3.14))
# print(math.sin(1))
# print(math.cos(1))
# print(math.floor(2.5))

import random

# 0.0 <= x < 1.0 리턴
print(random.random())
# 10 ~ 20 임의의 수 float 리턴
print(random.uniform(10, 20))
# 0 ~ 지정한 값 사이의 수(int) 리턴
print(random.randrange(10))
# 10 ~ 20 사이의 int 리턴
print(random.randrange(10, 20))
# 리스트 안의 임의의 수 리턴
print(random.choice([1,2,3,4,5,6]))

list1=list(range(10, 20))
print("생성된 리스트", list1)
# 리스트 요소를 랜덤하게 섞기
random.shuffle(list1)
print("리스트 섞은 후", list1)
# 리스트에서 임의의 숫자 k개만큼 추출
print(random.sample(list1, k=2))

import time

print("지금부터 5초 정지합니다.")
time.sleep(5)
print("프로그램 종료")




