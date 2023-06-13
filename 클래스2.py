#클래스의 작동 구현
## 클래스 선언 부분 ##
class Car:
    color = ""
    speed = 0
    
    def upSpeed(self, value):
        self.speed += value
        
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
myCar3.upSpeed(0)
print("자동차3의 색상은 %s이며, 현재 속도는 %dkm입니다." % (myCar3.color, myCar3.speed))


## 클래스 선언 부분 ##
class Car:
    color = ""
    speed = 0
    
    def __init__(self):
        self.color = "빨강"
        self.speed = 0
    
    def upSpeed(self, value):
        self.speed += value
        
    def downSpeed(self, value):
        self.speed -= value
        

## 메인 코드부분 ##
myCar1 = Car()
myCar2 = Car()

## 메서드 호출 ##
print("자동차1의 색상은 %s이며, 현재 속도는 %dkm입니다." % (myCar1.color, myCar1.speed))
print("자동차2의 색상은 %s이며, 현재 속도는 %dkm입니다." % (myCar2.color, myCar2.speed))


#매개변수가 있는 생성자
## 클래스 선언 부분 ## 
class Car:
    color = ""
    speed = 0
    
    def __init__(self, value1, value2):
        self.color = value1
        self.speed = value2
        
## 메인 코드부분 ##
myCar1 = Car("빨강", 30)
myCar2 = Car("파랑", 60)

## 메서드 호출 ##
print("자동차1의 색상은 %s이며, 현재 속도는 %dkm입니다." % (myCar1.color, myCar1.speed))
print("자동차2의 색상은 %s이며, 현재 속도는 %dkm입니다." % (myCar2.color, myCar2.speed))

#상속을 구현하는 문법
#class 승용차(자동차) 
#    메서드 - 


#메서드 오버라이딩 (상위 클래스의 메서드를 서브 클래스에서 재정의)
class Car:
    speed = 0
    def upSpeed(self, value):
        self.speed += value
        
        print("현재 속도(슈퍼클래스) : %d" % self.speed)

class Sedan(Car):  #메서드 오버라이딩
    def upSpeed(self, value):
        self.speed += value
        
        if self.speed > 150:
            self.speed = 150
        print("현재 속도(서브클래스) : %d" % self.speed)

class Ttuck(Car):  #메서드 오버라이딩
    pass

##변수 선언 부분##
sedan1, truck1 = None, None

##메인 코드 부분##
truck1 = Ttuck()
sedan1 = Sedan()
print("트럭 --> ", end = "")
truck1.upSpeed(200)
print("승용차 --> ", end = "")
sedan1.upSpeed(200)
