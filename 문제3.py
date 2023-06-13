# 1. Encore라는 클래스를 만들어 보세요.(hello 메소드)
# lee = Encore(25, "이새싹")
# lee.hello()
# kim = Encore(22, "김새싹")
# kim.hello()
# ---------   결  과  -------------
# 25살 이새싹입니다.
# 22살 김새싹입니다.

## 클래스 선언 부분 ##
class Encore:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def hello(self):
        print(f"{self.age}살 {self.name}입니다")
lee = Encore(25, "이새싹")
lee.hello()
kim = Encore(25, "김새싹")
kim.hello()

# 2. Student클래스가 Encore를 상속받게 해 보세요.
# lee = Student(25, "이새싹", 990011)
# lee.hello()
# lee.encore_study()
# lee.today()
# ---------   결  과  -------------
# 25살 이새싹입니다
# 학번 : 990011
# 하루라도 문제를 풀지 않으면 손에 가시가 돋친다.
# 비가 많이 내립니다.

class Encore:
    def __init__(self, age, name, ID):
        self.age = age
        self.name = name
        self.ID = ID
    def hello(self):
        print(f"{self.age}살 {self.name}입니다")
class Student(Encore):
    def encore_study(self):
        print(f"학번 : {self.ID}")
    def today(self):
        print("하루라도 문제를 풀지 않으면 손에 가시가 돋친다.\n비가 많이 내립니다")
lee = Student(25, "이새싹", 990011)
lee.hello()
lee.encore_study()
lee.today() 