class UserInfo:
#     """
#     Author: Hong
#     Date: 2023.06.21
#     Description: 클래스 작성법: 인자 있는 생성자(오버로딩 유사)
#     """

    def __init__(self,name,age,email=None) -> None:
        self.name=name
        self.age=age
        self.email=email

    def user_info(self):
        return "name: {}, age: {}, email: {}".format(self.name, self.age, self.email)
    
# 두 명의 객체 생성
user1=UserInfo("홍길동", 34, "hong@naver.com")
user2=UserInfo("고길동", 44)

# user_info(메서드) 호출
print(user1.user_info())
print(user2.user_info())

# 클래스 변수 확인
print("생성된 user {} 명".format(UserInfo.user_count))
print("생성된 user {} 명".format(user1.user_count))

# user 삭제
del user1 # __del__ 메서드 자동으로 호출되어 실행
print("생성된 user {} 명".format(UserInfo.user_count))

# function1(), function2() 호출
# user1.function1() # TypeError: UserInfo.function1() takes 0 positional arguments but 1 was given
UserInfo.function1() 
user2.function2()

