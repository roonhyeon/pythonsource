# 파이썬 자료형
# 1. 문자열
# "", '', """""", ''''''

# + : 결합
print("Python "+"is fun")

# * : 복제
print("Python"*3)

print("*"*50)
print("내 프로그램")
print("*"*50)

# 1) 인덱싱: 문자열은 인덱스 값을 가지고 있음(0부터 시작)

str1="Life is too short"
print(str1[3])

# 2) 슬라이싱: [시작위치:끝위치] => 끝 위치는 포함하지 않는다.
print("str1[2:6]", str1[2:6])
print("str1[:6]", str1[:6]) # 시작위치 지정하지 않은 경우 0
print("str1[:]", str1[:]) # 위치 지정하지 않은 경우 0~끝
print("str1[:-4]", str1[:-4]) # -값은 오른쪽 끝에서부터 위치를 잡는 경우 -1부터 시작

# 3) len(): 길이 함수
print("str1 길이", len(str1))

str2="20230615Sunny"
# 년도, 날씨를 구별해서 변수에 담기
date=str2[:8]
weather=str2[8:]
print(date, weather)

# date 변수에 담긴 값을 년-월-일
year=str2[:4]
month=str2[4:6]
day=str2[6:8]
print(year, month, day, sep="-")

# 주민등록번호 001205-3234567
# 남자(1,3) / 여자(2,4) 출력
str3="001205-3234567"
no=str3[7]
# no가 1 or 3 남, 2 or 4 여
if no == "1" or no == "3":
    print("남")
elif no == "2" or no == "4":
    print("여")

if int(no) % 2 == 1:
    print("남")
else:
    print("여")

str1 = "대한민국"
for s in str1:
    print(s+"$", end="") # 대$한$민$국$
    print()

# 입력받은 숫자만큼 하트 출력
# 54321
# ♥♥♥♥♥
# ♥♥♥♥
# ♥♥♥
# ♥♥
# ♥
# numnum=input("숫자 입력: ")
# for i in range(len(numnum)):
#    for j in range(int(numnum[i])):
#        print("♥", end="")
#    print()

# 2. 문자열 관련 함수
# 1) count
print("\n문자열 관련 함수")
str1="hobby"
print("원본 문자열에 포함된 특정 문자 개수 ", str1.count("b"))

str1="python is best choice"
# 2) find(): 찾는 문자가 없는 경우 -1 반환
print("찾는 문자의 시작 위치 반환", str1.find("b"))
print("찾는 문자의 시작 위치 반환", str1.find("k"))
print("찾는 문자의 시작 위치 반환", str1.find("i", 10)) # 10번자리 위치부터 찾아줘
print("찾는 문자의 시작 위치 반환", str1.rfind("i"))

# 3) index(): 못 찾는 경우 ValueError 발생
print("찾는 문자의 시작 위치 반환", str1.index("b"))
# print("찾는 문자의 시작 위치 반환", str1.index("k"))

# 4) startswith() / endswith(): 특정 문자열로 시작하는지 / 끝나는지
print(str1.startswith("p"))
print(str1.endswith("p"))

# 5) join()
str2=","
print("문자열 삽입", str2.join("abcde"))

# 6) upper() / lower()
print("대문자", "abcdef".upper())
print("소문자", "ABCDEF".lower())

# 7) swapcase(): 대문자 -> 소문자, 소문자 -> 대문자
str1="Python is Easy"
print(str1.swapcase())

print("abc"=="ABC") # false

# 8) 공백 제거: 왼쪽, 오른쪽, 양쪽
str1="      hi"
print(str1)
print("왼쪽 공백 제거", str1.lstrip())

str1="hi     "
print(str1)
print("오른쪽 공백 제거", str1.rstrip())

str1="    hi    "
print(str1)
print("양쪽 공백 제거", str1.strip())

# 9) replace()
str1="Life is too short"
print("특정 문자열 변경", str1.replace("Life", "Your leg"))

# 10) split() => [](리스트)로 반환
print(str1.split()) # ['Life', 'is', 'too', 'short']

a="abcd"
print(a.split()) # ['abcd']

a="a:b:c:d"
print(a.split(":")) # ['a', 'b', 'c', 'd']

a="하나\n둘\n셋"
print(a.splitlines()) # ['하나', '둘', '셋']
print(a.split()) # ['하나', '둘', '셋']

# 11) 문자열 구성 파악: isdigit(), isalpha(), isalnum(), islower(), isupper()
print("12345".isdigit()) # 숫자로만 구성되어 있느냐?
print("12345".isalpha()) # 알파벳으로 구성되어 있느냐?
print("12345".isalnum()) # 알파벳+숫자로 구성되어 있느냐?
print("12345".islower()) # 소문자로만 구성되어 있느냐?
print("12345".isupper()) # 대문자로만 구성되어 있느냐?

# 12) 사이트별 비밀번호를 만들어 주는 프로그램
# https://www.naver.com
# 규칙1: https://www. 제외 => naver.com
# 규칙2: 처음 나오는 . 이후 부분은 제외 => naver
# 규칙3: 남은 글자 중 처음 3자리 + 글자개수 + 글자 내 e 개수 + ! 구성
# 완성된 비밀번호: nav51!
url="https://www.naver.com"
str1=url[12:]
# url=url.replace("https://www.", "")
str2=str1[:5]
# idx=url.find(".")
# url=url[:idx]
# => url=url[:url.find(".")]
str3=str2[:3]+str(len(str2))+str(str2.count("e"))+"!"
print(str3)
