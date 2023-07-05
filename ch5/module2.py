# 모듈: 함수, 변수, 클래스를 모아놓은 파일

# 파이썬에서 제공하는 모듈 사용
# import 모듈명
# from 모듈명 import 사용할 함수, 클래스...

# from math import sin,cos,floor,ceil

# 특정 함수명을 지정해줬기 때문에 math.ceil 이런 식으로 안 써도 된다.
# print(ceil(3.14))
# print(sin(1))
# print(cos(1))
# print(floor(2.5))

# import 모듈명 as 별칭
import math as m
print(m.ceil(2.5))