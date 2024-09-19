# Work5. 브라우저에 URL 입력 시 발생하는 과정

## 플로우 차트 및 과정

![img](https://github.com/user-attachments/assets/b73e6e2d-5eb6-47d0-81b7-28dd2c32d26c)

1. **URL 입력 및 해석**
   - 사용자가 브라우저 주소창에 URL을 입력하고 Enter를 누릅니다. 브라우저는 URL의 유효성을 검사합니다.

2. **DNS 조회**
   - 도메인 이름을 IP 주소로 변환하기 위해 DNS 서버에 요청을 보냅니다.

3. **TCP 연결 설정**
   - IP 주소를 얻으면 브라우저는 해당 서버와 TCP 3-way handshake를 통해 연결을 설정합니다.

4. **보안 확인 (HTTPS의 경우)**
   - HTTPS 연결인 경우, TLS handshake를 통해 보안 연결을 설정합니다.

5. **HTTP/HTTPS 요청 전송**
   - 브라우저는 서버에 HTTP 또는 HTTPS 요청을 보냅니다.

6. **서버 응답 수신**
   - 서버는 요청을 처리하고, HTML, CSS, JavaScript 등의 리소스를 포함한 응답을 반환합니다.

7. **HTML 파싱 및 렌더링**
   - 브라우저는 받은 HTML을 파싱하여 DOM(Document Object Model)을 생성하고, CSS와 JavaScript를 적용하여 화면에 렌더링합니다.

8. **추가 리소스 요청**
   - HTML 파싱 중 필요한 이미지, 스타일시트, 스크립트 등의 추가 리소스를 병렬로 요청하고 로드합니다.

## 핵심개념 정리

- **네트워크 7계층**: 네트워크 통신 과정을 7개의 계층으로 나눈 OSI 모델. 각 계층은 특정 네트워크 기능을 담당.
- **HTML 파싱 및 렌더링**: 브라우저가 서버로부터 받은 HTML 문서를 해석하고 화면에 표시하는 과정.
- **HTTP(HTTPS) 프로토콜 요청과 응답**: 클라이언트와 서버 간의 웹 통신 규약. HTTPS는 보안이 강화된 버전.
- **DNS (Domain Name System)**: 도메인 이름을 IP 주소로 변환하는 시스템.
- **TCP (Transmission Control Protocol)**: 신뢰성 있는 데이터 전송을 보장하는 연결 지향적 프로토콜.
- **UDP (User Datagram Protocol)**: 비연결형 프로토콜로, 빠른 전송이 필요한 경우 사용.
- **DHCP (Dynamic Host Configuration Protocol)**: 네트워크 장치에 자동으로 IP 주소를 할당하는 프로토콜.
- **IP 주소 발급방법**: DHCP를 통한 자동 할당 또는 수동 설정으로 IP 주소 부여.
- **공인/사설 IP주소**: 공인 IP는 인터넷에서 직접 접근 가능한 주소, 사설 IP는 내부 네트워크에서만 사용되는 주소.
- **MAC 주소 (Media Access Control)**: 네트워크 인터페이스 카드의 고유 식별자.
- **ARP (Address Resolution Protocol)**: IP 주소를 MAC 주소로 변환하는 프로토콜.
- **ISP (Internet Service Provider)**: 개인이나 기업에게 인터넷 접속 서비스를 제공하는 회사.
