# csv 읽기
import csv # python에서 제공하는 csv 모듈

# with open("resource/sample1.csv", "r") as f:
#     content=csv.reader(f)
#     print(content)
#     print(dir(content))
#     print(type(content))

#     next(content) # 헤더명 제거
#     for c in content:
#         print(c)

# '' 안에 분리되지 않고 하나로 일렬로 다 들어왔다. => delimiter="|"를 쓰면 해결된다.
# with open("resource/sample2.csv", "r") as f:
#     content=csv.reader(f, delimiter="|")

#     next(content) # 헤더명 제거
#     for c in content:
#         print(c)

# with open("resource/sample2.csv", "r") as f:
#     content=csv.DictReader(f, delimiter="|") # dict 구조로 출력됨

#     next(content) # 헤더명 제거
#     for c in content:
#         print(c)
#         for k, v in c.items():
#             print(k, ":", v)
#         print()

# sample3.csv 읽기
# with open("resource/sample2=3.csv", "r") as f:
#     content=csv.reader(f)

#     for row in content:
#         for i in row:
#             print(i, end=" ")
#         print()

# csv 쓰기, newline의 역할은 엔터가 되어 출력되는 데이터를 방지
# data=[[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15]]

# with open("resource/sample4.csv", "w", newline="") as f:
#     wt=csv.writer(f)

#     for v in data:
#         wt.writerow(v)

data=[[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15]]

with open("resource/sample5.csv", "w", newline="") as f:
    wt=csv.writer(f)

    wt.writerows(data)

