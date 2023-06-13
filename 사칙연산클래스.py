#사칙연산 클래스
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    
    def add(self):
        result = self.first + self.second
        return result
    
a = FourCal()
a.setdata(4, 2) # a는 setdata, add를 가지고 있다.
print(a.add())
print(a.first)
print(a.second)

#더하기 곱하기 빼기 나누기
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self): #더하기 add
        result = self.first + self.second
        return result
    def mul(self): #곱하기 mul
        result = self.first * self.second
        return result
    def sub(self): #빼기 sub
        result = self.first - self.second
        return result
    def div(self): #나누기 div
        result = self.first / self.second
        return result
    
a = FourCal()
b = FourCal()
a.setdata(4, 2)
b.setdata(3, 8)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
print(b.add())
print(b.mul())
print(b.sub())
print(b.div())

#생성자
class FourCal:
    def __init__(self, first, second): # < __init__ 생성자
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self): #더하기 add
        result = self.first + self.second
        return result
    def mul(self): #곱하기 mul
        result = self.first * self.second
        return result
    def sub(self): #빼기 sub
        result = self.first - self.second
        return result
    def div(self): #나누기 div
        result = self.first / self.second
        return result

#클래스의 상속(Inheritance - '물려받다')
class MoreFourCal(FourCal): #FourCal 클래스를 상속하는 MoreFourCal 클래스
    pass

#a의 b의 제곱을 계산하는 MoreFourCal 클래스
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(4, 2)
print(a.add()) 
print(a.pow()) 
    
a = FourCal(4, 2)
print(a.first)
print(a.second)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())

#매서드 오버라이딩
#상속받을 대상인 클래스의 메서드와 이름은 같지만 그 행동을 다르게 해야 할 때
#메서드 이름을 동일하게 다시 구현하는 것을 메서드 오버라이딩
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0: # 나누는 값이 0인 경우 0을 리턴하도록 수정
            return 0
        else:
            return self.first / self.second

a = SafeFourCal(4, 0)
print(a.div())

