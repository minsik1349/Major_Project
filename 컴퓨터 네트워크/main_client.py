#!/usr/bin/env python
# coding: utf-8

# In[ ]:

# 순서 => 

# 테스트 데이터 경우 확인

test_case = [
    
    # 정상의 경우 예시 
    {'url': '127.0.0.1/', 'method': 'HEAD', 'body': ''},          # 100 CONTINUTE(최초 연결 후 Head 확인) => HEAD 유효한 경우 
    {'url': '127.0.0.1/', 'method': 'GET', 'body': ''},           # 200 OK => GET 유효한 경우 
             
    ## 오류 예시
    {'url': '127.0.0.1??', 'method': 'GET', 'body': ''},          # 404 ERROR(url 주소가 잘못된 경우 => (PORT/주소))
    {'url': '127.0.0.1/', 'method': 'PRRT', 'body': ''},          # 405 ERROR(유효하지 않는 METHOD 입력 된 경우)
    {'url': '127.0.5.1/', 'method': 'GET', 'body': ''},           # 400 ERROR(허용 되지 않는 HOST인 경우)
    {'url': '127.0.0.1/create', 'method': 'PUT', 'body': ''},     #    EㅈRROR(CREATE나 UPDATE 시 path가 매칭이 안된 경우)
    
    # POST 정상 / 오류 예시
    {'url': '127.0.0.1/create', 'method': 'POST', 'body': 'ID: 20182793&Subject: Computer_Network&Grade: A'}, # 200 OK(데이터 정상 입력)
    {'url': '127.0.0.1/', 'method': 'GET', 'body': ''},                     # 200 OK(DB 저장 내용 확인)
    {'url': '127.0.0.1/create', 'method': 'POST', 'body': ': 95'},          # 400 ERROR(Key 값이 유효하지 않는 경우 에러 발생)
    {'url': '127.0.0.1/create', 'method': 'POST', 'body': 'middle_exam70'}, # 400 ERROR(Key-value 쌍이 유효하지 않는 경우 에러 발생)
    {'url': '127.0.0.1/create', 'method': 'POST', 'body': 'ID: 20180434'},  # 400 ERROR(같은 key 값을 갖은 경우 에러 발생)
    {'url': '127.0.0.1/', 'method': 'HEAD', 'body': ''},                    # 100 CONTINUTE (Head 유효)
    
    # PUT 정상 / 오류 에시
    {'url': '127.0.0.1/update', 'method': 'PUT', 'body': 'ID: 20180434&final_exam: 90'}, # 200 OK(데이터 정상 업데이트 & 추가)
    {'url': '127.0.0.1/update', 'method': 'PUT', 'body': ''},                            # 400 Error(update 내용이 입력되지 않았을 경우)
    {'url': '127.0.0.1/update', 'method': 'PUT', 'body': 'retake_wheaterYes'},           # 400 ERROR(Key-value 쌍이 유효하지 않는 경우 에러 발생)
    {'url': '127.0.0.1/', 'method': 'END', 'body': ''}                                   # 종료조건
]

## 필요한 모듈 정의 
from socket import *
from datetime import datetime

host = '127.0.0.1'
port = 10000
case_num = 0

def request_formate(method, host, path, body=''):
    start_line = "{} / HTTP/1.1".format(method)
    head_line = "Host: {}/{}\r\nContent-Type: text/html\r\nConnection: keep-alive\r\nContent-Length: {}".format(host, path, len(body))
    response = start_line +"\r\n" + head_line + "\r\n\n" + body
    return response

for test in test_case:
    case_num +=1                                                       # 테스트 경우를 시각화 하기 위한 case_num 데이터
    
    print("### Test Case{}: {}".format(case_num, test))
    print("----------------------------------------")
   
    client_socket = socket(AF_INET, SOCK_STREAM)                       # Client socket 생성
    client_socket.connect((host, port))                                # variables에 설정된 주소의 서버로 연결을 요청
        
    method, url, body = test['method'], test['url'], test['body']      # request를 작성(필요한 내용을 test에서 분할)
    
    # request 내용 중 올바른 주소가 아닐 경우(올바른 주소 판단 여부: "(host)/address" 구조) 처리하기 위한 함수
    if '/' in url:
        host_num = url.split('/')[0]
        path_num = url.split('/')[1]
    else:
        host_num = "?"
        path_num = "?"
    print("Sending Request...\n\r")
    
    request = request_formate(method, host_num, path_num, body)         # 각 상황에 맞는 request 생성
    client_socket.send(request.encode('utf-8'))                         # request를 server로 전송
    
    print("Receving Response...\n\r")
    data = client_socket.recv(4096).decode('utf-8')                     # request에 대응하는 server의 response
    
    print("Response data:\n\r", data)
    client_socket.close()                                              # client는 한 번 request와 response를 주고 받고나면 종료(Server는 계속 열림)
    
    print("\n\rFinish...\n\r")