# 주차장 프로그램

# 주차장 리스트 생성
parking_lot=[]

# 주차위치, 자동차명 변수 생성
top, car_name=0, "A"

out_car=0

# 메뉴 제공
# [1] 자동차 넣기 | [2] 자동차 빼기 | [3] 종료 :
while True:
    menu=int(input("[1] 자동차 넣기 | [2] 자동차 빼기 | [3] 종료 :"))

    if menu <= 3:
        if menu==1:
            if top >= 5:
                print("주차장 꽉 찼음")
            else:
                parking_lot.append(car_name)
                print("{} 자동차 들어감. 주차장 상태 ==> {}".format(car_name, parking_lot))

                top+=1
                car_name=chr(ord(car_name)+1)
        elif menu==2:
            if top == 0:
                print("빠져나갈 자동차가 없음")
            else:
                out_car=parking_lot.pop()
                print("{} 자동차 나감. 주차장 상태 ==> {}".format(car_name, parking_lot))

                top-=1
                car_name=chr(ord(car_name)-1)               
        else:
            print("프로그램 종료")
            break
    else:
        print("번호를 확인해주세요.")

# print(ord("A"))
# print(chr(65))
