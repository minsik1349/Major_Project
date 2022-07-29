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
  - Head 부분(Body 부분을 제외한 부분) 반환, 100 CONTINUTE 
  
  라. GET Method 정의
  -
  
  마. POST Method 정의
  
  바. PUT Method 정의

   #### Case 정리
   
   
   
### 4. 내 역할
- Server & Client 파일 구성(py)
- 2대의 노트북으로 통신하는 방법 진행(AWS로 시도했지만 실패)
- Read.me file 정리

### 5. Review  
- 컴퓨터 네트워크 관련 개녀만을 이해하는 것도 어려웠지만, 이를 실제로 구현하는 게 처음에는 어려웠지만 개념을 다시 이해하면서 구현하니 쉽게 진행되었음
- AWS 과정을 시도했지만 실패한 것은 너무 아쉬었고, 차후 프로젝트 과정에서 한번 더 도전을 해보고 싶은 생각

### 6. [추가 과제](https://github.com/minsik1349/Major_Project/blob/main/%EC%BB%B4%ED%93%A8%ED%84%B0%20%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC/WireShark%20%ED%86%B5%EC%8B%A0%EB%B6%84%EC%84%9D.pdf)
-
