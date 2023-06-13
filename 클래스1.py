#클래스는 왜 필요한가?
#반복되는 변수나 메서드(함수)를 미리 정해 놓은 틀(설계도)
result = 0

def add(num):
    global result # > 이전에 계산된 결과값 유지를 위해 전역변수 사용
    result += num
    return result
#Add 함수는 입력 인수로 num을 받으면 이전에 계산된 결과값에 더한 후 출력하는 함수이다
print(add(3))
print(add(4))

#(한프로그램에서 두개의 계산기가 필요하다?) - 함수를 각각 따로
result1 = 0
result2 = 0

def add1(num):
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result2 += num
    return result2

print(add1(3)) # ->계산기의 결과값이 계산기 2에 아무런 영향을 끼치지x
print(add1(4)) # ->계산기가 3개, 5개, 10개.... 필요하다면? 전역변수와 함수를 추가??
print(add2(3))
print(add2(7))

#반복되는 변수나 메서드(함수)를 미리 정해 놓은 틀
# 반복되는 변수 : result
# 메서드(함수) : add
# 클래스 안레서 구현된 함수는 함수라고 하지 않고 메서드라고 함.

# 클래스를 쓰는 방법
# 1. class입력하고
# 2. 대문자로 시작하는 클래스의 이름을 작성
# 3.안에 들어갈 함수와 변수 설정 
# 클래스를 이용한 계산기
class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result
    
cal1 = Calculator() # -> 클래스를 이용하면 계산기의 개수가 늘어나더라도 인스턴스를 생성하기만 하면 된다 클래스의 장점 
cal2 = Calculator() 

print(cal1.add(3)) 
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))
print(cal2.sub(2))

# 클래스(class) : 똑같은 무엇인가를 계속해서 만들어 낼 수 있는 설계도면
# 객체(Object) : 클래스로 만든 피조물
# 아무기능도 없는 껍질뿐인 클래스도 객체 생성이 가능

#생성자
# 생성자의 개념 : 인스턴스를 생성하면서 필드값을 초기화시키는 함수
# 생성자의 기본 형태 : __init__()라는 이름
# __init__()는 앞뒤에 언더바(_)가 2개씩, init는 lnitialize의 약자로 초기화 의미

#class 클래스명 :
#    def __init__(self):
        # 이부분에 초기화 할 코드 입렵