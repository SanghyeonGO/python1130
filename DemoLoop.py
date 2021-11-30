#DemoLoop.py
from typing import ItemsView


value = 5
while value >0:
    print(value)
    value -= 1

    print("---for in루프---")
    lst = [100,"apple",3.14]
for item in lst:
    print(item,type(item))

#딕셔너리로 값을 초기화
d = {"apple":100, "kiwi":200}
for item in d.item():
    print(item())

print("---키만 출력---")
for k in d.keys():
    print(k)

print("---값만 출력---")
#디버깅 모드로 실행할 때 만나면 멈추는 중단점(Break Point)
for v in d.values():
    print(v)
