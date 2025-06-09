# Gmail 전송 프로그램

Gmail을 통해 이메일을 전송할 수 있는 GUI 프로그램입니다. 이메일 작성, 첨부 파일 관리, HTML 형식 지원 등 다양한 기능을 제공합니다.

## 주요 기능

- 이메일 작성 및 전송
- 다중 수신자 지원
- HTML 형식 이메일 지원
- 첨부 파일 관리
- Gmail 계정 설정 관리
- 사용자 친화적인 GUI 인터페이스

## 사전 요구사항

- Python 3.8 이상
- Gmail 계정 (2단계 인증 활성화 필요)
- Gmail 앱 비밀번호

## 설치 방법

### 1. 저장소 클론

```bash
git clone https://github.com/dev-jsLee/gmail_sender
cd gmail_sender
```

### 2. 가상환경 설정 및 패키지 설치

#### pip를 사용하는 경우:

```bash
# 가상환경 생성
python -m venv .venv

# 가상환경 활성화
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate

# 패키지 설치
pip install -r requirements.txt

# 개발용 패키지 설치 시 아래 코드 추가 실행
pip install -e ".[dev]"
```

#### uv를 사용하는 경우:

```bash
# uv 설치 (아직 설치하지 않은 경우)
pip install uv

# 가상환경 생성 및 패키지 설치
uv venv
uv pip install -r requirements.txt
# 개발용 패키지 설치 시 아래 코드 추가 실행
uv pip install -e ".[dev]"

# 가상환경 활성화
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
```

### 3. Gmail 계정 설정

1. Gmail 계정에서 2단계 인증을 활성화합니다.
2. Gmail 앱 비밀번호를 생성합니다:
   - Google 계정 설정 > 보안 > 2단계 인증 > 앱 비밀번호
   - 앱 선택: 기타 > 이름 입력 (예: "Gmail 전송 프로그램")
   - 생성된 16자리 앱 비밀번호를 복사

### 4. 환경 변수 설정

프로젝트 루트 디렉토리에 `.env` 파일을 생성하고 해당 파일에 본인의 이메일과 앱 비밀번호를 입력합니다:

```
GMAIL_USER=your.email@gmail.com
GMAIL_PASSWORD=your_app_password
```

## 실행 방법

```bash
python main_gui.py
```

## 사용 방법

1. 프로그램 실행
2. 설정 메뉴에서 Gmail 계정 정보 입력
3. 이메일 작성:
   - 수신자 이메일 주소 입력
   - 제목 입력
   - 본문 작성
   - 필요한 경우 파일 첨부
   - HTML 형식 사용 여부 선택
4. 전송 버튼 클릭

## 프로젝트 구조

```
send_gmail/
├── .env                    # 환경 변수 파일
├── requirements.txt       # 필요한 라이브러리 목록
├── main_gui.py           # GUI 프로그램 진입점
├── src/                  # 소스 코드 디렉토리
│   ├── gui/             # GUI 관련 모듈
│   ├── config.py        # 설정 관련 코드
│   ├── email_sender.py  # 이메일 전송 핵심 기능
│   └── utils.py         # 유틸리티 함수들
└── tests/               # 테스트 코드 디렉토리
```

## 테스트

```bash
python -m unittest discover tests
```

## 라이선스

MIT License

## 기여 방법

1. 이 저장소를 포크합니다.
2. 새로운 브랜치를 생성합니다 (`git checkout -b feature/amazing-feature`).
3. 변경사항을 커밋합니다 (`git commit -m 'Add some amazing feature'`).
4. 브랜치에 푸시합니다 (`git push origin feature/amazing-feature`).
5. Pull Request를 생성합니다.

## 문제 해결

- 이메일 전송 실패 시 Gmail 계정 설정과 앱 비밀번호를 확인해주세요.
- 첨부 파일 관련 문제는 파일 경로와 권한을 확인해주세요.
- 기타 문제는 Issues 탭에 등록해주세요.
