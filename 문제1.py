#클래스의 작동 구현
# Car
## 클래스 선언 부분 ##
class Car:
    color = ""
    speed = 0
    
    def upSpeed(self, value):
        self.speed += value
        if self.speed > 150:
            self.speed = 150
        
    def downSpeed(self, value):
        self.speed -= value
        
    def printMessage():  # printMessage() 안에서는 필드를 사용하지 않으므로 이때는 self 생략 가능
        print("시험 출력이다.")

## 메인 코드부분 ##
myCar1 = Car()
myCar1.color = "빨강"
myCar1.speed = 0

myCar2 = Car()
myCar2.color = "파랑"
myCar2.speed = 0

myCar3 = Car()
myCar3.color = "노랑"
myCar3.speed = 0

## 메서드 호출 ##
myCar1.upSpeed(30)
print("자동차1의 색상은 %s이며, 현재 속도는 %dkm입니다." % (myCar1.color, myCar1.speed))
myCar2.upSpeed(60)
print("자동차2의 색상은 %s이며, 현재 속도는 %dkm입니다." % (myCar2.color, myCar2.speed))
myCar3.upSpeed(200)
print("자동차3의 색상은 %s이며, 현재 속도는 %dkm입니다." % (myCar3.color, myCar3.speed))


