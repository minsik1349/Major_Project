## 컴퓨터 네트워크

### [Readme 파일](https://github.com/minsik1349/Major_Project/blob/main/%EC%BB%B4%ED%93%A8%ED%84%B0%20%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC/TCP%20Socket%20%ED%86%B5%EC%8B%A0.pdf)

### 1. 프로젝트 개요
- 목적: 이론 수업 간 배웠던 컴퓨터 네트워크 TCP 통신을 실제로 구현
- 환경: Python(언어), Socket 통신(Local 진행)
- 개요: TCP 기반 소켓프로그래밍 작성후 Client에서는 HTTP 프로토콜의 GET/HEAD/POST/PUT Request를 요청하고 Server에서는 Client의 Request에따라 응답 메시지를 구성하여 Response하도록 구현(TCP 기반 Client, Server 구현한 프로그램 파일을 제출)
   -  case 5개 이상 수행진행
   -  소스파일과 Readme 파일(ppt, doc 등)을 작성하여 제출
   -  Readme 파일은 소스 파일, 동작 환경, HTTP 명령어 결과에 대한 설명을 포함
   -  HTTP 명령어 수행시 Client, Server에서 출력하는 내용을 화면 캡쳐하여 작성
    
### 2. 활동 내용 
- 국민대학교 컴퓨터 네트워크/타전공(2022 1학기) 
- 팀 프로젝트로 진행 

### 3. 프로젝트 과정(세부사항)
  - 목표: TCP Socket 통신을 Error 없이 진행
  
  #### Server 
  - Client connection을 기다린 이후 Accept 진행
  - Client Request을 수신 후, 필요한 정보를 정리
  - 종료 조건이 들어올경우(Reguset Method 중 "End"일 경우) Socket 통신 종료
  - 그 이외의 경우는 맞는 Response 생성 후 결과를 Client 보냄

  가. Reponse
  - HTTP 생성함수를 3단계(Start, header, reponse)로 나눠서 정의한 후 Response 진행
  - HTTP 1.1 Version 구조로 정의

  나. Request
  -  읽어드린 URL이 잘못된 경우(?/?의 경우): 404 ERROR(Invalid Address(url))
  -  요청한 Request가 4가지(HEAD, GET, POST, PUT) 해당되지 않는 경우: 405 ERROR(Mehthod not aloowed)
  -  허용되지 않는 IP인 경우(Local: 127.0.0.1): 400 ERROR(Not allowd host)
  -  path와 Method 불일칠 할경우: 404 ERROR(Select the appropriate method)  
  => [1] path가 create일 때 POST 이외 Method 들어온 경우 [2] path가 update일 때 PUT 이외의 Method 들어온 경우 
  -  각 Method별 데이터 읽기 진행

  다. Head Method 정의
  - Head 부분 반환(Body 부분을 제외한 부분), 100 CONTINUTE  
  
  라. GET Method 정의
  - Get 부분 반환, 200 OK
  - DB 내 정보가 있을 경우, 정보를 반환(Key-value 형식) / 없을 경우, "No data in DB" 문구와 함께 반환
  
  마. POST Method 정의
  - DB 내의 정보를 저장하기 위한 내용
  - Body 형식: Key1:value1&key2:value2 => key와 value 간의 대응관계를 ":"로 구분, 데이터요소는 "&"로 구분
  - 추가해야할 내용이 아무것도 없을 경우(Body가 비어있거나, 길이가 0인 경우): 400 ERROR
  - Key:value 형식이 맞지 않는다면(key-value 구분자 ":"가 없을 경우): 400 ERROR(Key-value formatis not valid)
  - Key 값이 비어있거나 공백일 경우: 400 ERROR(Key'value does not exist or is blank)
  - Key 값이 없는 경우에 DB에 key와 value를 저장
  - Key 값이 중복된 경우: 400 ERROR(The key already exists!)
  - 정상적으로 저장되었을 경우: 200 OK 
  
  바. PUT Method 정의
  - DB 내의 정보를 갱신하기 위한 내용
  - Body 형식은 POST와 동일 
  - 갱신해야할 내용이 아무것도 없을 경우(Body가 비어있거나, 길이가 0인 경우): 400 ERROR
  - Key:value 형식이 맞지 않는다면(key-value 구분자 ":"가 없을 경우): 400 ERROR(Key-value formatis not valid)
  - Key 값이 비어있거나 공백일 경우: DB에 Updata를 진행
  - Key 값이 없는 경우에 DB에 Create를 진행
  - 정상적으로 저장되었을 경우: 200 OK 
  
  #### Client
  - Client Socket을 생성 후, 변수로 설정된 주소의 서버로 연결 요청
  - Request 작성(test case에서 필요한 부분을 분할 넣음)
  - Request 내용 중 올바른 주소 형태(host/address)아닐 경우: "?/?"형태로 변경(ERROR 감지 위함)
  - Request에 대응되는 server의 response 제공
  - Client는(서버와 달리) 한 번의 Request-Responsed 주고받으면 종료
  
  가. Case 정리(총 17개의 Case 진행 / 앞선 Method의 예외 처리 경우 Case 존재)

  나. Request 
  - Response와 마찬가지로 HTTP 생성함수를 3단계(Start, header, reponse)로 나눠서 정의한 후 Requet 진행
   
### 4. 내 역할
- Server & Client 파일 구성(py)
- 2대의 노트북으로 통신하는 방법 진행(AWS로 시도했지만 실패)
- Read.me file 정리

### 5. Review  
- 컴퓨터 네트워크 관련 개녀만을 이해하는 것도 어려웠지만, 이를 실제로 구현하는 게 처음에는 어려웠지만 개념을 다시 이해하면서 구현하니 쉽게 진행되었음
- AWS 과정을 시도했지만 실패한 것은 너무 아쉬었고, 차후 프로젝트 과정에서 한번 더 도전을 해보고 싶은 생각

### 6. [추가 과제](https://github.com/minsik1349/Major_Project/blob/main/%EC%BB%B4%ED%93%A8%ED%84%B0%20%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC/WireShark%20%ED%86%B5%EC%8B%A0%EB%B6%84%EC%84%9D.pdf)
- 와이어샤크로 DNS, TCP 인 경우에 메시지를 캡쳐하여 분하는 과제
- [1] DNS 분석의 경우: 구글 => 공공데이터포탈 접속 과정에 대한 DNS query and response 
- [2] TCP 분석의 경우: 앞선 TCP scoket 통신 Local에서 진행한 결과로 분석 진행(TCP Segment의 format을 분석)
