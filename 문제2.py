class Car:
    speed = 0
    def upSpeed(self, value):
        self.speed += value
        
        print("현재 속도(슈퍼클래스) : %d" % self.speed)

class Sedan(Car):  
    def upSpeed(self, value):
        self.speed += value
        
        if self.speed > 150:
            self.speed = 150
        print("현재 속도(서브클래스) : %d" % self.speed)

class Sonata(Sedan):
    pass

class Ttuck(Car):  
    pass

##변수 선언 부분##
sedan1, truck1, sonata1 = None, None, None

##메인 코드 부분##
truck1 = Ttuck()
sedan1 = Sedan()
sonata1 = Sonata()

print("트럭 --> ", end = "")
truck1.upSpeed(200)
print("승용차 --> ", end = "")
sonata1.upSpeed(150)
print("소나타 --> ", end = "")
sonata1.upSpeed(150)
