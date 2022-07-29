#!/usr/bin/env python
# coding: utf-8

# In[ ]:

# 필요한 모듈 불러오기 
import time
from socket import *

# 필요한 변수들 정리 
IP, port = '127.0.0.1', 10000
status_pair = {100:'CONTINUE', 200:'OK', 400:'BAD_REQUEST', 404:'NOT_FOUND', 405:'METHOD_NOT_ALLOWED'}
db_data = {}
    
# Client에서 온 Request을 처리하는 함수 정의(완료)
def change_response(method, url, body):
    
    # 0. 읽어드린 url이 잘못된 경우 에러 발생
    if '?/?' not in url:
        host = url.split('/')[0]
        path = url.split('/')[1]
    else:
        body = "Invalid Address(url)"
        response = response_format(404, "?", "?", body)
        return response
    
    # 1. 요청한 Request에 4가지 해당하지 않을 경우 에러 발생
    if method not in ['HEAD','GET','POST', 'PUT']:
        body = "Method not allowed"
        response = response_format(405, host, path, body = body)
    
    # 2. 허용하지 않는 host일 경우 에러 발생
    elif host != IP:
        body = "Not allowed host: {}".format(host)
        response = response_format(400, host, path, body = body)
    
    # 3. method별 데이터 읽기 
    else:
        # PATH 내의 create이면 method가 post이면 값을 반환
        if path == "create":
            if method == "POST":
                response = post(host, path, body)
        # PATH 내의 create이지만 method가 대응되는 POST가 아닐 경우는 경고 메시지 반환(에러)        
            else:
                body = "Select the appropriate method(Create mode => POST)"
                response = response_format(404, host, path, body = body)
        
        # PATH 내의 update이면 method가 put이면 값을 반환
        elif path == "update":
            if method == "PUT":
                response = put(host, path, body)
        # PATH 내의 create이지만 method가 대응되는 put 아닐 경우는 경고 메시지 반환(에러)      
            else:
                body = "Select the appropriate method(Updata mode => PUT)"
                response = response_format(404, host, path, body = body)
        
        # HEAD를 읽을 떄 
        elif method == "HEAD":
            response = head(host, path, body)
        
        # GET을 읽을 때
        elif method == "GET":
            response = get(host, path, body)
                
    return response
    
# response 작성
def response_format(code, host, path, body=''):
    data = time.strftime("%a, %d %b %Y %H:%M:%S KST", time.localtime())
    
    start_line = "HTTP/1.1 {} {}".format(code, status_pair[code])
    head_line = "Host: {}/{}\r\nContent-Type: text/html\r\nConnection: keep-alive\r\nContent-Length: {}\r\nDate: {}".format(host, path, len(body), data)
    response = start_line +"\r\n" + head_line + "\r\n\n" + body
    return response
        
# Method 정의
## 1. head 응답 함수: response에 header부분만 표시
def head(host, path, body):
    response = response_format(100, host, path, body = '')
    return response 

## 2. Get 응답 함수: Response에 header + body 부분 표시
def get(host, path, body):    
    # db 내에 정보가 있을 경우 그 정보를 반환
    if db_data: 
        body = "The data in DB is as follows. \n\r"
        for key, value in db_data.items():
            body += key + ':' + value + '\r\n'
        body = body[:-2]
    # db 내에 정보가 없을 경우 정보가 없다는 문구 반환
    else:
        body = "No data in DB"
    response = response_format(200, host, path, body)
    return response 

    
## 3. post 응답 함수
def post(host, path, body):
    content, total = '', ''
    # 추가 해야할 내용이 아무것도 없을 때(body == 0), 오류 발생 변환
    if len(body) == 0 or body in ['', ' ']:
        response = response_format(400, host, path, body)
        return response
    
    # 추가 해야할 내용이 있다면, 인식 확인하였다는 점을 200으로 반환 / 추가 데이터 반환
    else: 
        body_values = body.split('&')
        # 여러 개의 값들을 입력 하게 되면
        for body_value in body_values:
            
            # key: value 형식을 맞추지 않는 다면(key-value를 구분하는 : 없다면) 잘못된 요청으로 판단해 400 에러 발생
            if ":" not in body_value:
                body = "Key-value format is not valid."
                response = response_format(400, host, path, body)
                return response
                
            key, value = body_value.split(':')
            key = key.strip()
            value = value.strip()
            
            # key 값이 비워있거나 공백일 경우 400 에러 발생
            if key in [None, '', ' ']:
                body = "Key value does not exist or is blank."
                response = response_format(400, host, path, body)
                return response
            
            # key 값이 없는 경우 db에 내용 추가
            elif db_data.get(key) == None:
                db_data.setdefault(key, value)
                content = key + ':' + value + '\r\n'
                total += content
                
            # 같은 key 값을 저장한 있는 경우 400 에러 발생    
            else:
                body = "The key already exists!"
                response = response_format(400, host, path, body)
                return response
            
        # 값이 정상적으로 정상적으로 저장되었을 경우 200, OK 반환
        body = "Post Suceessfully OK" 
        total += body
        
        response = response_format(200, host, path, total)
    return response
        

## 4. Put 응답 함수:
def put(host, path, body):
    old_dic, change_dic, new_dic = {}, {}, {}
    main_key, content = '', ''
    
    # update 해야 할 내용을 입력하지 않는다면(body = ''), 인식하지 못했다고 반환(오류) 400
    if len(body) == 0 or body in ['',' ']:
        body = "There is no content. Please check"
        response = response_format(400, host, path, body)
        return response
    
    # update 해야 할 내용을 입력했으면, 인식한 결과 반환(200) / error 제외
    else:
        body_values = body.split('&')
        for body_value in body_values:
            
            # key: value 형식을 맞추지 않는 다면(key-value를 구분하는 : 없다면) 잘못된 요청으로 판단해 400 에러 발생
            if ":" not in body_value:
                body = "Key-value format is not valid."
                response = response_format(400, host, path, body)
                return response
            
            key, value = body_value.split(':')
            key = key.strip()
            value = value.strip()
            
            # key 값이 db에 있다면 updage 진행
            if key in db_data:
                previous_data = db_data[key]
                db_data[key] = value
                old_dic.setdefault(key, previous_data)
                change_dic.setdefault(previous_data, value)    
                
            # key 값이 db에 없다면 create 진행
            else: 
                db_data.setdefault(key, value)
                new_dic.setdefault(previous_data, value)
        
        # updata를 진행할 경우(key 값이 존재하고, 해당 값을 updata) 하는 것에 대한 정보 전달 코드
        if len(change_dic):
            body += "\n\n\rUpdate Data as follow:\n\r"
            
            for key, pre in old_dic.items():
                change_data = change_dic[pre] 
                body += key + ": " + pre + " => " + change_data + "\n\r"
                
        # create_upbdata를 진행할 경우(key 값이 존재하지 않아 새롭게 만드는 것에 대한) 하는 것에 대한 정보 전달 코드        
        if len(new_dic) !=0:
            body += "\n\rUpdate(New) Data as follow:\n\r"
            
            for key, new in new_dic.items():
                body += key + ": " + new + "(There's no key. New update)"
        
        body += "\n\rUpdate with new data Sucessfully OK \n\r"
        body = body[:-2]
        response = response_format(200, host, path, body)
        return response

# 서버 생성: IP와 port 활용해 TCP 서버
server_socket = socket(AF_INET, SOCK_STREAM) 
server_socket.bind((IP,port))
server_socket.listen(5)

# 서버를 연 이후 계속 유지(종료 조건이 오기 전까지)
while True:
    print("----------The Server is ready to receive (Host: {}, Port: {})----------".format(IP,port))
     
    client_socket, client_addr = server_socket.accept()   # Client connectino을 기다린 후 accept 진행
    request = client_socket.recv(4096).decode('utf-8')    # Client Request을 수신
    
    print("request:\n\r", request)                         # Request 수신 시각화
    
    ## Request에서  Response 으로 변환횔 때의 필요한 내용 정리
    ## (method => 수행해야할 작업 / body => 내용 정보 url => host 및 adress 정보)
    request_part = request.split('\n')                     
    url = request_part[1].split(':')[1][1:-1]  
 
    method = request_part[0].split()[0]
    body = request_part[-1]
    
    # 종료조건(들어온 reqest 중 End가 발생할 경우 socekt 종료 진행)
    if method == "END":
        print("Complete all courses. socket finish")
        break
        
    response = change_response(method, url, body)         # reponse 생성 후 그 결과를 client 보냄
    client_socket.sendall(response.encode('utf-8'))
    print("send the response...\n\r")
    
# 종료 후 socket을 닫음    
client_socket.close()
server_socket.close()  