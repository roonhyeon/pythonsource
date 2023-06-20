# 람다 함수
# 단일문으로 표현되는 익명함수
# 코드 상에서 한번만 사용이 되는 상황일 때 

# def square(x):
#     return x*x

# print(square(5))

square=lambda x: x*x
print(square) # <function <lambda> at 0x00000279B80C04A0>
print(square(5))

add=lambda a, b: a+b
print(add(5, 6))

# 문자열 길이 리턴 함수
def str_len(s):
    return len(s)

strings=["bob", "charles", "alexander", "teddy"]
strings.sort(key=str_len) # 정렬 기준 부여
print(strings)

strings.sort(key=lambda s:len(s))
print(strings)

# filter(함수, 리스트)
# 짝수 리스트 생성
even_list=[]

def even(arr):
    for n in arr:
        if n%2==0:
            even_list.append(n)

list1=[1,2,3,6,8,9,10,12]
even(list1)
print(even_list)

# List comprehension
even_list2=[n for n in list1 if n%2==0]
print(even_list2)

# lamda + filter
# filter(함수, 리스트)
def even2(n):
    return n%2==0 # 이 조건에 충족되는 애들만 list에 담아서 출력해줘(filter)
print(list(filter(even2, list1))) # [2,6,8,10,12]

print(list(filter(lambda n: n%2==0, list1))) # 이렇게 한 줄로 정리할 수 있게 된다.

# lamda+ map
def mul(x):
    return x**2

nums=[1,2,3,6,8,10,11,12,13,14,15]

# map(함수, 리스트)
print(list(map(mul, nums))) # [1,4,9,36,64,100,121,144,169,196,225]
print(list(map(lambda x: x**2, nums)))

# 3의 배수만 문자열로 변경한 리스트 반환
# [1, 2, '3', 4, 5, '6', 7, 8, '9', 10]
nums=list(range(1,11)) # 1~10 리스트 생성
nums_result=[]

def str_check(nums):
    for i in nums:
        if i%3==0:
            nums_result.append(str(i))
        else:
            nums_result.append(i)
    return nums_result

print(str_check(nums))

# filter, map
def str_check2(i):
    if i%3==0:
        return str(i)
    else:
        return i
print(list(map(str_check2, nums)))
print(list(map(lambda i: str(i) if i%3==0 else i, nums)))