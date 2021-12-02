# DemoFile.py
import sys

print("hello", "python", sep="~", end="!", file=sys.stderr)

#파일을 다루는 객체를 생성
f = open("c:\\work\\demo.txt","wt")
print("파일에 쓰는 작업", file=f)
f.close()

#문자열을 결합하는 경우
url = "http:\\www.naver.com/?page=" + str(1)
print(url)
