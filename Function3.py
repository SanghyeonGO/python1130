# Function3.py
#함수의 기본값이 있는 경우
def times(a=10, b=20):
    return a*b

#호출
print( times())
print( times(5))
print( times(5,6))

#키워드, 인자
def userURI(server, port):
    strURI = "http://" + server + ":" + port
    return strURI

#호출
print( userURI("credu.com", "80"))
print( userURI(port="8080", server="credu.com"))

#가변인자는 입력되는 인자의 갯수가 가볍적인 경우
def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

#호출(중단점, Break Point)
print( union("HAM", "EGG"))
print( union("HAM", "EGG", "SPAM"))

#정의되지 않은 인자 처리
def userURIBuilder(server, port, **user):
    strURI = "http://" + server + ":" + port + "/?"
    for key in user.keys():
        strURI += key + "=" + user[key] + "&"
    return strURI

#호출
print( userURIBuilder("naver.com", "80", id="kim", password="1234"))
print( userURIBuilder("naver.com", "80", id="kim", password="1234", name="mike", age="30"))
