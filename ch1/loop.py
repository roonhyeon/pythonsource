# 반복문
# while, for

# 1~10 출력
i=1
while i<11:
    print(i, end=" ")
    i+=1

print()

# 1~100 짝수만 출력
i=1
while i<=100:
    if i%2==0:
        print(i, end=" ")
    i+=1

print()

# i++은 파이썬에서는 불가
# 구구단 3단 출력
i=1
while i<10:
    print("{} * {} = {}".format(3, i, 3*i))
    i+=1

# range(시작값, 종료값(필수), 증감값): 범위 지정
print(range(5)) # range(0, 5) => 0~4
print(list(range(1,5))) # [1, 2, 3, 4]
print(list(range(0,10,2))) # [0, 2, 4, 6, 8]

# in: 연산기호, 포함의 의미
print("in 기호")
print("y" in "python") # True
print("k" not in "python")

# for
for i in range(1,101):
    print(i, end=" ")
