# 파이썬 자료형
# 3. 리스트(자바 배열, List와 같은 개념): []

# 1) 리스트 생성: 데이터는 아무거나 가능
list1=[]
list2=["a", 1, 3.15, True]
print(list1)
print(list2)
list3=["a", 1, 3.15, True, ["b", 35, 45]]
print(list3)

# 2) 리스트 인덱싱
print(list2[0])
print(list2[2])
print(list2[-1])
print(list3[-1])
print(list3[-1][1])

# 3) 리스트 슬라이싱
print(list2[0:2])
print(list3[:-1])
print(list3[4:]) # [['b', 35, 45]]
print(list3[4]) # ['b', 35, 45]
print(list3[4][:2]) # ['b', 35]

# 4) is 문자열 찾기
list4=[1, 2, ["a", "b", ["Life", "is"]]]
print(list4[2][2][1])
print(list4[-1][-1][-1])

# 5) + : 연결의 의미
a=[1, 2, 3]
b=[4, 5, 6]
print(a+b)
print(a[0]+b[1])

# 6) * : 반복
print(a*3)

# 7) 리스트 특정 요소 수정
a[1]=7
print(a)

a[2]="Life"
print(a)

b[1:2]=[10, 11]
print(b)

b[1]=[15, 16, 17]
print(b)

# 8) 리스트 요소 삭제
del b[1]
print(b)

b[0:1]=[]
print(b)

numbers=[273, 103, 5, 32, 65, 9, 72, 800, 99]
for number in numbers:
    if number >= 100:
        print("100 이상의 수 ", number)

# 273은 3자릿수입니다.
# 103은 3자릿수입니다.
# 5는 1자릿수입니다.
for num in numbers:
    print("{}은 {}자릿수입니다.".format(num, len(str(num))))

# 9) (): 튜플
list4=list([1,2,3])
print(list4)

# 4. 리스트 함수
# 1) append(): 리스트 뒤에 요소 추가
list4.append(5)
print(list4)
list4.append([6,7,8])
print(list4)

# 2) sort()
print("정렬 전 ", numbers)
numbers.sort() # 오름차순 정렬
print("정렬 후 ", numbers)

alpha=["a", "z", "c", "b", "f"]
alpha.sort()
print("정렬 후 ", alpha)

alpha=["a", "z", "A", "b", "D", "f"]
alpha.sort() # 대문자 우선 출력
print("정렬 후 ", alpha)

han=["호랑이", "강아지", "원숭이", "고양이"]
han.sort()
print("정렬 후 ", han)

numbers=[273, 103, 5, 32, 65, 9, 72, 800, 99]
numbers.sort(reverse=True) # 내림차순 정렬
print("정렬 후 ", numbers)

# 3) reverse(): 리스트 뒤집기
han.reverse()
print("reverse 후 ", han)

# 4) index(찾고자 하는 요소)
print(han[0])
print(han.index("호랑이"))

# 5) insert(위치, 요소)
han.insert(1, "악어")
print("insert 후 ", han)

# 6) remove(삭제할 요소)
han.remove("고양이")
print("remove 후 ", han)

# 7) pop(): 리스트 요소 중 마지막 요소 날리기
han.pop()
print("pop 후 ", han)
han.pop(1)
print("pop 후 ", han)

# 8) count()
a=[1, 2, 3, 1]
print("리스트에 포함된 1의 개수 ", a.count(1))

# 9) clear()
a.clear()
print("clear 후 ", a)

# 10) 리스트 안의 요소가 비어있는 경우 False
list6=[]
if list6:
    print("True")
else:
    print("False") # 비어있으면 false

str=""
if str:
    print("True")
else:
    print("False") # 비어있으면 false

# 11) in
print("p" in "python") # TrueB

fruits=["사과", "배", "포도", "자몽"]
print("사과" in fruits)
print("메론" not in fruits)

# 리스트 출력
for fruit in fruits:
    print(fruit)

print()

# 12) enumerate(): index 부여
for fruit in enumerate(fruits):
    print(fruit)

print()

# 튜플 형태가 싫을 때
for idx, fruit in enumerate(fruits):
    print(idx, fruit)

# A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
# 70, 60, 55, 75, 95, 90, 80, 85, 100, 88
# 중간고사 점수를 리스트로 생성하고, A 학급의 평균 구하기
a_class=[70, 60, 55, 75, 95, 90, 80, 85, 100, 88]

total=0
for num in a_class:
    total+=num
print("A 학급 평균 : %.2f" % (total / len(a_class)))

# sum() 이용
print("A 학급 평균 : %.2f" % (sum(a_class) / len(a_class)))

# 1~20 리스트 생성 : [1,2,3,4...]
list2=list(range(1, 21))
print(list2)

list3=[]
for x in range(1, 101):
    list3.append(x)
print(list3)

# comprehension
list3=[x for x in range(1, 101)]
print(list3)

list4=["갑", "을", "병", "정", "경"]
# '정'을 제외하고 출력
for x in list4:
    if x != "정":
        print(x)

list5=[x for x in list4 if x != "정"]
print(list5)

# 1~100 숫자 중에서 홀수만 리스트로 생성
list6=list(range(1, 101, 2))
print(list6)

list7=[]
for i in range(1, 101, 2):
    list7.append(i)
print(list7)

list8=[x for x in range(1, 101, 2)]
print(list8)

# 아래의 리스트에서 소문자만 추출해서 새로운 리스트로 생성 후 출력
list9=["A", "b", "c", "D", "e", "F", "G", "h"]

list10=[]
for x in list9:
    if x.islower():
        list10.append(x)

print(list10)

# list comprehension
list10=[x for x in list9 if x.islower()]
print(list10)

# [1,2,3,4] ==> [2,4,6,8]
print([x*2 for x in [1, 2, 3, 4]])

# [0,1,2,3,4] ==> [0, 1, 4, 9, 16]
print([x*x for x in [0, 1, 2, 3, 4]])

list1=[1,2,3]
# [[1,2,3], [2,3,4], [3,4,5]]

list2=[]

for x in list1:
    list2.append([x, x+1, x+2])

print(list2)

print([[x, x+1, x+2] for x in list1])