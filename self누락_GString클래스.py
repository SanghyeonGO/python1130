#전역변수
str = "Not Class Member"

class GString:
    #초기화 매서드
    def __init__(self):
        #인스턴스 맴버변수 초기화
        self.str = "" 
    #인스턴스 매서드
    def set(self, msg):
        self.str = msg
    def print(self):
        #버그~~
        print(self.str)

#인스턴스(복사본)생성
g = GString()
g.set("First Message")
g.print()
