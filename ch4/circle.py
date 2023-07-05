import math

class Circle:
    def __init__(self,radius) -> None:
        self.__radius=radius

    def getCircum(self):
        return 2*math.pi*self.__radius
    
    def getArea(self):
        return math.pi*(self.__radius**2)
    
    def getRadius(self):
        return self.__radius
    
    def setRadius(self,radius):
        self.__radius=radius
    
circle=Circle()
# print(circle.__radius) # AttributeError: 'Circle' object has no attribute '__radius'
# __radius 접근: getter, setter 사용
print("반지름 : {}".format(circle.getRadius()))
print("원의 둘레 : {}".format(circle.getCircum()))
print("원의 면적 : {}".format(circle.getArea()))

circle.setRadius(20)
print("반지름 : {}".format(circle.getRadius()))
print("원의 둘레 : {}".format(circle.getCircum()))
print("원의 면적 : {}".format(circle.getArea()))