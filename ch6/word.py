import random
import time

words=[]

# 시도횟수, 정답 개수
n, cor_cnt=1,0

# with 구문 이용해서 word.txt 읽어서 words 리스트에 추가
# words 출력: ['policy']
with open("resource/word.txt") as f:
    for w in f:
        words.append(w.strip())

# print(words)

input("Ready? Press Enter Key")
start=time.time() # 시작 시간

while n <= 5:
    # 리스트 요소 임의로 섞기
    random.shuffle(words)

    # 리스트 요소 중 임의로 하나 추출
    q=random.choice(words)

    # 추출된 요소 화면에 출력하기
    print("Question #{}".format(n))
    print(q)
    x=input()

    print()

    if str(q).strip()==str(x).strip():
        print("Pass!!")
        cor_cnt+=1 # 정답 개수 추가
    else:
        print("Wrong!!")

    n+=1 # 문제 개수 추가

# while 문 끝난 시간
end=time.time()

# 걸린 시간
during=end-start
during=format(during, ".3f")

# 게임 시간, 정답 개수 출력 => ex) 게임시간: 3초, 정답개수: 4개
print("게임시간: {}, 정답개수: {}".format(during, cor_cnt))

# 정답 개수가 4개 이상이면 합격 메시지 출력
if cor_cnt >= 4:
    print("Pass!!")
else:
    print("Wrong!!")

# db에 저장
# 테이블 records 생성: 정답개수(cor_cnt), 기록(record), 날짜(현재 날짜와 시간)
import sqlite3
conn=sqlite3.connect("/source/pythonsource/resource/test.db", isolation_level=None)
cursor=conn.cursor()
cursor.execute("create table if not exists records(cor_cnt integer, record text, regdate text)")

# inser 작업
import datetime
now=datetime.now()
nowDateTime=now.strftime("%Y-%m-%d %H:%M:%S")
cursor.execute("insert into records(cor_cnt, record, regdate) values(?,?,?)",
               (cor_cnt, during, nowDateTime), 
              )