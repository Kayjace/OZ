# Flask 쇼핑몰 API

이 프로젝트는 Flask를 사용하여 구축된 쇼핑 플랫폼을 위한 RESTful API입니다. 사용자, 제품, 주문, 장바구니 관리를 위한 기능을 제공합니다.

## 기능

- **사용자 관리**: 
  - 사용자 등록 및 인증.
  - 관리자는 사용자 정보를 조회하고 수정할 수 있습니다.

- **제품 관리**:
  - 제품 생성, 조회, 수정, 삭제 기능.
  - 관리자가 제품을 관리할 수 있습니다.

- **주문 관리**:
  - 사용자가 주문을 생성할 수 있습니다.
  - 주문 세부 정보를 조회할 수 있습니다.

- **장바구니 관리**:
  - 사용자가 장바구니에 아이템을 추가할 수 있습니다.
  - 장바구니 아이템을 조회하고 관리할 수 있습니다.

## 데이터베이스 스키마

데이터베이스 스키마는 다음과 같은 테이블을 포함합니다:

- **Users**: 사용자 정보 저장 (이름, 이메일, 비밀번호, 관리자 상태 등).
- **Orders**: 주문 세부 정보 (사용자 ID, 아이템, 총액, 상태 등).
- **Products**: 제품 정보 (제목, 설명, 가격, 상태 등).
- **Cart**: 각 사용자의 장바구니 아이템 관리.

## 프로젝트 구조
```
flask_shopping_api/
│
├── app/
│ ├── init.py # 애플리케이션 설정 및 구성
│ ├── models.py # 데이터베이스 모델
│ ├── routes.py # API 라우트
│ ├── auth.py # 인증 로직
│ └── utils.py # 유틸리티 함수
│
├── config.py # 설정 파일
├── run.py # 애플리케이션 진입점
├── requirements.txt # Python 의존성 목록
└── .env # 환경 변수
```

## 설치 방법

1. **저장소 클론** :
   ```bash
   git clone https://github.com/Kayjace/OZ.git
   cd OZ/Flask/flask_shopping_api
2. **가상환경 생성** :
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows에서는 'venv\Scripts\activate'
   ```
3. **의존성 설치** :
   ```bash
   pip install -r requirements.txt
   ```
4. **데이터베이스 설정** :
  - MySQL이 실행 중인지 확인하고 데이터베이스를 생성합니다.
  - '.env' 파일에 데이터베이스 자격 증명을 업데이트합니다.

## 사용 방법
API는 http://localhost:5000에서 접근 가능합니다.
Postman 등의 도구를 사용하여 API 엔드포인트와 상호작용할 수 있습니다.

## 보안
.env 파일이 공개되지 않도록 주의하세요.
환경 변수를 사용하여 민감한 정보를 관리하세요.
