# 파이썬으로 gmail 전송 코드 계획
_Exported on 2025. 6. 9. at 21시 55분 41초 GMT+9 from Cursor (0.50.5)_

---

**User**

파이썬을 이용해서 구글의 gmail을 전송하는 코드를 작성해보려고 해.
어떻게 코드를 작성할지 전체적인 계획을 세워보자.

---

**Cursor**

Gmail을 전송하는 파이썬 코드를 작성하기 위한 계획을 세워보겠습니다. 먼저 `plan.md` 파일에 계획을 작성하겠습니다.


```markdown
# Gmail 전송 프로그램 개발 계획

## 1. 필요한 라이브러리
- `smtplib`: 이메일 전송을 위한 기본 라이브러리
- `email`: 이메일 메시지 구성
- `os`: 환경 변수 관리
- `python-dotenv`: 환경 변수 로드를 위한 라이브러리

## 2. 주요 기능
1. Gmail SMTP 서버 연결
   - SMTP 서버: smtp.gmail.com
   - 포트: 587 (TLS)
   - 보안: SSL/TLS 사용

2. 이메일 구성
   - 발신자 정보
   - 수신자 정보
   - 제목
   - 본문 내용
   - 첨부 파일 (선택사항)

3. 보안 설정
   - Gmail 앱 비밀번호 사용
   - 환경 변수를 통한 보안 정보 관리

## 3. 구현 단계
1. 환경 설정
   - 필요한 라이브러리 설치
   - .env 파일 생성 및 보안 정보 설정

2. 기본 이메일 전송 기능 구현
   - SMTP 서버 연결
   - 이메일 메시지 구성
   - 이메일 전송

3. 추가 기능 구현
   - 첨부 파일 지원
   - HTML 형식 이메일 지원
   - 다중 수신자 지원

4. 예외 처리
   - 연결 오류 처리
   - 인증 오류 처리
   - 전송 실패 처리

## 4. 사용 방법
1. Gmail 계정 설정
   - 2단계 인증 활성화
   - 앱 비밀번호 생성

2. 환경 변수 설정
   - GMAIL_USER: Gmail 주소
   - GMAIL_PASSWORD: 앱 비밀번호

3. 프로그램 실행
   - 필요한 파라미터 입력
   - 이메일 전송 실행

## 5. 테스트 계획
1. 단위 테스트
   - 이메일 구성 테스트
   - SMTP 연결 테스트

2. 통합 테스트
   - 전체 이메일 전송 프로세스 테스트
   - 다양한 시나리오 테스트
```

위와 같이 Gmail 전송 프로그램을 위한 상세한 계획을 작성했습니다. 주요 내용을 간단히 설명드리면:

1. 필요한 라이브러리들을 명시했습니다. 특히 `smtplib`와 `email` 라이브러리가 핵심이 됩니다.

2. 주요 기능으로는:
   - Gmail SMTP 서버 연결
   - 이메일 구성 (발신자, 수신자, 제목, 본문 등)
   - 보안 설정 (앱 비밀번호 사용)

3. 구현 단계를 명확히 구분했습니다:
   - 환경 설정
   - 기본 기능 구현
   - 추가 기능 구현
   - 예외 처리

4. 사용 방법과 테스트 계획도 포함했습니다.

이 계획을 바탕으로 실제 코드 구현을 시작하시겠습니까? 먼저 필요한 라이브러리를 설치하고 기본적인 이메일 전송 기능부터 구현하는 것을 추천드립니다.

---

**User**

필요한 라이브러리 목록을 @requiremensts.txt 에 작성해줘.

---

**Cursor**

`requirements.txt` 파일에 필요한 라이브러리들을 작성하겠습니다.


```plaintext
python-dotenv==1.0.0
email-validator==2.1.0.post1
```

`requirements.txt` 파일에 필요한 라이브러리들을 추가했습니다. 각 라이브러리의 용도를 설명드리면:

1. `python-dotenv`: 
   - 환경 변수 관리를 위한 라이브러리
   - Gmail 계정 정보와 앱 비밀번호를 안전하게 관리하는데 사용

2. `email-validator`:
   - 이메일 주소 유효성 검사를 위한 라이브러리
   - 이메일 주소 형식이 올바른지 확인하는데 사용

참고로 `smtplib`와 `email` 라이브러리는 파이썬 기본 라이브러리이므로 별도로 설치할 필요가 없습니다.

이제 다음 명령어로 필요한 라이브러리들을 설치할 수 있습니다:
```
pip install -r requirements.txt
```

라이브러리 설치가 완료되면 실제 코드 구현을 시작할 수 있습니다. 코드 구현을 시작하시겠습니까?

```plaintext
pip install -r requirements.txt
```

---

**User**

어떤 폴더에 어떤 파일들을 만들지에 대한 계획을 plan.md에 작성해줘.

---

**Cursor**

`plan.md` 파일에 프로젝트 구조와 파일 구성에 대한 계획을 추가하겠습니다.


죄송합니다. 파일 편집 도구에 문제가 있어 보입니다. 하지만 제가 제안한 프로젝트 구조를 설명드리겠습니다:

프로젝트의 주요 디렉토리와 파일 구조는 다음과 같습니다:

```
send_gmail/
├── .env                    # 환경 변수 파일 (Gmail 계정 정보)
├── .gitignore             # Git 무시 파일 목록
├── requirements.txt       # 필요한 라이브러리 목록
├── README.md             # 프로젝트 설명 문서
├── src/                  # 소스 코드 디렉토리
│   ├── __init__.py
│   ├── config.py         # 설정 관련 코드
│   ├── email_sender.py   # 이메일 전송 핵심 기능
│   └── utils.py          # 유틸리티 함수들
├── tests/                # 테스트 코드 디렉토리
│   ├── __init__.py
│   ├── test_config.py
│   └── test_email_sender.py
└── examples/             # 사용 예제 디렉토리
    └── send_email.py     # 기본 사용 예제
```

각 파일과 디렉토리의 역할은 다음과 같습니다:

1. `src/` 디렉토리:
   - `config.py`: 환경 변수 로드, SMTP 서버 설정 등 설정 관련 코드
   - `email_sender.py`: 이메일 전송의 핵심 기능 구현
   - `utils.py`: 이메일 주소 검증, 첨부 파일 처리 등 유틸리티 함수

2. `tests/` 디렉토리:
   - 단위 테스트와 통합 테스트 코드 포함
   - 각 모듈별 테스트 케이스 관리

3. `examples/` 디렉토리:
   - 기본적인 사용 예제 코드
   - 사용 방법 문서화

4. 루트 디렉토리:
   - `.env`: Gmail 계정 정보 저장 (보안을 위해 Git에 포함되지 않음)
   - `requirements.txt`: 필요한 라이브러리 목록
   - `README.md`: 프로젝트 설명 및 사용 방법

이 구조를 바탕으로 개발을 시작하면 좋을 것 같습니다. 어떤 파일부터 구현을 시작하시겠습니까?

```plaintext
send_gmail/
├── .env                    # 환경 변수 파일 (Gmail 계정 정보)
├── .gitignore             # Git 무시 파일 목록
├── requirements.txt       # 필요한 라이브러리 목록
├── README.md             # 프로젝트 설명 문서
├── src/                  # 소스 코드 디렉토리
│   ├── __init__.py
│   ├── config.py         # 설정 관련 코드
│   ├── email_sender.py   # 이메일 전송 핵심 기능
│   └── utils.py          # 유틸리티 함수들
├── tests/                # 테스트 코드 디렉토리
│   ├── __init__.py
│   ├── test_config.py
│   └── test_email_sender.py
└── examples/             # 사용 예제 디렉토리
    └── send_email.py     # 기본 사용 예제
```

---

**User**

@__init__.py @config.py @email_sender.py @utils.py @src 네가 알려준 구조대로 폴더와 파일을 만들었어. 각 파일의 내용을 작성해봐.

---

**Cursor**

네, 각 파일의 내용을 작성해드리겠습니다. 먼저 각 파일의 역할과 내용을 설명드리고 코드를 작성하겠습니다.

1. `__init__.py`:
```python
"""
Gmail 전송 모듈
이 모듈은 Gmail을 통해 이메일을 전송하는 기능을 제공합니다.
"""

from .email_sender import EmailSender
from .config import EmailConfig

__all__ = ['EmailSender', 'EmailConfig']
```

2. `config.py`:
```python
"""
이메일 설정을 관리하는 모듈
"""
import os
from dotenv import load_dotenv

class EmailConfig:
    def __init__(self):
        # .env 파일 로드
        load_dotenv()
        
        # Gmail 계정 정보
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
        self.username = os.getenv('GMAIL_USER')
        self.password = os.getenv('GMAIL_PASSWORD')
        
        # 기본 설정값
        self.use_tls = True
        self.timeout = 10  # 초 단위
        
    def validate(self):
        """설정값 유효성 검사"""
        if not self.username or not self.password:
            raise ValueError("Gmail 계정 정보가 설정되지 않았습니다. .env 파일을 확인해주세요.")
        
        return True
```

3. `utils.py`:
```python
"""
유틸리티 함수들을 제공하는 모듈
"""
import os
from email.mime.base import MIMEBase
from email import encoders
from email_validator import validate_email, EmailNotValidError

def validate_email_address(email: str) -> bool:
    """
    이메일 주소 유효성 검사
    
    Args:
        email (str): 검사할 이메일 주소
        
    Returns:
        bool: 유효한 이메일 주소인 경우 True
    """
    try:
        validate_email(email)
        return True
    except EmailNotValidError:
        return False

def attach_file(file_path: str) -> MIMEBase:
    """
    파일을 이메일에 첨부하기 위한 MIME 객체 생성
    
    Args:
        file_path (str): 첨부할 파일의 경로
        
    Returns:
        MIMEBase: 첨부 파일 MIME 객체
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"파일을 찾을 수 없습니다: {file_path}")
        
    with open(file_path, 'rb') as f:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(f.read())
        
    encoders.encode_base64(part)
    part.add_header(
        'Content-Disposition',
        f'attachment; filename="{os.path.basename(file_path)}"'
    )
    
    return part
```

4. `email_sender.py`:
```python
"""
Gmail 이메일 전송을 위한 핵심 모듈
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List, Optional
from .config import EmailConfig
from .utils import validate_email_address, attach_file

class EmailSender:
    def __init__(self, config: EmailConfig):
        """
        이메일 전송기 초기화
        
        Args:
            config (EmailConfig): 이메일 설정 객체
        """
        self.config = config
        self.config.validate()
        
    def send_email(
        self,
        to_emails: List[str],
        subject: str,
        body: str,
        is_html: bool = False,
        attachments: Optional[List[str]] = None
    ) -> bool:
        """
        이메일 전송
        
        Args:
            to_emails (List[str]): 수신자 이메일 주소 목록
            subject (str): 이메일 제목
            body (str): 이메일 본문
            is_html (bool): HTML 형식 여부
            attachments (Optional[List[str]]): 첨부 파일 경로 목록
            
        Returns:
            bool: 전송 성공 여부
        """
        # 수신자 이메일 주소 검증
        for email in to_emails:
            if not validate_email_address(email):
                raise ValueError(f"유효하지 않은 이메일 주소입니다: {email}")
        
        # 이메일 메시지 생성
        msg = MIMEMultipart()
        msg['From'] = self.config.username
        msg['To'] = ', '.join(to_emails)
        msg['Subject'] = subject
        
        # 본문 추가
        content_type = 'html' if is_html else 'plain'
        msg.attach(MIMEText(body, content_type, 'utf-8'))
        
        # 첨부 파일 추가
        if attachments:
            for file_path in attachments:
                msg.attach(attach_file(file_path))
        
        try:
            # SMTP 서버 연결
            with smtplib.SMTP(self.config.smtp_server, self.config.smtp_port, timeout=self.config.timeout) as server:
                if self.config.use_tls:
                    server.starttls()
                
                # 로그인
                server.login(self.config.username, self.config.password)
                
                # 이메일 전송
                server.send_message(msg)
                
            return True
            
        except Exception as e:
            raise Exception(f"이메일 전송 중 오류가 발생했습니다: {str(e)}")
```

이제 각 파일의 역할을 설명드리겠습니다:

1. `__init__.py`: 
   - 패키지 초기화 파일
   - 외부에서 사용할 주요 클래스들을 노출

2. `config.py`:
   - 이메일 설정 관리
   - 환경 변수에서 Gmail 계정 정보 로드
   - 설정값 유효성 검사

3. `utils.py`:
   - 이메일 주소 유효성 검사
   - 파일 첨부 기능
   - 기타 유틸리티 함수

4. `email_sender.py`:
   - 이메일 전송 핵심 기능
   - SMTP 서버 연결 및 이메일 전송
   - HTML 이메일 및 첨부 파일 지원

이제 이 코드를 사용하기 위해서는 `.env` 파일을 생성하고 Gmail 계정 정보를 설정해야 합니다. `.env` 파일을 생성하시겠습니까?

```python
"""
Gmail 전송 모듈
이 모듈은 Gmail을 통해 이메일을 전송하는 기능을 제공합니다.
"""

from .email_sender import EmailSender
from .config import EmailConfig

__all__ = ['EmailSender', 'EmailConfig']
```

```python
"""
이메일 설정을 관리하는 모듈
"""
import os
from dotenv import load_dotenv

class EmailConfig:
    def __init__(self):
        # .env 파일 로드
        load_dotenv()
        
        # Gmail 계정 정보
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
        self.username = os.getenv('GMAIL_USER')
        self.password = os.getenv('GMAIL_PASSWORD')
        
        # 기본 설정값
        self.use_tls = True
        self.timeout = 10  # 초 단위
        
    def validate(self):
        """설정값 유효성 검사"""
        if not self.username or not self.password:
            raise ValueError("Gmail 계정 정보가 설정되지 않았습니다. .env 파일을 확인해주세요.")
        
        return True
```

```python
"""
유틸리티 함수들을 제공하는 모듈
"""
import os
from email.mime.base import MIMEBase
from email import encoders
from email_validator import validate_email, EmailNotValidError

def validate_email_address(email: str) -> bool:
    """
    이메일 주소 유효성 검사
    
    Args:
        email (str): 검사할 이메일 주소
        
    Returns:
        bool: 유효한 이메일 주소인 경우 True
    """
    try:
        validate_email(email)
        return True
    except EmailNotValidError:
        return False

def attach_file(file_path: str) -> MIMEBase:
    """
    파일을 이메일에 첨부하기 위한 MIME 객체 생성
    
    Args:
        file_path (str): 첨부할 파일의 경로
        
    Returns:
        MIMEBase: 첨부 파일 MIME 객체
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"파일을 찾을 수 없습니다: {file_path}")
        
    with open(file_path, 'rb') as f:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(f.read())
        
    encoders.encode_base64(part)
    part.add_header(
        'Content-Disposition',
        f'attachment; filename="{os.path.basename(file_path)}"'
    )
    
    return part
```

```python
"""
Gmail 이메일 전송을 위한 핵심 모듈
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List, Optional
from .config import EmailConfig
from .utils import validate_email_address, attach_file

class EmailSender:
    def __init__(self, config: EmailConfig):
        """
        이메일 전송기 초기화
        
        Args:
            config (EmailConfig): 이메일 설정 객체
        """
        self.config = config
        self.config.validate()
        
    def send_email(
        self,
        to_emails: List[str],
        subject: str,
        body: str,
        is_html: bool = False,
        attachments: Optional[List[str]] = None
    ) -> bool:
        """
        이메일 전송
        
        Args:
            to_emails (List[str]): 수신자 이메일 주소 목록
            subject (str): 이메일 제목
            body (str): 이메일 본문
            is_html (bool): HTML 형식 여부
            attachments (Optional[List[str]]): 첨부 파일 경로 목록
            
        Returns:
            bool: 전송 성공 여부
        """
        # 수신자 이메일 주소 검증
        for email in to_emails:
            if not validate_email_address(email):
                raise ValueError(f"유효하지 않은 이메일 주소입니다: {email}")
        
        # 이메일 메시지 생성
        msg = MIMEMultipart()
        msg['From'] = self.config.username
        msg['To'] = ', '.join(to_emails)
        msg['Subject'] = subject
        
        # 본문 추가
        content_type = 'html' if is_html else 'plain'
        msg.attach(MIMEText(body, content_type, 'utf-8'))
        
        # 첨부 파일 추가
        if attachments:
            for file_path in attachments:
                msg.attach(attach_file(file_path))
        
        try:
            # SMTP 서버 연결
            with smtplib.SMTP(self.config.smtp_server, self.config.smtp_port, timeout=self.config.timeout) as server:
                if self.config.use_tls:
                    server.starttls()
                
                # 로그인
                server.login(self.config.username, self.config.password)
                
                # 이메일 전송
                server.send_message(msg)
                
            return True
            
        except Exception as e:
            raise Exception(f"이메일 전송 중 오류가 발생했습니다: {str(e)}")
```

---

**User**

Optional 클래스에 대해서 설명해줘.

---

**Cursor**

`Optional` 클래스에 대해 설명드리겠습니다.

`Optional`은 Python의 `typing` 모듈에서 제공하는 타입 힌트(Type Hint) 기능입니다. 이는 Python 3.5부터 도입된 기능으로, 변수나 매개변수의 타입을 명시적으로 지정할 수 있게 해줍니다.

`Optional[T]`의 주요 특징은 다음과 같습니다:

1. **기본 개념**:
   - `Optional[T]`는 `Union[T, None]`과 동일한 의미입니다.
   - 즉, 해당 값이 타입 T이거나 `None`일 수 있다는 것을 나타냅니다.

2. **사용 예시**:
```python
from typing import Optional

# 이 함수는 문자열 또는 None을 반환할 수 있음을 나타냅니다
def get_name(user_id: int) -> Optional[str]:
    if user_id in users:
        return users[user_id]
    return None

# 매개변수가 문자열 또는 None일 수 있음을 나타냅니다
def process_name(name: Optional[str] = None):
    if name is None:
        print("이름이 제공되지 않았습니다")
    else:
        print(f"이름: {name}")
```

3. **`email_sender.py`에서의 사용**:
```python
def send_email(
    self,
    to_emails: List[str],
    subject: str,
    body: str,
    is_html: bool = False,
    attachments: Optional[List[str]] = None  # 첨부 파일 목록이 없을 수 있음을 나타냄
) -> bool:
```
- `attachments` 매개변수는 `List[str]` 타입이거나 `None`일 수 있음을 나타냅니다.
- 이는 첨부 파일이 있을 수도 있고 없을 수도 있다는 것을 의미합니다.

4. **장점**:
   - 코드의 가독성 향상
   - IDE의 자동 완성 및 타입 체크 기능 지원
   - 버그 예방에 도움
   - 문서화 효과

5. **실제 사용 시 주의사항**:
```python
def process_data(data: Optional[str]):
    # None 체크가 필요합니다
    if data is None:
        return "데이터 없음"
    
    # 이 시점에서는 data가 str 타입임이 보장됩니다
    return data.upper()
```

`Optional`은 특히 함수의 매개변수나 반환값이 있을 수도 있고 없을 수도 있는 경우에 유용하게 사용됩니다. 이는 코드의 의도를 명확하게 전달하고, 타입 안정성을 높이는 데 도움이 됩니다.

```python
from typing import Optional

# 이 함수는 문자열 또는 None을 반환할 수 있음을 나타냅니다
def get_name(user_id: int) -> Optional[str]:
    if user_id in users:
        return users[user_id]
    return None

# 매개변수가 문자열 또는 None일 수 있음을 나타냅니다
def process_name(name: Optional[str] = None):
    if name is None:
        print("이름이 제공되지 않았습니다")
    else:
        print(f"이름: {name}")
```

```python
def send_email(
    self,
    to_emails: List[str],
    subject: str,
    body: str,
    is_html: bool = False,
    attachments: Optional[List[str]] = None  # 첨부 파일 목록이 없을 수 있음을 나타냄
) -> bool:
```

```python
def process_data(data: Optional[str]):
    # None 체크가 필요합니다
    if data is None:
        return "데이터 없음"
    
    # 이 시점에서는 data가 str 타입임이 보장됩니다
    return data.upper()
```

---

**User**

@__init__.py @test_config.py @tests @test_email_sender.py @plan.md 계획에 따라서 테스트 코드 작성해줘.

---

**Cursor**

테스트 코드를 작성해드리겠습니다. 각 파일의 역할과 내용을 설명드리고 코드를 작성하겠습니다.

1. `tests/__init__.py`:
```python
"""
테스트 패키지 초기화 파일
"""
```

2. `tests/test_config.py`:
```python
"""
EmailConfig 클래스에 대한 테스트
"""
import os
import unittest
from unittest.mock import patch
from src.config import EmailConfig

class TestEmailConfig(unittest.TestCase):
    def setUp(self):
        """테스트 전 환경 설정"""
        self.test_env = {
            'GMAIL_USER': 'test@gmail.com',
            'GMAIL_PASSWORD': 'test_password'
        }
    
    def test_init_with_valid_env(self):
        """유효한 환경 변수로 초기화 테스트"""
        with patch.dict(os.environ, self.test_env):
            config = EmailConfig()
            self.assertEqual(config.username, 'test@gmail.com')
            self.assertEqual(config.password, 'test_password')
            self.assertEqual(config.smtp_server, 'smtp.gmail.com')
            self.assertEqual(config.smtp_port, 587)
            self.assertTrue(config.use_tls)
    
    def test_init_without_env(self):
        """환경 변수 없이 초기화 테스트"""
        with patch.dict(os.environ, {}, clear=True):
            config = EmailConfig()
            self.assertIsNone(config.username)
            self.assertIsNone(config.password)
    
    def test_validate_with_valid_config(self):
        """유효한 설정으로 검증 테스트"""
        with patch.dict(os.environ, self.test_env):
            config = EmailConfig()
            self.assertTrue(config.validate())
    
    def test_validate_with_invalid_config(self):
        """잘못된 설정으로 검증 테스트"""
        with patch.dict(os.environ, {}, clear=True):
            config = EmailConfig()
            with self.assertRaises(ValueError):
                config.validate()

if __name__ == '__main__':
    unittest.main()
```

3. `tests/test_email_sender.py`:
```python
"""
EmailSender 클래스에 대한 테스트
"""
import unittest
from unittest.mock import patch, MagicMock
from src.email_sender import EmailSender
from src.config import EmailConfig
from src.utils import validate_email_address

class TestEmailSender(unittest.TestCase):
    def setUp(self):
        """테스트 전 환경 설정"""
        self.config = EmailConfig()
        self.config.username = 'test@gmail.com'
        self.config.password = 'test_password'
        self.sender = EmailSender(self.config)
        
        self.test_email = {
            'to_emails': ['recipient@example.com'],
            'subject': 'Test Subject',
            'body': 'Test Body',
            'is_html': False,
            'attachments': None
        }
    
    def test_send_email_with_valid_data(self):
        """유효한 데이터로 이메일 전송 테스트"""
        with patch('smtplib.SMTP') as mock_smtp:
            # SMTP 서버 모의 설정
            mock_smtp_instance = MagicMock()
            mock_smtp.return_value.__enter__.return_value = mock_smtp_instance
            
            # 이메일 전송 테스트
            result = self.sender.send_email(**self.test_email)
            
            # 검증
            self.assertTrue(result)
            mock_smtp_instance.starttls.assert_called_once()
            mock_smtp_instance.login.assert_called_once_with(
                self.config.username, 
                self.config.password
            )
            mock_smtp_instance.send_message.assert_called_once()
    
    def test_send_email_with_invalid_email(self):
        """잘못된 이메일 주소로 전송 시도 테스트"""
        invalid_email = {
            'to_emails': ['invalid-email'],
            'subject': 'Test Subject',
            'body': 'Test Body'
        }
        
        with self.assertRaises(ValueError):
            self.sender.send_email(**invalid_email)
    
    def test_send_email_with_attachment(self):
        """첨부 파일이 있는 이메일 전송 테스트"""
        test_email_with_attachment = self.test_email.copy()
        test_email_with_attachment['attachments'] = ['test.txt']
        
        with patch('smtplib.SMTP') as mock_smtp, \
             patch('os.path.exists', return_value=True), \
             patch('builtins.open', unittest.mock.mock_open(read_data='test')):
            
            mock_smtp_instance = MagicMock()
            mock_smtp.return_value.__enter__.return_value = mock_smtp_instance
            
            result = self.sender.send_email(**test_email_with_attachment)
            
            self.assertTrue(result)
            mock_smtp_instance.send_message.assert_called_once()
    
    def test_send_email_with_html(self):
        """HTML 형식 이메일 전송 테스트"""
        html_email = self.test_email.copy()
        html_email['is_html'] = True
        html_email['body'] = '<h1>Test HTML</h1>'
        
        with patch('smtplib.SMTP') as mock_smtp:
            mock_smtp_instance = MagicMock()
            mock_smtp.return_value.__enter__.return_value = mock_smtp_instance
            
            result = self.sender.send_email(**html_email)
            
            self.assertTrue(result)
            mock_smtp_instance.send_message.assert_called_once()

if __name__ == '__main__':
    unittest.main()
```

각 테스트 파일의 역할을 설명드리면:

1. `test_config.py`:
   - `EmailConfig` 클래스의 기능 테스트
   - 환경 변수 로드 테스트
   - 설정값 유효성 검사 테스트

2. `test_email_sender.py`:
   - `EmailSender` 클래스의 기능 테스트
   - 이메일 전송 기능 테스트
   - 첨부 파일 처리 테스트
   - HTML 이메일 전송 테스트
   - 오류 처리 테스트

테스트를 실행하려면 다음 명령어를 사용하시면 됩니다:
```bash
python -m unittest discover tests
```

이 테스트 코드들은 다음을 테스트합니다:
- 환경 변수 설정 및 로드
- 이메일 주소 유효성 검사
- 이메일 전송 기능
- 첨부 파일 처리
- HTML 이메일 지원
- 오류 처리

테스트를 실행하기 전에 필요한 라이브러리가 모두 설치되어 있는지 확인해주세요.

```python
"""
테스트 패키지 초기화 파일
"""
```

```python
"""
EmailConfig 클래스에 대한 테스트
"""
import os
import unittest
from unittest.mock import patch
from src.config import EmailConfig

class TestEmailConfig(unittest.TestCase):
    def setUp(self):
        """테스트 전 환경 설정"""
        self.test_env = {
            'GMAIL_USER': 'test@gmail.com',
            'GMAIL_PASSWORD': 'test_password'
        }
    
    def test_init_with_valid_env(self):
        """유효한 환경 변수로 초기화 테스트"""
        with patch.dict(os.environ, self.test_env):
            config = EmailConfig()
            self.assertEqual(config.username, 'test@gmail.com')
            self.assertEqual(config.password, 'test_password')
            self.assertEqual(config.smtp_server, 'smtp.gmail.com')
            self.assertEqual(config.smtp_port, 587)
            self.assertTrue(config.use_tls)
    
    def test_init_without_env(self):
        """환경 변수 없이 초기화 테스트"""
        with patch.dict(os.environ, {}, clear=True):
            config = EmailConfig()
            self.assertIsNone(config.username)
            self.assertIsNone(config.password)
    
    def test_validate_with_valid_config(self):
        """유효한 설정으로 검증 테스트"""
        with patch.dict(os.environ, self.test_env):
            config = EmailConfig()
            self.assertTrue(config.validate())
    
    def test_validate_with_invalid_config(self):
        """잘못된 설정으로 검증 테스트"""
        with patch.dict(os.environ, {}, clear=True):
            config = EmailConfig()
            with self.assertRaises(ValueError):
                config.validate()

if __name__ == '__main__':
    unittest.main()
```

```python
"""
EmailSender 클래스에 대한 테스트
"""
import unittest
from unittest.mock import patch, MagicMock
from src.email_sender import EmailSender
from src.config import EmailConfig
from src.utils import validate_email_address

class TestEmailSender(unittest.TestCase):
    def setUp(self):
        """테스트 전 환경 설정"""
        self.config = EmailConfig()
        self.config.username = 'test@gmail.com'
        self.config.password = 'test_password'
        self.sender = EmailSender(self.config)
        
        self.test_email = {
            'to_emails': ['recipient@example.com'],
            'subject': 'Test Subject',
            'body': 'Test Body',
            'is_html': False,
            'attachments': None
        }
    
    def test_send_email_with_valid_data(self):
        """유효한 데이터로 이메일 전송 테스트"""
        with patch('smtplib.SMTP') as mock_smtp:
            # SMTP 서버 모의 설정
            mock_smtp_instance = MagicMock()
            mock_smtp.return_value.__enter__.return_value = mock_smtp_instance
            
            # 이메일 전송 테스트
            result = self.sender.send_email(**self.test_email)
            
            # 검증
            self.assertTrue(result)
            mock_smtp_instance.starttls.assert_called_once()
            mock_smtp_instance.login.assert_called_once_with(
                self.config.username, 
                self.config.password
            )
            mock_smtp_instance.send_message.assert_called_once()
    
    def test_send_email_with_invalid_email(self):
        """잘못된 이메일 주소로 전송 시도 테스트"""
        invalid_email = {
            'to_emails': ['invalid-email'],
            'subject': 'Test Subject',
            'body': 'Test Body'
        }
        
        with self.assertRaises(ValueError):
            self.sender.send_email(**invalid_email)
    
    def test_send_email_with_attachment(self):
        """첨부 파일이 있는 이메일 전송 테스트"""
        test_email_with_attachment = self.test_email.copy()
        test_email_with_attachment['attachments'] = ['test.txt']
        
        with patch('smtplib.SMTP') as mock_smtp, \
             patch('os.path.exists', return_value=True), \
             patch('builtins.open', unittest.mock.mock_open(read_data='test')):
            
            mock_smtp_instance = MagicMock()
            mock_smtp.return_value.__enter__.return_value = mock_smtp_instance
            
            result = self.sender.send_email(**test_email_with_attachment)
            
            self.assertTrue(result)
            mock_smtp_instance.send_message.assert_called_once()
    
    def test_send_email_with_html(self):
        """HTML 형식 이메일 전송 테스트"""
        html_email = self.test_email.copy()
        html_email['is_html'] = True
        html_email['body'] = '<h1>Test HTML</h1>'
        
        with patch('smtplib.SMTP') as mock_smtp:
            mock_smtp_instance = MagicMock()
            mock_smtp.return_value.__enter__.return_value = mock_smtp_instance
            
            result = self.sender.send_email(**html_email)
            
            self.assertTrue(result)
            mock_smtp_instance.send_message.assert_called_once()

if __name__ == '__main__':
    unittest.main()
```

```shellscript
python -m unittest discover tests
```

---

**User**

테스트 결과 문제가 없었어. 이제 직접 제목, 본문, 받을 이메일 목록을 작성해서 이메일 전송을 해보려고 해.
main.py에 코드 작성해줘.

---

**Cursor**

`main.py`에 이메일 전송을 위한 예제 코드를 작성해드리겠습니다.

```python
"""
Gmail 이메일 전송 예제 프로그램
"""
import os
from dotenv import load_dotenv
from src.email_sender import EmailSender
from src.config import EmailConfig

def main():
    # .env 파일 로드
    load_dotenv()
    
    # 이메일 설정
    config = EmailConfig()
    
    try:
        # 이메일 전송기 초기화
        sender = EmailSender(config)
        
        # 이메일 정보 설정
        to_emails = [
            "recipient1@example.com",  # 수신자 1
            "recipient2@example.com"   # 수신자 2
        ]
        
        subject = "테스트 이메일입니다"
        
        # HTML 형식의 이메일 본문
        body = """
        <html>
            <body>
                <h1>안녕하세요!</h1>
                <p>이것은 <b>테스트 이메일</b>입니다.</p>
                <p>다음과 같은 기능을 테스트하고 있습니다:</p>
                <ul>
                    <li>HTML 형식 이메일</li>
                    <li>다중 수신자</li>
                    <li>한글 지원</li>
                </ul>
                <p>감사합니다.</p>
            </body>
        </html>
        """
        
        # 첨부 파일 목록 (선택사항)
        attachments = [
            # "example.pdf",  # 첨부할 파일이 있다면 주석 해제
            # "image.jpg"
        ]
        
        # 이메일 전송
        result = sender.send_email(
            to_emails=to_emails,
            subject=subject,
            body=body,
            is_html=True,  # HTML 형식 사용
            attachments=attachments
        )
        
        if result:
            print("이메일이 성공적으로 전송되었습니다!")
        else:
            print("이메일 전송에 실패했습니다.")
            
    except Exception as e:
        print(f"오류가 발생했습니다: {str(e)}")

if __name__ == "__main__":
    main()
```

이 코드를 실행하기 전에 다음 사항들을 확인해주세요:

1. `.env` 파일이 프로젝트 루트 디렉토리에 있는지 확인하고, 다음과 같은 형식으로 Gmail 계정 정보를 설정해주세요:
```
GMAIL_USER=your.email@gmail.com
GMAIL_PASSWORD=your_app_password
```

2. Gmail 계정에서 다음 설정이 되어 있어야 합니다:
   - 2단계 인증이 활성화되어 있어야 함
   - 앱 비밀번호가 생성되어 있어야 함

3. `to_emails` 리스트에 실제 수신자 이메일 주소를 입력해주세요.

4. 첨부 파일을 사용하려면 `attachments` 리스트에 파일 경로를 추가하고 주석을 해제해주세요.

이 코드는 다음과 같은 기능을 제공합니다:
- HTML 형식의 이메일 전송
- 다중 수신자 지원
- 첨부 파일 지원 (선택사항)
- 한글 지원
- 오류 처리

코드를 실행하려면 터미널에서 다음 명령어를 입력하세요:
```bash
python main.py
```

실제 사용 시에는 `to_emails`, `subject`, `body` 등의 내용을 원하는 대로 수정하시면 됩니다. 첨부 파일이 필요한 경우 `attachments` 리스트에 파일 경로를 추가하시면 됩니다.

```python
"""
Gmail 이메일 전송 예제 프로그램
"""
import os
from dotenv import load_dotenv
from src.email_sender import EmailSender
from src.config import EmailConfig

def main():
    # .env 파일 로드
    load_dotenv()
    
    # 이메일 설정
    config = EmailConfig()
    
    try:
        # 이메일 전송기 초기화
        sender = EmailSender(config)
        
        # 이메일 정보 설정
        to_emails = [
            "recipient1@example.com",  # 수신자 1
            "recipient2@example.com"   # 수신자 2
        ]
        
        subject = "테스트 이메일입니다"
        
        # HTML 형식의 이메일 본문
        body = """
        <html>
            <body>
                <h1>안녕하세요!</h1>
                <p>이것은 <b>테스트 이메일</b>입니다.</p>
                <p>다음과 같은 기능을 테스트하고 있습니다:</p>
                <ul>
                    <li>HTML 형식 이메일</li>
                    <li>다중 수신자</li>
                    <li>한글 지원</li>
                </ul>
                <p>감사합니다.</p>
            </body>
        </html>
        """
        
        # 첨부 파일 목록 (선택사항)
        attachments = [
            # "example.pdf",  # 첨부할 파일이 있다면 주석 해제
            # "image.jpg"
        ]
        
        # 이메일 전송
        result = sender.send_email(
            to_emails=to_emails,
            subject=subject,
            body=body,
            is_html=True,  # HTML 형식 사용
            attachments=attachments
        )
        
        if result:
            print("이메일이 성공적으로 전송되었습니다!")
        else:
            print("이메일 전송에 실패했습니다.")
            
    except Exception as e:
        print(f"오류가 발생했습니다: {str(e)}")

if __name__ == "__main__":
    main()
```

```plaintext
GMAIL_USER=your.email@gmail.com
GMAIL_PASSWORD=your_app_password
```

```shellscript
python main.py
```

---

**User**

html 형식뿐만 아니라 plain 형식으로 이메일을 보내는 예제도 작성해줘.

---

**Cursor**

`main.py`에 plain 텍스트 형식의 이메일 전송 예제를 추가하겠습니다.

```python
"""
Gmail 이메일 전송 예제 프로그램
"""
import os
from dotenv import load_dotenv
from src.email_sender import EmailSender
from src.config import EmailConfig

def send_html_email(sender: EmailSender):
    """HTML 형식 이메일 전송"""
    to_emails = [
        "miraclelee0613@gmail.com",
    ]
    
    subject = "HTML 형식 테스트 이메일"
    
    body = """
    <html>
        <body>
            <h1>안녕하세요!</h1>
            <p>이것은 <b>테스트 이메일</b>입니다.</p>
            <p>다음과 같은 기능을 테스트하고 있습니다:</p>
            <ul>
                <li>HTML 형식 이메일</li>
                <li>다중 수신자</li>
                <li>한글 지원</li>
            </ul>
            <p>감사합니다.</p>
        </body>
    </html>
    """
    
    result = sender.send_email(
        to_emails=to_emails,
        subject=subject,
        body=body,
        is_html=True
    )
    
    if result:
        print("HTML 이메일이 성공적으로 전송되었습니다!")
    else:
        print("HTML 이메일 전송에 실패했습니다.")

def send_plain_email(sender: EmailSender):
    """일반 텍스트 형식 이메일 전송"""
    to_emails = [
        "miraclelee0613@gmail.com",
    ]
    
    subject = "일반 텍스트 테스트 이메일"
    
    body = """
    안녕하세요!
    
    이것은 일반 텍스트 형식의 테스트 이메일입니다.
    
    다음과 같은 기능을 테스트하고 있습니다:
    - 일반 텍스트 형식 이메일
    - 다중 수신자
    - 한글 지원
    
    감사합니다.
    """
    
    result = sender.send_email(
        to_emails=to_emails,
        subject=subject,
        body=body,
        is_html=False  # 일반 텍스트 형식 사용
    )
    
    if result:
        print("일반 텍스트 이메일이 성공적으로 전송되었습니다!")
    else:
        print("일반 텍스트 이메일 전송에 실패했습니다.")

def main():
    # .env 파일 로드
    load_dotenv()
    
    # 이메일 설정
    config = EmailConfig()
    
    try:
        # 이메일 전송기 초기화
        sender = EmailSender(config)
        
        # HTML 형식 이메일 전송
        print("\n=== HTML 형식 이메일 전송 ===")
        send_html_email(sender)
        
        # 일반 텍스트 형식 이메일 전송
        print("\n=== 일반 텍스트 형식 이메일 전송 ===")
        send_plain_email(sender)
            
    except Exception as e:
        print(f"오류가 발생했습니다: {str(e)}")

if __name__ == "__main__":
    main()
```

주요 변경사항:

1. 코드를 함수로 분리하여 가독성을 높였습니다:
   - `send_html_email()`: HTML 형식 이메일 전송
   - `send_plain_email()`: 일반 텍스트 형식 이메일 전송

2. 일반 텍스트 이메일의 특징:
   - `is_html=False`로 설정
   - HTML 태그 없이 순수 텍스트로 작성
   - 들여쓰기와 줄바꿈으로 가독성 확보

3. 각 이메일 전송 결과를 구분하여 출력

이 코드를 실행하면 HTML 형식과 일반 텍스트 형식의 이메일이 순차적으로 전송됩니다. 각각의 형식에 맞는 이메일이 수신자의 이메일 클라이언트에 표시됩니다.

실행 방법은 동일합니다:
```bash
python main.py
```

두 형식의 이메일을 모두 테스트해보시면, 각각의 장단점을 확인하실 수 있습니다:
- HTML 형식: 서식과 스타일링이 가능하지만, 일부 이메일 클라이언트에서 제한될 수 있음
- 일반 텍스트: 모든 이메일 클라이언트에서 안정적으로 표시되지만, 서식과 스타일링이 불가능

```python
"""
Gmail 이메일 전송 예제 프로그램
"""
import os
from dotenv import load_dotenv
from src.email_sender import EmailSender
from src.config import EmailConfig

def send_html_email(sender: EmailSender):
    """HTML 형식 이메일 전송"""
    to_emails = [
        "miraclelee0613@gmail.com",
    ]
    
    subject = "HTML 형식 테스트 이메일"
    
    body = """
    <html>
        <body>
            <h1>안녕하세요!</h1>
            <p>이것은 <b>테스트 이메일</b>입니다.</p>
            <p>다음과 같은 기능을 테스트하고 있습니다:</p>
            <ul>
                <li>HTML 형식 이메일</li>
                <li>다중 수신자</li>
                <li>한글 지원</li>
            </ul>
            <p>감사합니다.</p>
        </body>
    </html>
    """
    
    result = sender.send_email(
        to_emails=to_emails,
        subject=subject,
        body=body,
        is_html=True
    )
    
    if result:
        print("HTML 이메일이 성공적으로 전송되었습니다!")
    else:
        print("HTML 이메일 전송에 실패했습니다.")

def send_plain_email(sender: EmailSender):
    """일반 텍스트 형식 이메일 전송"""
    to_emails = [
        "miraclelee0613@gmail.com",
    ]
    
    subject = "일반 텍스트 테스트 이메일"
    
    body = """
    안녕하세요!
    
    이것은 일반 텍스트 형식의 테스트 이메일입니다.
    
    다음과 같은 기능을 테스트하고 있습니다:
    - 일반 텍스트 형식 이메일
    - 다중 수신자
    - 한글 지원
    
    감사합니다.
    """
    
    result = sender.send_email(
        to_emails=to_emails,
        subject=subject,
        body=body,
        is_html=False  # 일반 텍스트 형식 사용
    )
    
    if result:
        print("일반 텍스트 이메일이 성공적으로 전송되었습니다!")
    else:
        print("일반 텍스트 이메일 전송에 실패했습니다.")

def main():
    # .env 파일 로드
    load_dotenv()
    
    # 이메일 설정
    config = EmailConfig()
    
    try:
        # 이메일 전송기 초기화
        sender = EmailSender(config)
        
        # HTML 형식 이메일 전송
        print("\n=== HTML 형식 이메일 전송 ===")
        send_html_email(sender)
        
        # 일반 텍스트 형식 이메일 전송
        print("\n=== 일반 텍스트 형식 이메일 전송 ===")
        send_plain_email(sender)
            
    except Exception as e:
        print(f"오류가 발생했습니다: {str(e)}")

if __name__ == "__main__":
    main()
```

```shellscript
python main.py
```

---

**User**

제목, 본문, html 형식인지 여부, 받는 이메일주소 리스트 등을 매개변수로 받는 함수를 작성해줘.
이메일을 보낼 때 필요한 세팅들을 알아서 해주는 함수로 작성하면 될 것 같아.

---

**Cursor**

이메일 전송을 위한 통합 함수를 작성해드리겠습니다. `main.py`를 다음과 같이 수정하겠습니다:

```python
"""
Gmail 이메일 전송 예제 프로그램
"""
import os
from typing import List, Optional
from dotenv import load_dotenv
from src.email_sender import EmailSender
from src.config import EmailConfig

def send_email(
    to_emails: List[str],
    subject: str,
    body: str,
    is_html: bool = False,
    attachments: Optional[List[str]] = None
) -> bool:
    """
    이메일 전송 함수
    
    Args:
        to_emails (List[str]): 수신자 이메일 주소 목록
        subject (str): 이메일 제목
        body (str): 이메일 본문
        is_html (bool): HTML 형식 사용 여부 (기본값: False)
        attachments (Optional[List[str]]): 첨부 파일 경로 목록 (기본값: None)
    
    Returns:
        bool: 이메일 전송 성공 여부
    
    Raises:
        Exception: 이메일 전송 중 오류 발생 시
    """
    try:
        # .env 파일 로드
        load_dotenv()
        
        # 이메일 설정
        config = EmailConfig()
        
        # 이메일 전송기 초기화
        sender = EmailSender(config)
        
        # 이메일 전송
        result = sender.send_email(
            to_emails=to_emails,
            subject=subject,
            body=body,
            is_html=is_html,
            attachments=attachments
        )
        
        if result:
            print(f"이메일이 성공적으로 전송되었습니다! (수신자: {', '.join(to_emails)})")
        else:
            print("이메일 전송에 실패했습니다.")
            
        return result
        
    except Exception as e:
        print(f"이메일 전송 중 오류가 발생했습니다: {str(e)}")
        raise

def main():
    # HTML 형식 이메일 전송 예제
    html_body = """
    <html>
        <body>
            <h1>안녕하세요!</h1>
            <p>이것은 <b>테스트 이메일</b>입니다.</p>
            <p>다음과 같은 기능을 테스트하고 있습니다:</p>
            <ul>
                <li>HTML 형식 이메일</li>
                <li>다중 수신자</li>
                <li>한글 지원</li>
            </ul>
            <p>감사합니다.</p>
        </body>
    </html>
    """
    
    # 일반 텍스트 이메일 전송 예제
    plain_body = """
    안녕하세요!
    
    이것은 일반 텍스트 형식의 테스트 이메일입니다.
    
    다음과 같은 기능을 테스트하고 있습니다:
    - 일반 텍스트 형식 이메일
    - 다중 수신자
    - 한글 지원
    
    감사합니다.
    """
    
    try:
        # HTML 형식 이메일 전송
        print("\n=== HTML 형식 이메일 전송 ===")
        send_email(
            to_emails=["miraclelee0613@gmail.com"],
            subject="HTML 형식 테스트 이메일",
            body=html_body,
            is_html=True
        )
        
        # 일반 텍스트 형식 이메일 전송
        print("\n=== 일반 텍스트 형식 이메일 전송 ===")
        send_email(
            to_emails=["miraclelee0613@gmail.com"],
            subject="일반 텍스트 테스트 이메일",
            body=plain_body,
            is_html=False
        )
        
        # 첨부 파일이 있는 이메일 전송 예제
        print("\n=== 첨부 파일이 있는 이메일 전송 ===")
        send_email(
            to_emails=["miraclelee0613@gmail.com"],
            subject="첨부 파일 테스트 이메일",
            body="첨부 파일이 있는 테스트 이메일입니다.",
            is_html=False,
            attachments=["example.pdf"]  # 실제 파일 경로로 수정 필요
        )

    except Exception as e:
        print(f"오류가 발생했습니다: {str(e)}")

if __name__ == "__main__":
    main()
```

주요 변경사항:

1. 통합 `send_email()` 함수 추가:
   - 모든 필요한 매개변수를 받음
   - 환경 설정을 자동으로 처리
   - 오류 처리 포함
   - 전송 결과 반환

2. 함수 매개변수:
   - `to_emails`: 수신자 이메일 주소 목록
   - `subject`: 이메일 제목
   - `body`: 이메일 본문
   - `is_html`: HTML 형식 사용 여부 (선택적)
   - `attachments`: 첨부 파일 목록 (선택적)

3. 사용 예제:
   - HTML 형식 이메일
   - 일반 텍스트 이메일
   - 첨부 파일이 있는 이메일

이제 다음과 같이 간단하게 이메일을 전송할 수 있습니다:

```python
# 기본 사용 예시
send_email(
    to_emails=["recipient@example.com"],
    subject="테스트 이메일",
    body="이메일 본문",
    is_html=False
)

# HTML 형식 이메일 예시
send_email(
    to_emails=["recipient@example.com"],
    subject="HTML 테스트",
    body="<h1>HTML 본문</h1>",
    is_html=True
)

# 첨부 파일이 있는 이메일 예시
send_email(
    to_emails=["recipient@example.com"],
    subject="첨부 파일 테스트",
    body="첨부 파일이 있는 이메일입니다.",
    attachments=["file.pdf"]
)
```

이 함수는 이메일 전송에 필요한 모든 설정을 자동으로 처리하며, 오류 처리도 포함되어 있습니다. 필요한 경우 추가적인 기능이나 옵션을 쉽게 확장할 수 있습니다.

```python
"""
Gmail 이메일 전송 예제 프로그램
"""
import os
from typing import List, Optional
from dotenv import load_dotenv
from src.email_sender import EmailSender
from src.config import EmailConfig

def send_email(
    to_emails: List[str],
    subject: str,
    body: str,
    is_html: bool = False,
    attachments: Optional[List[str]] = None
) -> bool:
    """
    이메일 전송 함수
    
    Args:
        to_emails (List[str]): 수신자 이메일 주소 목록
        subject (str): 이메일 제목
        body (str): 이메일 본문
        is_html (bool): HTML 형식 사용 여부 (기본값: False)
        attachments (Optional[List[str]]): 첨부 파일 경로 목록 (기본값: None)
    
    Returns:
        bool: 이메일 전송 성공 여부
    
    Raises:
        Exception: 이메일 전송 중 오류 발생 시
    """
    try:
        # .env 파일 로드
        load_dotenv()
        
        # 이메일 설정
        config = EmailConfig()
        
        # 이메일 전송기 초기화
        sender = EmailSender(config)
        
        # 이메일 전송
        result = sender.send_email(
            to_emails=to_emails,
            subject=subject,
            body=body,
            is_html=is_html,
            attachments=attachments
        )
        
        if result:
            print(f"이메일이 성공적으로 전송되었습니다! (수신자: {', '.join(to_emails)})")
        else:
            print("이메일 전송에 실패했습니다.")
            
        return result
        
    except Exception as e:
        print(f"이메일 전송 중 오류가 발생했습니다: {str(e)}")
        raise

def main():
    # HTML 형식 이메일 전송 예제
    html_body = """
    <html>
        <body>
            <h1>안녕하세요!</h1>
            <p>이것은 <b>테스트 이메일</b>입니다.</p>
            <p>다음과 같은 기능을 테스트하고 있습니다:</p>
            <ul>
                <li>HTML 형식 이메일</li>
                <li>다중 수신자</li>
                <li>한글 지원</li>
            </ul>
            <p>감사합니다.</p>
        </body>
    </html>
    """
    
    # 일반 텍스트 이메일 전송 예제
    plain_body = """
    안녕하세요!
    
    이것은 일반 텍스트 형식의 테스트 이메일입니다.
    
    다음과 같은 기능을 테스트하고 있습니다:
    - 일반 텍스트 형식 이메일
    - 다중 수신자
    - 한글 지원
    
    감사합니다.
    """
    
    try:
        # HTML 형식 이메일 전송
        print("\n=== HTML 형식 이메일 전송 ===")
        send_email(
            to_emails=["miraclelee0613@gmail.com"],
            subject="HTML 형식 테스트 이메일",
            body=html_body,
            is_html=True
        )
        
        # 일반 텍스트 형식 이메일 전송
        print("\n=== 일반 텍스트 형식 이메일 전송 ===")
        send_email(
            to_emails=["miraclelee0613@gmail.com"],
            subject="일반 텍스트 테스트 이메일",
            body=plain_body,
            is_html=False
        )
        
        # 첨부 파일이 있는 이메일 전송 예제
        print("\n=== 첨부 파일이 있는 이메일 전송 ===")
        send_email(
            to_emails=["miraclelee0613@gmail.com"],
            subject="첨부 파일 테스트 이메일",
            body="첨부 파일이 있는 테스트 이메일입니다.",
            is_html=False,
            attachments=["example.pdf"]  # 실제 파일 경로로 수정 필요
        )

    except Exception as e:
        print(f"오류가 발생했습니다: {str(e)}")

if __name__ == "__main__":
    main()
```

```python
# 기본 사용 예시
send_email(
    to_emails=["recipient@example.com"],
    subject="테스트 이메일",
    body="이메일 본문",
    is_html=False
)

# HTML 형식 이메일 예시
send_email(
    to_emails=["recipient@example.com"],
    subject="HTML 테스트",
    body="<h1>HTML 본문</h1>",
    is_html=True
)

# 첨부 파일이 있는 이메일 예시
send_email(
    to_emails=["recipient@example.com"],
    subject="첨부 파일 테스트",
    body="첨부 파일이 있는 이메일입니다.",
    attachments=["file.pdf"]
)
```

---

**User**

main.py에 적절한 정보를 전달하면 이메일을 전송해주는 기능을 구현했어.
이제 이 기능을 GUI를 통해서 입력을 쉽게 할 수 있도록 만들려고 해.
어떻게 계획을 세워서 코드를 작성하면 좋을까?
계획을 plan_GUI.md에 작성해줘.

---

**Cursor**

GUI 계획을 `plan_GUI.md`에 작성해드리겠습니다.

```python


```markdown
# Gmail 전송 프로그램 GUI 개발 계획

## 1. 필요한 라이브러리
- `tkinter`: 기본 GUI 라이브러리
- `tkinter.ttk`: 현대적인 GUI 위젯
- `tkinter.filedialog`: 파일 선택 다이얼로그
- `tkinter.messagebox`: 메시지 박스

## 2. 주요 기능
1. 이메일 작성 화면
   - 수신자 이메일 주소 입력 (다중 입력 지원)
   - 제목 입력
   - 본문 입력 (일반 텍스트/HTML 형식 선택)
   - 첨부 파일 추가/삭제
   - 전송 버튼

2. 설정 화면
   - Gmail 계정 정보 설정
   - 환경 변수 관리
   - 기본 설정 저장/로드

3. 사용자 편의 기능
   - 이메일 주소 자동 완성
   - HTML 편집기 (간단한 서식 지원)
   - 첨부 파일 미리보기
   - 전송 이력 관리

## 3. 화면 구성
1. 메인 화면
   ```
   +----------------------------------+
   |  수신자: [이메일 주소 입력]      |
   |  제목: [제목 입력]               |
   |  +------------------------------+|
   |  |                            ||
   |  |      본문 입력 영역        ||
   |  |                            ||
   |  +------------------------------+|
   |  첨부 파일: [파일1] [파일2] [추가]|
   |  [HTML 형식] [전송] [설정]        |
   +----------------------------------+
   ```

2. 설정 화면
   ```
   +----------------------------------+
   |  Gmail 계정 설정                 |
   |  이메일: [계정 입력]             |
   |  앱 비밀번호: [비밀번호 입력]    |
   |                                  |
   |  기본 설정                       |
   |  [ ] HTML 형식 기본 사용         |
   |  [ ] 전송 완료 알림              |
   |                                  |
   |  [저장] [취소]                   |
   +----------------------------------+
   ```

## 4. 구현 단계
1. 기본 GUI 구현
   - 메인 윈도우 생성
   - 기본 위젯 배치
   - 이벤트 핸들러 연결

2. 이메일 작성 기능 구현
   - 수신자 입력 필드
   - 제목 입력 필드
   - 본문 입력 영역
   - 첨부 파일 관리

3. 설정 기능 구현
   - 계정 정보 관리
   - 환경 변수 처리
   - 설정 저장/로드

4. 추가 기능 구현
   - HTML 편집기
   - 파일 첨부 관리
   - 전송 이력 관리

## 5. 파일 구조
```
send_gmail/
├── src/
│   ├── gui/
│   │   ├── __init__.py
│   │   ├── main_window.py    # 메인 윈도우
│   │   ├── email_form.py     # 이메일 작성 폼
│   │   ├── settings.py       # 설정 화면
│   │   └── widgets.py        # 커스텀 위젯
│   └── ...
├── resources/
│   ├── icons/               # 아이콘 파일들
│   └── styles/              # 스타일 정의
└── main_gui.py             # GUI 프로그램 진입점
```

## 6. 사용자 경험 개선
1. 입력 검증
   - 이메일 주소 형식 검사
   - 필수 입력 항목 확인
   - 첨부 파일 존재 확인

2. 피드백 제공
   - 전송 진행 상태 표시
   - 오류 메시지 표시
   - 성공/실패 알림

3. 단축키 지원
   - Ctrl+S: 전송
   - Ctrl+A: 첨부 파일 추가
   - Ctrl+H: HTML 형식 전환

## 7. 테스트 계획
1. GUI 테스트
   - 위젯 동작 테스트
   - 이벤트 처리 테스트
   - 레이아웃 테스트

2. 통합 테스트
   - 이메일 전송 기능 연동
   - 설정 저장/로드
   - 오류 처리
```

GUI 개발 계획을 작성했습니다. 주요 내용을 설명드리면:

1. **기술 스택**:
   - `tkinter`를 기본 GUI 라이브러리로 사용
   - 현대적인 UI를 위한 `ttk` 위젯 활용
   - 파일 선택과 메시지 표시를 위한 추가 모듈 사용

2. **주요 기능**:
   - 이메일 작성 화면 (수신자, 제목, 본문, 첨부 파일)
   - 설정 화면 (Gmail 계정 정보 관리)
   - 사용자 편의 기능 (자동 완성, HTML 편집기 등)

3. **화면 구성**:
   - 메인 화면: 이메일 작성에 필요한 모든 요소 포함
   - 설정 화면: 계정 정보와 기본 설정 관리

4. **구현 단계**:
   - 기본 GUI 구현
   - 이메일 작성 기능
   - 설정 기능
   - 추가 기능

5. **파일 구조**:
   - `src/gui/` 디렉토리에 GUI 관련 코드 모듈화
   - 리소스 파일 분리
   - 메인 진입점 분리

6. **사용자 경험**:
   - 입력 검증
   - 피드백 제공
   - 단축키 지원

7. **테스트 계획**:
   - GUI 테스트
   - 통합 테스트

이 계획을 바탕으로 구현을 시작하시겠습니까? 어떤 부분부터 구현하면 좋을지 말씀해 주시면 도와드리겠습니다.

---

**User**

@__init__.py @email_form.py @main_window.py @settings.py @widgets.py @gui 계획된 대로 코드 작성해봐.

---

**Cursor**

각 파일의 코드를 순차적으로 작성해드리겠습니다.

1. `src/gui/__init__.py`:
```python
"""
GUI 모듈 초기화 파일
"""
from .main_window import MainWindow
from .email_form import EmailForm
from .settings import SettingsWindow
from .widgets import EmailEntry, FileList

__all__ = ['MainWindow', 'EmailForm', 'SettingsWindow', 'EmailEntry', 'FileList']
```

2. `src/gui/widgets.py`:
```python
"""
커스텀 위젯 모듈
"""
import tkinter as tk
from tkinter import ttk
from typing import List, Callable
import re

class EmailEntry(ttk.Entry):
    """이메일 주소 입력을 위한 커스텀 위젯"""
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self._emails: List[str] = []
        self.bind('<Return>', self._add_email)
        self.bind('<FocusOut>', self._add_email)
        
    def _add_email(self, event=None):
        """이메일 주소 추가"""
        email = self.get().strip()
        if email and self._validate_email(email):
            if email not in self._emails:
                self._emails.append(email)
                self.delete(0, tk.END)
                
    def _validate_email(self, email: str) -> bool:
        """이메일 주소 유효성 검사"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    def get_emails(self) -> List[str]:
        """저장된 이메일 주소 목록 반환"""
        return self._emails.copy()
    
    def clear(self):
        """입력 필드 초기화"""
        self._emails.clear()
        self.delete(0, tk.END)

class FileList(ttk.Frame):
    """첨부 파일 목록을 표시하는 커스텀 위젯"""
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self._files: List[str] = []
        self._create_widgets()
        
    def _create_widgets(self):
        """위젯 생성"""
        self.listbox = tk.Listbox(self, height=3)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        button_frame = ttk.Frame(self)
        button_frame.pack(side=tk.RIGHT, fill=tk.Y)
        
        ttk.Button(button_frame, text="추가", command=self._add_file).pack(fill=tk.X)
        ttk.Button(button_frame, text="삭제", command=self._remove_file).pack(fill=tk.X)
        
    def _add_file(self):
        """파일 추가"""
        from tkinter import filedialog
        files = filedialog.askopenfilenames()
        for file in files:
            if file not in self._files:
                self._files.append(file)
                self.listbox.insert(tk.END, file)
                
    def _remove_file(self):
        """선택된 파일 삭제"""
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            self._files.pop(index)
            self.listbox.delete(index)
            
    def get_files(self) -> List[str]:
        """첨부 파일 목록 반환"""
        return self._files.copy()
    
    def clear(self):
        """파일 목록 초기화"""
        self._files.clear()
        self.listbox.delete(0, tk.END)
```

3. `src/gui/email_form.py`:
```python
"""
이메일 작성 폼 모듈
"""
import tkinter as tk
from tkinter import ttk
from typing import Callable, Optional
from .widgets import EmailEntry, FileList

class EmailForm(ttk.Frame):
    """이메일 작성 폼"""
    def __init__(self, master, on_send: Optional[Callable] = None, **kwargs):
        super().__init__(master, **kwargs)
        self.on_send = on_send
        self._create_widgets()
        
    def _create_widgets(self):
        """위젯 생성"""
        # 수신자 입력
        ttk.Label(self, text="수신자:").pack(anchor=tk.W)
        self.to_entry = EmailEntry(self)
        self.to_entry.pack(fill=tk.X, pady=(0, 10))
        
        # 제목 입력
        ttk.Label(self, text="제목:").pack(anchor=tk.W)
        self.subject_entry = ttk.Entry(self)
        self.subject_entry.pack(fill=tk.X, pady=(0, 10))
        
        # 본문 입력
        ttk.Label(self, text="본문:").pack(anchor=tk.W)
        self.body_text = tk.Text(self, height=10)
        self.body_text.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # 첨부 파일
        ttk.Label(self, text="첨부 파일:").pack(anchor=tk.W)
        self.file_list = FileList(self)
        self.file_list.pack(fill=tk.X, pady=(0, 10))
        
        # 버튼 프레임
        button_frame = ttk.Frame(self)
        button_frame.pack(fill=tk.X)
        
        # HTML 형식 체크박스
        self.html_var = tk.BooleanVar()
        ttk.Checkbutton(
            button_frame, 
            text="HTML 형식", 
            variable=self.html_var
        ).pack(side=tk.LEFT)
        
        # 전송 버튼
        ttk.Button(
            button_frame,
            text="전송",
            command=self._on_send
        ).pack(side=tk.RIGHT)
        
    def _on_send(self):
        """전송 버튼 클릭 처리"""
        if self.on_send:
            self.on_send(
                to_emails=self.to_entry.get_emails(),
                subject=self.subject_entry.get(),
                body=self.body_text.get("1.0", tk.END),
                is_html=self.html_var.get(),
                attachments=self.file_list.get_files()
            )
            
    def clear(self):
        """폼 초기화"""
        self.to_entry.clear()
        self.subject_entry.delete(0, tk.END)
        self.body_text.delete("1.0", tk.END)
        self.file_list.clear()
        self.html_var.set(False)
```

4. `src/gui/settings.py`:
```python
"""
설정 창 모듈
"""
import tkinter as tk
from tkinter import ttk
import os
from dotenv import load_dotenv

class SettingsWindow(tk.Toplevel):
    """설정 창"""
    def __init__(self, master):
        super().__init__(master)
        self.title("설정")
        self.geometry("400x300")
        
        # 환경 변수 로드
        load_dotenv()
        
        self._create_widgets()
        self._load_settings()
        
    def _create_widgets(self):
        """위젯 생성"""
        # Gmail 계정 설정
        account_frame = ttk.LabelFrame(self, text="Gmail 계정 설정")
        account_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Label(account_frame, text="이메일:").pack(anchor=tk.W)
        self.email_entry = ttk.Entry(account_frame)
        self.email_entry.pack(fill=tk.X, pady=(0, 5))
        
        ttk.Label(account_frame, text="앱 비밀번호:").pack(anchor=tk.W)
        self.password_entry = ttk.Entry(account_frame, show="*")
        self.password_entry.pack(fill=tk.X)
        
        # 기본 설정
        default_frame = ttk.LabelFrame(self, text="기본 설정")
        default_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.html_var = tk.BooleanVar()
        ttk.Checkbutton(
            default_frame,
            text="HTML 형식 기본 사용",
            variable=self.html_var
        ).pack(anchor=tk.W)
        
        self.notify_var = tk.BooleanVar()
        ttk.Checkbutton(
            default_frame,
            text="전송 완료 알림",
            variable=self.notify_var
        ).pack(anchor=tk.W)
        
        # 버튼
        button_frame = ttk.Frame(self)
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Button(
            button_frame,
            text="저장",
            command=self._save_settings
        ).pack(side=tk.RIGHT, padx=5)
        
        ttk.Button(
            button_frame,
            text="취소",
            command=self.destroy
        ).pack(side=tk.RIGHT)
        
    def _load_settings(self):
        """설정 로드"""
        self.email_entry.insert(0, os.getenv('GMAIL_USER', ''))
        self.password_entry.insert(0, os.getenv('GMAIL_PASSWORD', ''))
        self.html_var.set(False)
        self.notify_var.set(True)
        
    def _save_settings(self):
        """설정 저장"""
        # .env 파일에 설정 저장
        with open('.env', 'w') as f:
            f.write(f"GMAIL_USER={self.email_entry.get()}\n")
            f.write(f"GMAIL_PASSWORD={self.password_entry.get()}\n")
        
        self.destroy()
```

5. `src/gui/main_window.py`:
```python
"""
메인 윈도우 모듈
"""
import tkinter as tk
from tkinter import ttk, messagebox
from .email_form import EmailForm
from .settings import SettingsWindow
from ..email_sender import EmailSender
from ..config import EmailConfig

class MainWindow(tk.Tk):
    """메인 윈도우"""
    def __init__(self):
        super().__init__()
        
        self.title("Gmail 전송 프로그램")
        self.geometry("600x500")
        
        self._create_widgets()
        self._setup_menu()
        
    def _create_widgets(self):
        """위젯 생성"""
        # 이메일 폼
        self.email_form = EmailForm(self, on_send=self._send_email)
        self.email_form.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
    def _setup_menu(self):
        """메뉴 설정"""
        menubar = tk.Menu(self)
        
        # 파일 메뉴
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="설정", command=self._show_settings)
        file_menu.add_separator()
        file_menu.add_command(label="종료", command=self.quit)
        menubar.add_cascade(label="파일", menu=file_menu)
        
        # 도움말 메뉴
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="사용 방법", command=self._show_help)
        help_menu.add_command(label="정보", command=self._show_about)
        menubar.add_cascade(label="도움말", menu=help_menu)
        
        self.config(menu=menubar)
        
    def _send_email(self, **kwargs):
        """이메일 전송"""
        try:
            config = EmailConfig()
            sender = EmailSender(config)
            
            result = sender.send_email(**kwargs)
            
            if result:
                messagebox.showinfo("성공", "이메일이 성공적으로 전송되었습니다.")
                self.email_form.clear()
            else:
                messagebox.showerror("오류", "이메일 전송에 실패했습니다.")
                
        except Exception as e:
            messagebox.showerror("오류", str(e))
            
    def _show_settings(self):
        """설정 창 표시"""
        SettingsWindow(self)
        
    def _show_help(self):
        """도움말 표시"""
        messagebox.showinfo(
            "사용 방법",
            "1. 수신자 이메일 주소를 입력하세요.\n"
            "2. 제목과 본문을 작성하세요.\n"
            "3. 필요한 경우 파일을 첨부하세요.\n"
            "4. 전송 버튼을 클릭하세요."
        )
        
    def _show_about(self):
        """정보 표시"""
        messagebox.showinfo(
            "정보",
            "Gmail 전송 프로그램 v1.0\n"
            "이메일 전송을 위한 GUI 프로그램입니다."
        )
```

이제 `main_gui.py` 파일을 생성하여 프로그램을 실행할 수 있도록 하겠습니다:

```python
"""
GUI 프로그램 진입점
"""
from src.gui.main_window import MainWindow

def main():
    app = MainWindow()
    app.mainloop()

if __name__ == "__main__":
    main()
```

이 코드는 다음과 같은 기능을 제공합니다:

1. **이메일 작성**:
   - 수신자 이메일 주소 입력 (다중 입력 지원)
   - 제목과 본문 입력
   - HTML 형식 지원
   - 첨부 파일 관리

2. **설정 관리**:
   - Gmail 계정 정보 설정
   - 기본 설정 저장/로드

3. **사용자 인터페이스**:
   - 직관적인 레이아웃
   - 메뉴 시스템
   - 도움말 및 정보

4. **오류 처리**:
   - 입력 검증
   - 오류 메시지 표시
   - 전송 결과 알림

프로그램을 실행하려면:
```bash
python main_gui.py
```

이제 GUI를 통해 이메일을 쉽게 작성하고 전송할 수 있습니다. 필요한 경우 추가 기능이나 수정사항을 말씀해 주시면 도와드리겠습니다.

```python
"""
GUI 모듈 초기화 파일
"""
from .main_window import MainWindow
from .email_form import EmailForm
from .settings import SettingsWindow
from .widgets import EmailEntry, FileList

__all__ = ['MainWindow', 'EmailForm', 'SettingsWindow', 'EmailEntry', 'FileList']
```

```python
"""
커스텀 위젯 모듈
"""
import tkinter as tk
from tkinter import ttk
from typing import List, Callable
import re

class EmailEntry(ttk.Entry):
    """이메일 주소 입력을 위한 커스텀 위젯"""
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self._emails: List[str] = []
        self.bind('<Return>', self._add_email)
        self.bind('<FocusOut>', self._add_email)
        
    def _add_email(self, event=None):
        """이메일 주소 추가"""
        email = self.get().strip()
        if email and self._validate_email(email):
            if email not in self._emails:
                self._emails.append(email)
                self.delete(0, tk.END)
                
    def _validate_email(self, email: str) -> bool:
        """이메일 주소 유효성 검사"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    def get_emails(self) -> List[str]:
        """저장된 이메일 주소 목록 반환"""
        return self._emails.copy()
    
    def clear(self):
        """입력 필드 초기화"""
        self._emails.clear()
        self.delete(0, tk.END)

class FileList(ttk.Frame):
    """첨부 파일 목록을 표시하는 커스텀 위젯"""
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self._files: List[str] = []
        self._create_widgets()
        
    def _create_widgets(self):
        """위젯 생성"""
        self.listbox = tk.Listbox(self, height=3)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        button_frame = ttk.Frame(self)
        button_frame.pack(side=tk.RIGHT, fill=tk.Y)
        
        ttk.Button(button_frame, text="추가", command=self._add_file).pack(fill=tk.X)
        ttk.Button(button_frame, text="삭제", command=self._remove_file).pack(fill=tk.X)
        
    def _add_file(self):
        """파일 추가"""
        from tkinter import filedialog
        files = filedialog.askopenfilenames()
        for file in files:
            if file not in self._files:
                self._files.append(file)
                self.listbox.insert(tk.END, file)
                
    def _remove_file(self):
        """선택된 파일 삭제"""
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            self._files.pop(index)
            self.listbox.delete(index)
            
    def get_files(self) -> List[str]:
        """첨부 파일 목록 반환"""
        return self._files.copy()
    
    def clear(self):
        """파일 목록 초기화"""
        self._files.clear()
        self.listbox.delete(0, tk.END)
```

```python
"""
이메일 작성 폼 모듈
"""
import tkinter as tk
from tkinter import ttk
from typing import Callable, Optional
from .widgets import EmailEntry, FileList

class EmailForm(ttk.Frame):
    """이메일 작성 폼"""
    def __init__(self, master, on_send: Optional[Callable] = None, **kwargs):
        super().__init__(master, **kwargs)
        self.on_send = on_send
        self._create_widgets()
        
    def _create_widgets(self):
        """위젯 생성"""
        # 수신자 입력
        ttk.Label(self, text="수신자:").pack(anchor=tk.W)
        self.to_entry = EmailEntry(self)
        self.to_entry.pack(fill=tk.X, pady=(0, 10))
        
        # 제목 입력
        ttk.Label(self, text="제목:").pack(anchor=tk.W)
        self.subject_entry = ttk.Entry(self)
        self.subject_entry.pack(fill=tk.X, pady=(0, 10))
        
        # 본문 입력
        ttk.Label(self, text="본문:").pack(anchor=tk.W)
        self.body_text = tk.Text(self, height=10)
        self.body_text.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # 첨부 파일
        ttk.Label(self, text="첨부 파일:").pack(anchor=tk.W)
        self.file_list = FileList(self)
        self.file_list.pack(fill=tk.X, pady=(0, 10))
        
        # 버튼 프레임
        button_frame = ttk.Frame(self)
        button_frame.pack(fill=tk.X)
        
        # HTML 형식 체크박스
        self.html_var = tk.BooleanVar()
        ttk.Checkbutton(
            button_frame, 
            text="HTML 형식", 
            variable=self.html_var
        ).pack(side=tk.LEFT)
        
        # 전송 버튼
        ttk.Button(
            button_frame,
            text="전송",
            command=self._on_send
        ).pack(side=tk.RIGHT)
        
    def _on_send(self):
        """전송 버튼 클릭 처리"""
        if self.on_send:
            self.on_send(
                to_emails=self.to_entry.get_emails(),
                subject=self.subject_entry.get(),
                body=self.body_text.get("1.0", tk.END),
                is_html=self.html_var.get(),
                attachments=self.file_list.get_files()
            )
            
    def clear(self):
        """폼 초기화"""
        self.to_entry.clear()
        self.subject_entry.delete(0, tk.END)
        self.body_text.delete("1.0", tk.END)
        self.file_list.clear()
        self.html_var.set(False)
```

```python
"""
설정 창 모듈
"""
import tkinter as tk
from tkinter import ttk
import os
from dotenv import load_dotenv

class SettingsWindow(tk.Toplevel):
    """설정 창"""
    def __init__(self, master):
        super().__init__(master)
        self.title("설정")
        self.geometry("400x300")
        
        # 환경 변수 로드
        load_dotenv()
        
        self._create_widgets()
        self._load_settings()
        
    def _create_widgets(self):
        """위젯 생성"""
        # Gmail 계정 설정
        account_frame = ttk.LabelFrame(self, text="Gmail 계정 설정")
        account_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Label(account_frame, text="이메일:").pack(anchor=tk.W)
        self.email_entry = ttk.Entry(account_frame)
        self.email_entry.pack(fill=tk.X, pady=(0, 5))
        
        ttk.Label(account_frame, text="앱 비밀번호:").pack(anchor=tk.W)
        self.password_entry = ttk.Entry(account_frame, show="*")
        self.password_entry.pack(fill=tk.X)
        
        # 기본 설정
        default_frame = ttk.LabelFrame(self, text="기본 설정")
        default_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.html_var = tk.BooleanVar()
        ttk.Checkbutton(
            default_frame,
            text="HTML 형식 기본 사용",
            variable=self.html_var
        ).pack(anchor=tk.W)
        
        self.notify_var = tk.BooleanVar()
        ttk.Checkbutton(
            default_frame,
            text="전송 완료 알림",
            variable=self.notify_var
        ).pack(anchor=tk.W)
        
        # 버튼
        button_frame = ttk.Frame(self)
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Button(
            button_frame,
            text="저장",
            command=self._save_settings
        ).pack(side=tk.RIGHT, padx=5)
        
        ttk.Button(
            button_frame,
            text="취소",
            command=self.destroy
        ).pack(side=tk.RIGHT)
        
    def _load_settings(self):
        """설정 로드"""
        self.email_entry.insert(0, os.getenv('GMAIL_USER', ''))
        self.password_entry.insert(0, os.getenv('GMAIL_PASSWORD', ''))
        self.html_var.set(False)
        self.notify_var.set(True)
        
    def _save_settings(self):
        """설정 저장"""
        # .env 파일에 설정 저장
        with open('.env', 'w') as f:
            f.write(f"GMAIL_USER={self.email_entry.get()}\n")
            f.write(f"GMAIL_PASSWORD={self.password_entry.get()}\n")
        
        self.destroy()
```

```python
"""
메인 윈도우 모듈
"""
import tkinter as tk
from tkinter import ttk, messagebox
from .email_form import EmailForm
from .settings import SettingsWindow
from ..email_sender import EmailSender
from ..config import EmailConfig

class MainWindow(tk.Tk):
    """메인 윈도우"""
    def __init__(self):
        super().__init__()
        
        self.title("Gmail 전송 프로그램")
        self.geometry("600x500")
        
        self._create_widgets()
        self._setup_menu()
        
    def _create_widgets(self):
        """위젯 생성"""
        # 이메일 폼
        self.email_form = EmailForm(self, on_send=self._send_email)
        self.email_form.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
    def _setup_menu(self):
        """메뉴 설정"""
        menubar = tk.Menu(self)
        
        # 파일 메뉴
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="설정", command=self._show_settings)
        file_menu.add_separator()
        file_menu.add_command(label="종료", command=self.quit)
        menubar.add_cascade(label="파일", menu=file_menu)
        
        # 도움말 메뉴
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="사용 방법", command=self._show_help)
        help_menu.add_command(label="정보", command=self._show_about)
        menubar.add_cascade(label="도움말", menu=help_menu)
        
        self.config(menu=menubar)
        
    def _send_email(self, **kwargs):
        """이메일 전송"""
        try:
            config = EmailConfig()
            sender = EmailSender(config)
            
            result = sender.send_email(**kwargs)
            
            if result:
                messagebox.showinfo("성공", "이메일이 성공적으로 전송되었습니다.")
                self.email_form.clear()
            else:
                messagebox.showerror("오류", "이메일 전송에 실패했습니다.")
                
        except Exception as e:
            messagebox.showerror("오류", str(e))
            
    def _show_settings(self):
        """설정 창 표시"""
        SettingsWindow(self)
        
    def _show_help(self):
        """도움말 표시"""
        messagebox.showinfo(
            "사용 방법",
            "1. 수신자 이메일 주소를 입력하세요.\n"
            "2. 제목과 본문을 작성하세요.\n"
            "3. 필요한 경우 파일을 첨부하세요.\n"
            "4. 전송 버튼을 클릭하세요."
        )
        
    def _show_about(self):
        """정보 표시"""
        messagebox.showinfo(
            "정보",
            "Gmail 전송 프로그램 v1.0\n"
            "이메일 전송을 위한 GUI 프로그램입니다."
        )
```

```python
"""
GUI 프로그램 진입점
"""
from src.gui.main_window import MainWindow

def main():
    app = MainWindow()
    app.mainloop()

if __name__ == "__main__":
    main()
```

```shellscript
python main_gui.py
```

---

**User**

readme.md에 이 프로젝트를 클론 받은 사람들이 가상환경을 세팅하고 코드를 실행해볼 수 있도록 프로젝트에 대한 설명과 함께 안내문을 작성하고 싶어.
uv를 활용한 설치 방법을 추가하여 내용을 작성해줄래?

---

**Cursor**

`README.md` 파일을 작성해드리겠습니다.

```python


```markdown
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
git clone https://github.com/yourusername/send_gmail.git
cd send_gmail
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
```

#### uv를 사용하는 경우:

```bash
# uv 설치 (아직 설치하지 않은 경우)
pip install uv

# 가상환경 생성 및 패키지 설치
uv venv
uv pip install -r requirements.txt

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

프로젝트 루트 디렉토리에 `.env` 파일을 생성하고 다음 내용을 입력합니다:

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
```

README.md 파일을 작성했습니다. 주요 내용은 다음과 같습니다:

1. **프로젝트 소개**:
   - 프로그램의 주요 기능 설명
   - 사전 요구사항 안내

2. **설치 방법**:
   - 저장소 클론 방법
   - pip와 uv를 사용한 가상환경 설정 및 패키지 설치 방법
   - Gmail 계정 설정 방법
   - 환경 변수 설정 방법

3. **사용 방법**:
   - 프로그램 실행 방법
   - 이메일 작성 및 전송 과정
   - 설정 방법

4. **프로젝트 구조**:
   - 디렉토리 및 파일 구조 설명
   - 각 파일의 역할 설명

5. **추가 정보**:
   - 테스트 실행 방법
   - 라이선스 정보
   - 기여 방법
   - 문제 해결 가이드

특히 uv를 사용한 설치 방법을 추가하여, 더 빠른 패키지 설치와 의존성 관리를 지원하도록 했습니다. 필요한 경우 내용을 수정하거나 추가할 수 있습니다.

---

**User**

@pyproject.toml 의 내용을 이전에 작성한 파일들을 읽고 내용을 작성해줘.
설명(description) 부분도 대략적으로 작성해줘.

---

**Cursor**

`pyproject.toml` 파일을 프로젝트에 맞게 수정하겠습니다.

```python


```plaintext
[project]
name = "gmail-sender"
version = "0.1.0"
description = "Gmail을 통해 이메일을 전송할 수 있는 GUI 프로그램. 이메일 작성, 첨부 파일 관리, HTML 형식 지원 등 다양한 기능을 제공합니다."
readme = "README.md"
requires-python = ">=3.8"
license = {text = "MIT"}
authors = [
    {name = "dev-jsLee", email = "miraclelee0613@gmail.com"}
]
dependencies = [
    "python-dotenv>=1.0.0",
    "email-validator>=2.1.0.post1",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "black>=23.0.0",
    "isort>=5.0.0",
    "mypy>=1.0.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.black]
line-length = 88
target-version = ["py38"]

[tool.isort]
profile = "black"
multi_line_output = 3

[tool.mypy]
python_version = "3.8"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
```

`pyproject.toml` 파일을 다음과 같이 수정했습니다:

1. **기본 프로젝트 정보**:
   - 프로젝트 이름을 `gmail-sender`로 변경
   - 상세한 설명 추가
   - Python 버전 요구사항을 3.8로 설정
   - MIT 라이선스 추가
   - 작성자 정보 추가

2. **의존성 관리**:
   - `requirements.txt`에 있는 패키지들을 의존성으로 추가
   - 개발용 의존성 그룹 추가 (pytest, black, isort, mypy)

3. **빌드 시스템**:
   - `hatchling`을 빌드 백엔드로 설정

4. **개발 도구 설정**:
   - `black`: 코드 포맷팅 설정
   - `isort`: import 정렬 설정
   - `mypy`: 타입 체크 설정

이제 이 프로젝트는 다음과 같은 기능을 지원합니다:
- 패키지 관리 및 배포
- 코드 품질 관리 (포맷팅, 정렬, 타입 체크)
- 테스트 실행
- 개발 환경 설정

개발 의존성을 설치하려면 다음 명령어를 사용할 수 있습니다:
```bash
pip install -e ".[dev]"
```

```shellscript
`pyproject.toml` 파일을 다음과 같이 수정했습니다:

1. **기본 프로젝트 정보**:
   - 프로젝트 이름을 `gmail-sender`로 변경
   - 상세한 설명 추가
   - Python 버전 요구사항을 3.8로 설정
   - MIT 라이선스 추가
   - 작성자 정보 추가

2. **의존성 관리**:
   - `requirements.txt`에 있는 패키지들을 의존성으로 추가
   - 개발용 의존성 그룹 추가 (pytest, black, isort, mypy)

3. **빌드 시스템**:
   - `hatchling`을 빌드 백엔드로 설정

4. **개발 도구 설정**:
   - `black`: 코드 포맷팅 설정
   - `isort`: import 정렬 설정
   - `mypy`: 타입 체크 설정

이제 이 프로젝트는 다음과 같은 기능을 지원합니다:
- 패키지 관리 및 배포
- 코드 품질 관리 (포맷팅, 정렬, 타입 체크)
- 테스트 실행
- 개발 환경 설정

개발 의존성을 설치하려면 다음 명령어를 사용할 수 있습니다:
```bash
pip install -e ".[dev]"tall -e ".[dev]"
```

---

**User**

3.12 버전 이상의 파이썬을 요구하려고 해.
그러면 30번째줄에 있는 내용도 바뀌어야 할까?

---

**Cursor**

네, Python 3.12 버전을 요구사항으로 설정했으므로, 개발 도구 설정도 이에 맞게 수정하는 것이 좋습니다. `pyproject.toml` 파일을 수정하겠습니다.

```python


```plaintext
[project]
name = "gmail-sender"
version = "0.1.0"
description = "Gmail을 통해 이메일을 전송할 수 있는 GUI 프로그램. 이메일 작성, 첨부 파일 관리, HTML 형식 지원 등 다양한 기능을 제공합니다."
readme = "README.md"
requires-python = ">=3.12"
license = {text = "MIT"}
authors = [
    {name = "dev-jsLee", email = "jslee7518@gmail.com"}
]
dependencies = [
    "python-dotenv>=1.0.0",
    "email-validator>=2.1.0.post1",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "black>=23.0.0",
    "isort>=5.0.0",
    "mypy>=1.0.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.black]
line-length = 88
target-version = ["py312"]

[tool.isort]
profile = "black"
multi_line_output = 3

[tool.mypy]
python_version = "3.12"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
```

다음과 같이 수정했습니다:

1. `[tool.black]` 섹션:
   - `target-version`을 `["py312"]`로 변경하여 Python 3.12 문법에 맞게 코드 포맷팅

2. `[tool.mypy]` 섹션:
   - `python_version`을 `"3.12"`로 변경하여 Python 3.12 타입 체크 지원

이렇게 수정함으로써:
- 코드 포맷팅이 Python 3.12 문법에 맞게 적용됩니다.
- 타입 체크가 Python 3.12의 타입 시스템을 기준으로 수행됩니다.
- 개발 도구들이 Python 3.12의 새로운 기능들을 지원하게 됩니다.

이 변경으로 프로젝트의 모든 부분이 Python 3.12 버전을 일관되게 지원하게 됩니다.

---

**User**

해당 위치의 내용이 무슨 내용인지 주석을 달 수 있을까?

---

**Cursor**

네, `pyproject.toml` 파일에 각 섹션에 대한 설명을 주석으로 추가하겠습니다.

```python


```plaintext
[project]
name = "gmail-sender"
version = "0.1.0"
description = "Gmail을 통해 이메일을 전송할 수 있는 GUI 프로그램. 이메일 작성, 첨부 파일 관리, HTML 형식 지원 등 다양한 기능을 제공합니다."
readme = "README.md"
requires-python = ">=3.12"
license = {text = "MIT"}
authors = [
    {name = "dev-jsLee", email = "jslee7518@gmail.com"}
]
dependencies = [
    "python-dotenv>=1.0.0",
    "email-validator>=2.1.0.post1",
]

# 개발 시에만 필요한 추가 패키지들
[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",    # 테스트 실행을 위한 프레임워크
    "black>=23.0.0",    # 코드 포맷팅 도구
    "isort>=5.0.0",     # import 문 정렬 도구
    "mypy>=1.0.0",      # 정적 타입 검사 도구
]

# 패키지 빌드 시스템 설정
[build-system]
requires = ["hatchling"]  # 빌드에 필요한 도구
build-backend = "hatchling.build"  # 빌드 백엔드 지정

# Black 코드 포맷터 설정
[tool.black]
line-length = 88        # 한 줄의 최대 길이
target-version = ["py312"]  # Python 3.12 문법 사용

# isort import 정렬 도구 설정
[tool.isort]
profile = "black"       # black 포맷터와 호환되는 설정 사용
multi_line_output = 3   # 여러 줄의 import 정렬 방식

# mypy 타입 체크 도구 설정
[tool.mypy]
python_version = "3.12"  # Python 3.12 타입 시스템 사용
warn_return_any = true   # Any 타입 반환 시 경고
warn_unused_configs = true  # 사용되지 않은 설정 경고
disallow_untyped_defs = true  # 타입 힌트가 없는 함수 정의 금지
```

각 섹션에 대한 설명을 주석으로 추가했습니다:

1. `[project.optional-dependencies]`: 개발 시에만 필요한 추가 패키지들을 정의하는 섹션입니다.
2. `[build-system]`: 패키지 빌드 시스템 설정을 정의하는 섹션입니다.
3. `[tool.black]`: Black 코드 포맷터의 설정을 정의하는 섹션입니다.
4. `[tool.isort]`: isort import 정렬 도구의 설정을 정의하는 섹션입니다.
5. `[tool.mypy]`: mypy 타입 체크 도구의 설정을 정의하는 섹션입니다.

각 설정 값에 대한 설명도 주석으로 추가하여 설정의 목적을 명확히 했습니다. 이렇게 하면 다른 개발자들이 설정 파일을 이해하고 수정하기 더 쉬워질 것입니다.

---

**User**

이제 exe파일로 만들어서 독립실행형 프로그램을 만들려고 해. 어떤 라이브러리를 활용해서 독립실행형 프로그램으로 만들어야 할까?

---

**Cursor**

Python 프로그램을 독립 실행형 EXE 파일로 만들기 위해 PyInstaller를 사용하는 것을 추천드립니다. PyInstaller는 가장 널리 사용되는 Python 패키징 도구 중 하나이며, 다음과 같은 장점이 있습니다:

1. 단일 EXE 파일 생성 가능
2. 의존성 자동 포함
3. Windows, macOS, Linux 모두 지원
4. 사용이 간단함

먼저 PyInstaller를 개발 의존성에 추가하겠습니다:

```python


```plaintext
[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",    # 테스트 실행을 위한 프레임워크
    "black>=23.0.0",    # 코드 포맷팅 도구
    "isort>=5.0.0",     # import 문 정렬 도구
    "mypy>=1.0.0",      # 정적 타입 검사 도구
    "pyinstaller>=6.3.0",  # EXE 파일 생성 도구
]
// ... existing code ...
```

이제 EXE 파일을 생성하기 위한 스크립트를 만들어보겠습니다:

```python


```python
"""
EXE 파일 생성을 위한 빌드 스크립트
"""
import os
import shutil
import subprocess
from pathlib import Path

def build_exe():
    # 빌드 디렉토리 생성
    build_dir = Path("build")
    dist_dir = Path("dist")
    
    # 기존 빌드 디렉토리 정리
    if build_dir.exists():
        shutil.rmtree(build_dir)
    if dist_dir.exists():
        shutil.rmtree(dist_dir)
    
    # PyInstaller 명령어 구성
    cmd = [
        "pyinstaller",
        "--name=gmail_sender",  # 실행 파일 이름
        "--onefile",  # 단일 EXE 파일로 생성
        "--windowed",  # GUI 모드로 실행
        "--icon=resources/icon.ico",  # 아이콘 파일 (필요시 추가)
        "--add-data=.env;.",  # 환경 변수 파일 포함
        "main_gui.py"  # 메인 스크립트
    ]
    
    # PyInstaller 실행
    subprocess.run(cmd, check=True)
    
    print("빌드가 완료되었습니다.")
    print(f"실행 파일 위치: {dist_dir / 'gmail_sender.exe'}")

if __name__ == "__main__":
    build_exe()
```

EXE 파일을 생성하기 위한 단계별 가이드를 제공해드리겠습니다:

1. **개발 의존성 설치**
```bash
pip install -e ".[dev]"
```

2. **아이콘 파일 준비** (선택사항)
- `resources` 디렉토리에 `icon.ico` 파일을 추가하세요.
- 아이콘이 없는 경우 `--icon` 옵션을 제거하거나 주석 처리하세요.

3. **EXE 파일 생성**
```bash
python build.py
```

4. **생성된 파일 확인**
- `dist` 디렉토리에 `gmail_sender.exe` 파일이 생성됩니다.
- 이 파일은 다른 컴퓨터에서도 Python이 설치되어 있지 않아도 실행 가능합니다.

주의사항:
1. `.env` 파일은 EXE 파일에 포함되지만, 보안을 위해 실제 배포 시에는 제외하는 것이 좋습니다.
2. 첫 실행 시 Windows Defender나 다른 백신이 경고를 표시할 수 있습니다.
3. 생성된 EXE 파일의 크기가 큰 것은 정상입니다 (모든 의존성이 포함되기 때문).

추가로 필요한 작업이 있다면 말씀해 주세요!

```shellscript
이제 EXE 파일을 생성하기 위한 스크립트를 만들어보겠습니다:

```python
EXE 파일을 생성하기 위한 단계별 가이드를 제공해드리겠습니다:

1. **개발 의존성 설치**
```bash
pip install -e ".[dev]"
```

2. **아이콘 파일 준비** (선택사항)
- `resources` 디렉토리에 `icon.ico` 파일을 추가하세요.
- 아이콘이 없는 경우 `--icon` 옵션을 제거하거나 주석 처리하세요.

3. **EXE 파일 생성**
```bash
python build.py
```

4. **생성된 파일 확인**
- `dist` 디렉토리에 `gmail_sender.exe` 파일이 생성됩니다.
- 이 파일은 다른 컴퓨터에서도 Python이 설치되어 있지 않아도 실행 가능합니다.

주의사항:
1. `.env` 파일은 EXE 파일에 포함되지만, 보안을 위해 실제 배포 시에는 제외하는 것이 좋습니다.
2. 첫 실행 시 Windows Defender나 다른 백신이 경고를 표시할 수 있습니다.
3. 생성된 EXE 파일의 크기가 큰 것은 정상입니다 (모든 의존성이 포함되기 때문).

추가로 필요한 작업이 있다면 말씀해 주세요!
```

```shellscript
python build.py
```

---

**User**

pyinstaller 라이브러리를 설치하려고 하는데 오류가 발생했어.

---

**Cursor**

오류 메시지를 보니 `hatchling` 빌드 시스템과 관련된 문제가 발생했네요. `pyproject.toml` 파일에 빌드 설정을 추가해야 할 것 같습니다. 다음과 같이 수정해보겠습니다:

```python


```plaintext
[project]
name = "gmail-sender"
version = "0.1.0"
description = "Gmail을 통해 이메일을 전송할 수 있는 GUI 프로그램. 이메일 작성, 첨부 파일 관리, HTML 형식 지원 등 다양한 기능을 제공합니다."
readme = "README.md"
requires-python = ">=3.12"
license = {text = "MIT"}
authors = [
    {name = "dev-jsLee", email = "jslee7518@gmail.com"}
]
dependencies = [
    "python-dotenv>=1.0.0",
    "email-validator>=2.1.0.post1",
]

# 개발 시에만 필요한 추가 패키지들
[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",    # 테스트 실행을 위한 프레임워크
    "black>=23.0.0",    # 코드 포맷팅 도구
    "isort>=5.0.0",     # import 문 정렬 도구
    "mypy>=1.0.0",      # 정적 타입 검사 도구
    "pyinstaller>=6.3.0",  # EXE 파일 생성 도구
]

# 패키지 빌드 시스템 설정
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

# hatchling 빌드 설정
[tool.hatch.build.targets.wheel]
packages = ["src"]

[tool.hatch.build.targets.sdist]
include = [
    "src",
    "tests",
    "README.md",
    "requirements.txt",
    "pyproject.toml",
]

# Black 코드 포맷터 설정
[tool.black]
line-length = 88        # 한 줄의 최대 길이
target-version = ["py312"]  # Python 3.12 문법 사용

# isort import 정렬 도구 설정
[tool.isort]
profile = "black"       # black 포맷터와 호환되는 설정 사용
multi_line_output = 3   # 여러 줄의 import 정렬 방식

# mypy 타입 체크 도구 설정
[tool.mypy]
python_version = "3.12"  # Python 3.12 타입 시스템 사용
warn_return_any = true   # Any 타입 반환 시 경고
warn_unused_configs = true  # 사용되지 않은 설정 경고
disallow_untyped_defs = true  # 타입 힌트가 없는 함수 정의 금지
```

이제 다음 단계를 따라 PyInstaller를 설치하고 EXE 파일을 생성해보세요:

1. **가상환경 활성화** (이미 활성화되어 있다면 건너뛰세요)
```bash
.venv\Scripts\activate
```

2. **개발 의존성 설치**
```bash
pip install -e ".[dev]"
```

3. **EXE 파일 생성**
```bash
python build.py
```

만약 여전히 오류가 발생한다면, 다음과 같은 대체 방법을 시도해볼 수 있습니다:

1. **직접 PyInstaller 설치**
```bash
pip install pyinstaller
```

2. **requirements.txt에 PyInstaller 추가**
```bash
echo "pyinstaller>=6.3.0" >> requirements.txt
pip install -r requirements.txt
```

3. **PyInstaller 직접 실행**
```bash
pyinstaller --name=gmail_sender --onefile --windowed --add-data=.env;. main_gui.py
```

어떤 방법을 시도해보시겠습니까? 오류가 계속되면 구체적인 오류 메시지를 공유해주시면 더 자세한 도움을 드릴 수 있습니다.

```shellscript
이제 다음 단계를 따라 PyInstaller를 설치하고 EXE 파일을 생성해보세요:

1. **가상환경 활성화** (이미 활성화되어 있다면 건너뛰세요)
```bash
.venv\Scripts\activate
```

2. **개발 의존성 설치**
```bash
pip install -e ".[dev]"
```

3. **EXE 파일 생성**
```bash
python build.py
```

만약 여전히 오류가 발생한다면, 다음과 같은 대체 방법을 시도해볼 수 있습니다:

1. **직접 PyInstaller 설치**
```bash
pip install pyinstaller
```

2. **requirements.txt에 PyInstaller 추가**
```bash
echo "pyinstaller>=6.3.0" >> requirements.txt
pip install -r requirements.txt
```

3. **PyInstaller 직접 실행**
```bash
pyinstaller --name=gmail_sender --onefile --windowed --add-data=.env;. main_gui.py
```

어떤 방법을 시도해보시겠습니까? 오류가 계속되면 구체적인 오류 메시지를 공유해주시면 더 자세한 도움을 드릴 수 있습니다.
```

```shellscript
pip install -e ".[dev]"
```

```shellscript
python build.py
```

```shellscript
pip install pyinstaller
```

```shellscript
echo "pyinstaller>=6.3.0" >> requirements.txt
pip install -r requirements.txt
```

```shellscript
pyinstaller --name=gmail_sender --onefile --windowed --add-data=.env;. main_gui.py
```

---

**User**

버전 정보를 동적으로 가져와서 파일명에 기재하고 싶어.

---

**Cursor**

`pyproject.toml`에서 버전 정보를 가져와서 EXE 파일 이름에 포함시키도록 `build.py`를 수정하겠습니다:

```python


```python
"""
EXE 파일 생성을 위한 빌드 스크립트
"""
# build.py 파일은 프로그램을 빌드하는 스크립트입니다.
# 프로그램을 빌드하려면 터미널에서 다음 명령어를 실행하세요:
# python build.py
# 빌드 후에는 dist 디렉토리에 실행 파일이 생성됩니다.
import os
import shutil
import subprocess
import tomli
from pathlib import Path

def get_version():
    """pyproject.toml에서 버전 정보를 가져옵니다."""
    with open("pyproject.toml", "rb") as f:
        pyproject = tomli.load(f)
    return pyproject["project"]["version"]

def build_exe():
    # 버전 정보 가져오기
    version = get_version()
    
    # 빌드 디렉토리 생성
    build_dir = Path("build")
    dist_dir = Path("dist")
    
    # 기존 빌드 디렉토리 정리
    if build_dir.exists():
        shutil.rmtree(build_dir)
    if dist_dir.exists():
        shutil.rmtree(dist_dir)
    
    # PyInstaller 명령어 구성
    cmd = [
        "pyinstaller",
        f"--name=gmail_sender_{version}",  # 실행 파일 이름
        "--onefile",  # 단일 EXE 파일로 생성
        "--windowed",  # GUI 모드로 실행
        # "--icon=resources/icon.ico",  # 아이콘 파일 (필요시 추가)
        "--add-data=.env;.",  # 환경 변수 파일 포함
        "main_gui.py"  # 메인 스크립트
    ]
    
    # PyInstaller 실행
    subprocess.run(cmd, check=True)
    
    print("빌드가 완료되었습니다.")
    print(f"실행 파일 위치: {dist_dir / f'gmail_sender_{version}.exe'}")

if __name__ == "__main__":
    build_exe()
```

이제 `tomli` 패키지를 설치해야 합니다. 이 패키지는 TOML 파일을 파싱하는데 사용됩니다:

```python


```plaintext
[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",    # 테스트 실행을 위한 프레임워크
    "black>=23.0.0",    # 코드 포맷팅 도구
    "isort>=5.0.0",     # import 문 정렬 도구
    "mypy>=1.0.0",      # 정적 타입 검사 도구
    "pyinstaller>=6.3.0",  # EXE 파일 생성 도구
    "tomli>=2.0.0",     # TOML 파일 파싱 도구
]
// ... existing code ...
```

이제 다음 단계를 따라 실행해보세요:

1. **개발 의존성 업데이트**
```bash
pip install -e ".[dev]"
```

2. **EXE 파일 생성**
```bash
python build.py
```

이렇게 하면 `pyproject.toml`에 정의된 버전 정보가 EXE 파일 이름에 자동으로 포함됩니다. 예를 들어, 버전이 "0.1.0"이라면 생성되는 파일 이름은 `gmail_sender_0.1.0.exe`가 됩니다.

버전을 변경하고 싶을 때는 `pyproject.toml`의 `version` 필드만 수정하면 됩니다. 이렇게 하면 버전 관리가 더 체계적으로 이루어질 수 있습니다.

```shellscript
이제 `tomli` 패키지를 설치해야 합니다. 이 패키지는 TOML 파일을 파싱하는데 사용됩니다:

```python
이제 다음 단계를 따라 실행해보세요:

1. **개발 의존성 업데이트**
```bash
pip install -e ".[dev]"
```

2. **EXE 파일 생성**
```bash
python build.py
```

이렇게 하면 `pyproject.toml`에 정의된 버전 정보가 EXE 파일 이름에 자동으로 포함됩니다. 예를 들어, 버전이 "0.1.0"이라면 생성되는 파일 이름은 `gmail_sender_0.1.0.exe`가 됩니다.

버전을 변경하고 싶을 때는 `pyproject.toml`의 `version` 필드만 수정하면 됩니다. 이렇게 하면 버전 관리가 더 체계적으로 이루어질 수 있습니다.
```

```shellscript
python build.py
```

---

**User**

@uv.lock 이 파일을 github에 올리는 게 맞을까? 아니면 gitigniore에 작성해서 제외하는 게 맞을까?

---

**Cursor**

`uv.lock` 파일은 `package-lock.json`이나 `poetry.lock`과 유사한 역할을 하는 의존성 잠금 파일입니다. 이 파일을 GitHub에 올릴지 말지는 다음과 같은 관점에서 결정할 수 있습니다:

1. **올리는 것이 좋은 경우**:
   - 팀 프로젝트에서 모든 개발자가 동일한 패키지 버전을 사용하도록 보장
   - 빌드의 재현성(reproducibility) 보장
   - CI/CD 파이프라인에서 일관된 환경 구성 가능

2. **제외하는 것이 좋은 경우**:
   - 개인 프로젝트이고 다른 개발자와 공유하지 않는 경우
   - 패키지 버전이 자주 변경되는 경우
   - 저장소 크기를 최소화하고 싶은 경우

현재 프로젝트의 경우, 다음과 같이 `.gitignore`에 추가하는 것을 추천드립니다:

```python


---

**User**

@gui 폴더에 있는 파일 중, 받는 이메일 목록을 추가하는 부분이 어느 파일이야?

---

**Cursor**

이메일 수신자 목록을 관리하는 부분은 `email_form.py` 파일에 있을 것 같습니다. 해당 파일의 내용을 확인해보겠습니다:



네, 이메일 수신자 목록을 관리하는 부분은 `email_form.py` 파일에 있습니다. 구체적으로:

1. 수신자 입력 필드는 `EmailEntry` 위젯을 사용하고 있으며, 이는 `widgets.py`에 정의되어 있습니다.
2. 실제 이메일 주소 입력과 검증은 `widgets.py`의 `EmailEntry` 클래스에서 처리됩니다.

`widgets.py` 파일도 확인해보겠습니다:


이메일 수신자 목록 관리와 관련된 주요 기능은 다음과 같습니다:

1. `EmailEntry` 클래스 (`widgets.py`):
   - 이메일 주소 입력 필드 제공
   - 이메일 주소 유효성 검사 (`_validate_email` 메서드)
   - 여러 이메일 주소 저장 (`_emails` 리스트)
   - Enter 키나 포커스 아웃 시 이메일 추가
   - 저장된 이메일 목록 반환 (`get_emails` 메서드)

2. `EmailForm` 클래스 (`email_form.py`):
   - `EmailEntry` 위젯을 사용하여 수신자 입력 UI 구성
   - 전송 시 저장된 이메일 목록을 가져와서 처리

이메일 주소를 추가하는 방법:
1. 입력 필드에 이메일 주소 입력
2. Enter 키를 누르거나 다른 곳을 클릭하면 자동으로 추가
3. 유효한 이메일 주소만 저장됨 (정규식으로 검증)
4. 중복된 이메일 주소는 자동으로 제외됨

---

**User**

@email_form.py 그러면 추가된 받는 이메일을 제거하거나 목록을 확인하는 기능을 넣고 싶은데, 어떻게 하면 좋을까?

---

**Cursor**

`EmailEntry` 클래스에 이메일 목록을 표시하고 제거할 수 있는 기능을 추가하겠습니다. `widgets.py`를 수정하여 이메일 목록을 보여주는 리스트박스와 제거 버튼을 추가하겠습니다:

```python


```python
class EmailEntry(ttk.Frame):
    """이메일 주소 입력을 위한 커스텀 위젯"""
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self._emails: List[str] = []
        self._create_widgets()
        
    def _create_widgets(self):
        """위젯 생성"""
        # 이메일 입력 필드
        self.entry = ttk.Entry(self)
        self.entry.pack(fill=tk.X, pady=(0, 5))
        self.entry.bind('<Return>', self._add_email)
        self.entry.bind('<FocusOut>', self._add_email)
        
        # 이메일 목록 프레임
        list_frame = ttk.Frame(self)
        list_frame.pack(fill=tk.BOTH, expand=True)
        
        # 이메일 목록
        self.listbox = tk.Listbox(list_frame, height=4)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # 스크롤바
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.configure(yscrollcommand=scrollbar.set)
        
        # 버튼 프레임
        button_frame = ttk.Frame(self)
        button_frame.pack(fill=tk.X, pady=(5, 0))
        
        # 제거 버튼
        ttk.Button(
            button_frame,
            text="선택 제거",
            command=self._remove_email
        ).pack(side=tk.LEFT)
        
        # 전체 제거 버튼
        ttk.Button(
            button_frame,
            text="전체 제거",
            command=self.clear
        ).pack(side=tk.RIGHT)
        
    def _add_email(self, event=None):
        """이메일 주소 추가"""
        email = self.entry.get().strip()
        if email and self._validate_email(email):
            if email not in self._emails:
                self._emails.append(email)
                self.listbox.insert(tk.END, email)
                self.entry.delete(0, tk.END)
                
    def _remove_email(self):
        """선택된 이메일 주소 제거"""
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            self._emails.pop(index)
            self.listbox.delete(index)
    
    def _validate_email(self, email: str) -> bool:
        """이메일 주소 유효성 검사"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    def get_emails(self) -> List[str]:
        """저장된 이메일 주소 목록 반환"""
        return self._emails.copy()
    
    def clear(self):
        """입력 필드 초기화"""
        self._emails.clear()
        self.entry.delete(0, tk.END)
        self.listbox.delete(0, tk.END)
// ... existing code ...
```

주요 변경사항은 다음과 같습니다:

1. `EmailEntry` 클래스를 `ttk.Entry`에서 `ttk.Frame`으로 변경하여 여러 위젯을 포함할 수 있도록 했습니다.

2. 새로운 기능 추가:
   - 이메일 목록을 보여주는 리스트박스
   - 스크롤바 (긴 목록을 스크롤할 수 있음)
   - "선택 제거" 버튼 (선택한 이메일만 제거)
   - "전체 제거" 버튼 (모든 이메일 제거)

3. 사용 방법:
   - 이메일 주소를 입력하고 Enter 키를 누르거나 다른 곳을 클릭하면 목록에 추가됩니다.
   - 목록에서 이메일을 선택하고 "선택 제거" 버튼을 클릭하면 해당 이메일이 제거됩니다.
   - "전체 제거" 버튼을 클릭하면 모든 이메일이 제거됩니다.

이제 이메일 주소를 더 쉽게 관리할 수 있으며, 현재 추가된 이메일 목록을 한눈에 볼 수 있습니다. 이메일 주소의 유효성 검사와 중복 체크 기능도 그대로 유지됩니다.

---

**User**

@gui 이메일을 추가하는 인풋박스와 이메일 목록을 보여주는 리스트를 좌우로 나란히 배치하면 좋을 것 같아. 그리고 리스트 아래에 선택 제거, 전체 제거를 놓는 게 어떨까?

---

**Cursor**

네, 좋은 제안입니다. `EmailEntry` 클래스의 레이아웃을 수정하여 입력 필드와 리스트를 좌우로 배치하고, 버튼들을 리스트 아래에 배치하도록 하겠습니다:

```python


```python
class EmailEntry(ttk.Frame):
    """이메일 주소 입력을 위한 커스텀 위젯"""
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self._emails: List[str] = []
        self._create_widgets()
        
    def _create_widgets(self):
        """위젯 생성"""
        # 메인 프레임 (입력 필드와 리스트를 좌우로 배치)
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # 왼쪽: 이메일 입력 프레임
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        # 이메일 입력 필드
        self.entry = ttk.Entry(input_frame)
        self.entry.pack(fill=tk.X)
        self.entry.bind('<Return>', self._add_email)
        self.entry.bind('<FocusOut>', self._add_email)
        
        # 입력 안내 레이블
        ttk.Label(
            input_frame,
            text="Enter 키를 누르거나\n다른 곳을 클릭하면\n이메일이 추가됩니다",
            justify=tk.LEFT,
            wraplength=150
        ).pack(fill=tk.X, pady=(5, 0))
        
        # 오른쪽: 이메일 목록 프레임
        list_frame = ttk.Frame(main_frame)
        list_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # 이메일 목록
        self.listbox = tk.Listbox(list_frame, height=6)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # 스크롤바
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.configure(yscrollcommand=scrollbar.set)
        
        # 버튼 프레임 (리스트 아래에 배치)
        button_frame = ttk.Frame(self)
        button_frame.pack(fill=tk.X, pady=(5, 0))
        
        # 제거 버튼
        ttk.Button(
            button_frame,
            text="선택 제거",
            command=self._remove_email
        ).pack(side=tk.LEFT)
        
        # 전체 제거 버튼
        ttk.Button(
            button_frame,
            text="전체 제거",
            command=self.clear
        ).pack(side=tk.RIGHT)
        
    def _add_email(self, event=None):
        """이메일 주소 추가"""
        email = self.entry.get().strip()
        if email and self._validate_email(email):
            if email not in self._emails:
                self._emails.append(email)
                self.listbox.insert(tk.END, email)
                self.entry.delete(0, tk.END)
                
    def _remove_email(self):
        """선택된 이메일 주소 제거"""
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            self._emails.pop(index)
            self.listbox.delete(index)
    
    def _validate_email(self, email: str) -> bool:
        """이메일 주소 유효성 검사"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    def get_emails(self) -> List[str]:
        """저장된 이메일 주소 목록 반환"""
        return self._emails.copy()
    
    def clear(self):
        """입력 필드 초기화"""
        self._emails.clear()
        self.entry.delete(0, tk.END)
        self.listbox.delete(0, tk.END)
// ... existing code ...
```

주요 변경사항은 다음과 같습니다:

1. 레이아웃 구조 변경:
   - 메인 프레임을 만들어 입력 필드와 리스트를 좌우로 배치
   - 입력 필드와 안내 텍스트를 왼쪽에 배치
   - 이메일 목록과 스크롤바를 오른쪽에 배치
   - 버튼들을 리스트 아래에 배치

2. UI 개선:
   - 입력 필드 아래에 사용 안내 텍스트 추가
   - 리스트의 높이를 6으로 증가하여 더 많은 이메일을 한 번에 표시
   - 입력 프레임과 리스트 프레임 사이에 여백 추가 (padx)

3. 사용성 개선:
   - 입력 방법에 대한 안내 텍스트 추가
   - 좌우 배치로 공간 활용도 향상
   - 버튼 위치를 리스트 아래로 이동하여 직관적인 사용성 제공

이제 이메일 입력과 목록 관리가 더 직관적이고 사용하기 쉬워졌습니다. 입력 필드에서 이메일을 입력하고 Enter를 누르면 바로 오른쪽의 리스트에 추가되며, 리스트 아래의 버튼으로 쉽게 관리할 수 있습니다.

---

**User**

선택제거 버튼도 리스트 아래로 보내줘.

---

**Cursor**

네, 선택 제거 버튼도 리스트 아래로 이동시키겠습니다:

```python


```python
class EmailEntry(ttk.Frame):
    """이메일 주소 입력을 위한 커스텀 위젯"""
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self._emails: List[str] = []
        self._create_widgets()
        
    def _create_widgets(self):
        """위젯 생성"""
        # 메인 프레임 (입력 필드와 리스트를 좌우로 배치)
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # 왼쪽: 이메일 입력 프레임
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        # 이메일 입력 필드
        self.entry = ttk.Entry(input_frame)
        self.entry.pack(fill=tk.X)
        self.entry.bind('<Return>', self._add_email)
        self.entry.bind('<FocusOut>', self._add_email)
        
        # 입력 안내 레이블
        ttk.Label(
            input_frame,
            text="Enter 키를 누르거나\n다른 곳을 클릭하면\n이메일이 추가됩니다",
            justify=tk.LEFT,
            wraplength=150
        ).pack(fill=tk.X, pady=(5, 0))
        
        # 오른쪽: 이메일 목록 프레임
        list_frame = ttk.Frame(main_frame)
        list_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # 이메일 목록
        self.listbox = tk.Listbox(list_frame, height=6)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # 스크롤바
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.configure(yscrollcommand=scrollbar.set)
        
        # 버튼 프레임 (리스트 아래에 배치)
        button_frame = ttk.Frame(list_frame)
        button_frame.pack(fill=tk.X, pady=(5, 0))
        
        # 제거 버튼
        ttk.Button(
            button_frame,
            text="선택 제거",
            command=self._remove_email
        ).pack(side=tk.LEFT)
        
        # 전체 제거 버튼
        ttk.Button(
            button_frame,
            text="전체 제거",
            command=self.clear
        ).pack(side=tk.RIGHT)
// ... existing code ...
```

주요 변경사항:
1. 버튼 프레임의 부모를 `self`(전체 프레임)에서 `list_frame`(리스트 프레임)으로 변경했습니다.
2. 이제 버튼들이 리스트 바로 아래에 위치하게 됩니다.

이렇게 하면 버튼들이 리스트와 더 가깝게 위치하여 사용성이 향상됩니다. 선택 제거와 전체 제거 버튼이 리스트 바로 아래에 있어 직관적으로 사용할 수 있습니다.

---

**User**

이메일 목록과 제거버튼들을 하나의 프레임 안에 넣고 리스트 아래에 좌우로 제거 버튼이 위치하도록 설정해줘.

---

**Cursor**

네, 이메일 목록과 제거 버튼들을 하나의 프레임으로 묶고, 버튼들을 리스트 아래에 좌우로 배치하도록 수정하겠습니다:

```python


```python
class EmailEntry(ttk.Frame):
    """이메일 주소 입력을 위한 커스텀 위젯"""
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self._emails: List[str] = []
        self._create_widgets()
        
    def _create_widgets(self):
        """위젯 생성"""
        # 메인 프레임 (입력 필드와 리스트를 좌우로 배치)
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # 왼쪽: 이메일 입력 프레임
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        # 이메일 입력 필드
        self.entry = ttk.Entry(input_frame)
        self.entry.pack(fill=tk.X)
        self.entry.bind('<Return>', self._add_email)
        self.entry.bind('<FocusOut>', self._add_email)
        
        # 입력 안내 레이블
        ttk.Label(
            input_frame,
            text="Enter 키를 누르거나\n다른 곳을 클릭하면\n이메일이 추가됩니다",
            justify=tk.LEFT,
            wraplength=150
        ).pack(fill=tk.X, pady=(5, 0))
        
        # 오른쪽: 이메일 목록과 버튼을 포함하는 프레임
        list_container = ttk.Frame(main_frame)
        list_container.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # 이메일 목록 프레임
        list_frame = ttk.Frame(list_container)
        list_frame.pack(fill=tk.BOTH, expand=True)
        
        # 이메일 목록
        self.listbox = tk.Listbox(list_frame, height=6)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # 스크롤바
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.configure(yscrollcommand=scrollbar.set)
        
        # 버튼 프레임 (리스트 아래에 배치)
        button_frame = ttk.Frame(list_container)
        button_frame.pack(fill=tk.X, pady=(5, 0))
        
        # 제거 버튼
        ttk.Button(
            button_frame,
            text="선택 제거",
            command=self._remove_email
        ).pack(side=tk.LEFT)
        
        # 전체 제거 버튼
        ttk.Button(
            button_frame,
            text="전체 제거",
            command=self.clear
        ).pack(side=tk.RIGHT)
// ... existing code ...
```

주요 변경사항:
1. 새로운 `list_container` 프레임을 추가하여 이메일 목록과 버튼들을 하나로 묶었습니다.
2. `list_frame`을 `list_container`의 자식으로 변경하여 이메일 목록을 포함하도록 했습니다.
3. `button_frame`의 부모를 `list_container`로 변경하여 버튼들이 리스트 아래에 위치하도록 했습니다.

이제 이메일 목록과 제거 버튼들이 하나의 프레임 안에 깔끔하게 정리되어 있으며, 버튼들은 리스트 아래에 좌우로 배치됩니다. 이렇게 하면 UI가 더 통일성 있고 사용하기 편리해집니다.

---

**User**

상단의 메뉴바의 파일 > 설정에 작성한 내용은 파일 형태로 저장이 될까?

---

**Cursor**

네, `settings.py` 파일을 확인해보겠습니다:

```python


현재 코드를 보면, 설정 내용은 `.env` 파일에 저장되도록 되어 있습니다. 하지만 몇 가지 개선이 필요해 보입니다:

1. 현재는 Gmail 계정 정보만 저장되고 있고, HTML 형식 사용 여부와 알림 설정은 저장되지 않습니다.
2. 설정 파일의 위치가 명확하지 않습니다.

설정을 더 체계적으로 관리하기 위해 코드를 수정하겠습니다:

```python


```python
"""
설정 창 모듈
"""
import tkinter as tk
from tkinter import ttk, messagebox
import os
import json
from pathlib import Path
from dotenv import load_dotenv

class SettingsWindow(tk.Toplevel):
    """설정 창"""
    def __init__(self, master):
        super().__init__(master)
        self.title("설정")
        self.geometry("400x300")
        
        # 설정 파일 경로
        self.settings_dir = Path.home() / '.gmail_sender'
        self.settings_file = self.settings_dir / 'settings.json'
        self.env_file = self.settings_dir / '.env'
        
        # 설정 디렉토리 생성
        self.settings_dir.mkdir(exist_ok=True)
        
        # 환경 변수 로드
        if self.env_file.exists():
            load_dotenv(self.env_file)
        
        self._create_widgets()
        self._load_settings()
        
    def _create_widgets(self):
        """위젯 생성"""
        # Gmail 계정 설정
        account_frame = ttk.LabelFrame(self, text="Gmail 계정 설정")
        account_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Label(account_frame, text="이메일:").pack(anchor=tk.W)
        self.email_entry = ttk.Entry(account_frame)
        self.email_entry.pack(fill=tk.X, pady=(0, 5))
        
        ttk.Label(account_frame, text="앱 비밀번호:").pack(anchor=tk.W)
        self.password_entry = ttk.Entry(account_frame, show="*")
        self.password_entry.pack(fill=tk.X)
        
        # 기본 설정
        default_frame = ttk.LabelFrame(self, text="기본 설정")
        default_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.html_var = tk.BooleanVar()
        ttk.Checkbutton(
            default_frame,
            text="HTML 형식 기본 사용",
            variable=self.html_var
        ).pack(anchor=tk.W)
        
        self.notify_var = tk.BooleanVar()
        ttk.Checkbutton(
            default_frame,
            text="전송 완료 알림",
            variable=self.notify_var
        ).pack(anchor=tk.W)
        
        # 버튼
        button_frame = ttk.Frame(self)
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Button(
            button_frame,
            text="저장",
            command=self._save_settings
        ).pack(side=tk.RIGHT, padx=5)
        
        ttk.Button(
            button_frame,
            text="취소",
            command=self.destroy
        ).pack(side=tk.RIGHT)
        
    def _load_settings(self):
        """설정 로드"""
        # 이메일과 비밀번호는 .env 파일에서 로드
        self.email_entry.insert(0, os.getenv('GMAIL_USER', ''))
        self.password_entry.insert(0, os.getenv('GMAIL_PASSWORD', ''))
        
        # 나머지 설정은 settings.json에서 로드
        if self.settings_file.exists():
            try:
                with open(self.settings_file, 'r', encoding='utf-8') as f:
                    settings = json.load(f)
                    self.html_var.set(settings.get('use_html', False))
                    self.notify_var.set(settings.get('show_notification', True))
            except Exception as e:
                print(f"설정 파일 로드 중 오류 발생: {e}")
                self.html_var.set(False)
                self.notify_var.set(True)
        else:
            self.html_var.set(False)
            self.notify_var.set(True)
        
    def _save_settings(self):
        """설정 저장"""
        try:
            # Gmail 계정 정보는 .env 파일에 저장
            with open(self.env_file, 'w', encoding='utf-8') as f:
                f.write(f"GMAIL_USER={self.email_entry.get()}\n")
                f.write(f"GMAIL_PASSWORD={self.password_entry.get()}\n")
            
            # 나머지 설정은 settings.json에 저장
            settings = {
                'use_html': self.html_var.get(),
                'show_notification': self.notify_var.get()
            }
            
            with open(self.settings_file, 'w', encoding='utf-8') as f:
                json.dump(settings, f, indent=4, ensure_ascii=False)
            
            messagebox.showinfo("알림", "설정이 저장되었습니다.")
            self.destroy()
            
        except Exception as e:
            messagebox.showerror("오류", f"설정 저장 중 오류가 발생했습니다: {e}")
// ... existing code ...
```

주요 변경사항:

1. 설정 파일 저장 위치 변경:
   - 사용자의 홈 디렉토리 아래에 `.gmail_sender` 폴더를 생성
   - Gmail 계정 정보는 `.env` 파일에 저장
   - 나머지 설정은 `settings.json` 파일에 저장

2. 설정 저장 기능 개선:
   - Gmail 계정 정보와 일반 설정을 분리하여 저장
   - JSON 형식으로 설정을 저장하여 확장성 향상
   - 파일 저장 시 인코딩을 UTF-8로 지정

3. 오류 처리 추가:
   - 설정 파일 로드/저장 시 발생할 수 있는 예외 처리
   - 사용자에게 적절한 알림 메시지 표시

4. 설정 로드 기능 개선:
   - 기존 설정이 있는 경우 자동으로 로드
   - 설정 파일이 없는 경우 기본값 사용

이제 설정 창에서 변경한 내용이 모두 파일로 저장되며, 프로그램을 다시 실행해도 이전 설정이 유지됩니다. 설정 파일은 사용자의 홈 디렉토리 아래 `.gmail_sender` 폴더에 저장됩니다.

---

**User**

메인 창 아래에 진행바(프로그레스 바)를 추가해서 여러 이메일에 전송하는 경우, 몇 퍼센트 진행되었는지 표시되도록 해줘.

---

**Cursor**

네, 메인 창에 진행바를 추가하고 이메일 전송 진행 상황을 표시하도록 수정하겠습니다. 먼저 `main_window.py` 파일을 확인해보겠습니다:

```python


이제 `main_window.py` 파일을 수정하여 진행바를 추가하고 이메일 전송 진행 상황을 표시하도록 하겠습니다:

```python


```python
"""
메인 윈도우 모듈
"""
import tkinter as tk
from tkinter import ttk, messagebox
from .email_form import EmailForm
from .settings import SettingsWindow
from ..email_sender import EmailSender
from ..config import EmailConfig

class MainWindow(tk.Tk):
    """메인 윈도우"""
    def __init__(self):
        super().__init__()
        
        self.title("Gmail 전송 프로그램")
        self.geometry("600x500")
        
        self._create_widgets()
        self._setup_menu()
        
    def _create_widgets(self):
        """위젯 생성"""
        # 메인 프레임
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # 이메일 폼
        self.email_form = EmailForm(main_frame, on_send=self._send_email)
        self.email_form.pack(fill=tk.BOTH, expand=True)
        
        # 진행 상태 프레임
        progress_frame = ttk.Frame(main_frame)
        progress_frame.pack(fill=tk.X, pady=(10, 0))
        
        # 진행 상태 레이블
        self.progress_label = ttk.Label(progress_frame, text="")
        self.progress_label.pack(side=tk.LEFT)
        
        # 진행바
        self.progress_bar = ttk.Progressbar(
            progress_frame,
            mode='determinate',
            length=300
        )
        self.progress_bar.pack(side=tk.LEFT, padx=(5, 0))
        
    def _setup_menu(self):
        """메뉴 설정"""
        menubar = tk.Menu(self)
        
        # 파일 메뉴
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="설정", command=self._show_settings)
        file_menu.add_separator()
        file_menu.add_command(label="종료", command=self.quit)
        menubar.add_cascade(label="파일", menu=file_menu)
        
        # 도움말 메뉴
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="사용 방법", command=self._show_help)
        help_menu.add_command(label="정보", command=self._show_about)
        menubar.add_cascade(label="도움말", menu=help_menu)
        
        self.config(menu=menubar)
        
    def _send_email(self, **kwargs):
        """이메일 전송"""
        try:
            config = EmailConfig()
            sender = EmailSender(config)
            
            # 수신자 목록 가져오기
            recipients = kwargs.get('to', [])
            total_recipients = len(recipients)
            
            if total_recipients == 0:
                messagebox.showwarning("경고", "수신자 이메일 주소를 입력해주세요.")
                return
            
            # 진행바 초기화
            self.progress_bar['value'] = 0
            self.progress_label['text'] = "이메일 전송 중..."
            self.update()
            
            # 각 수신자에게 이메일 전송
            success_count = 0
            for i, recipient in enumerate(recipients, 1):
                # 현재 수신자에게 이메일 전송
                kwargs['to'] = [recipient]  # 단일 수신자로 설정
                result = sender.send_email(**kwargs)
                
                if result:
                    success_count += 1
                
                # 진행 상태 업데이트
                progress = (i / total_recipients) * 100
                self.progress_bar['value'] = progress
                self.progress_label['text'] = f"전송 중... ({i}/{total_recipients})"
                self.update()
            
            # 전송 결과 표시
            if success_count == total_recipients:
                messagebox.showinfo("성공", f"모든 이메일이 성공적으로 전송되었습니다. ({success_count}/{total_recipients})")
                self.email_form.clear()
            else:
                messagebox.showwarning("경고", f"일부 이메일 전송에 실패했습니다. ({success_count}/{total_recipients})")
            
            # 진행바 초기화
            self.progress_bar['value'] = 0
            self.progress_label['text'] = ""
            
        except Exception as e:
            messagebox.showerror("오류", str(e))
            # 진행바 초기화
            self.progress_bar['value'] = 0
            self.progress_label['text'] = ""
            
    def _show_settings(self):
        """설정 창 표시"""
        SettingsWindow(self)
        
    def _show_help(self):
        """도움말 표시"""
        messagebox.showinfo(
            "사용 방법",
            "1. 수신자 이메일 주소를 입력하세요.\n"
            "2. 제목과 본문을 작성하세요.\n"
            "3. 필요한 경우 파일을 첨부하세요.\n"
            "4. 전송 버튼을 클릭하세요."
        )
        
    def _show_about(self):
        """정보 표시"""
        messagebox.showinfo(
            "정보",
            "Gmail 전송 프로그램 v1.0\n"
            "이메일 전송을 위한 GUI 프로그램입니다."
        )
```

주요 변경사항:

1. UI 변경:
   - 메인 프레임을 추가하여 이메일 폼과 진행 상태를 포함
   - 진행 상태를 표시할 레이블과 진행바 추가
   - 진행바는 0-100% 범위로 표시되며, 현재 진행 상황을 시각적으로 보여줌

2. 이메일 전송 로직 개선:
   - 수신자 목록을 가져와서 전체 수신자 수 계산
   - 각 수신자에게 개별적으로 이메일 전송
   - 전송 진행 상황을 실시간으로 업데이트
   - 성공/실패 횟수를 추적하여 최종 결과 표시

3. 진행 상태 표시:
   - 전송 시작 시 진행바 초기화
   - 각 이메일 전송마다 진행률 업데이트
   - 현재 전송 중인 이메일 번호와 전체 수신자 수 표시
   - 전송 완료 또는 오류 발생 시 진행바 초기화

4. 오류 처리 개선:
   - 수신자가 없는 경우 경고 메시지 표시
   - 일부 이메일 전송 실패 시 경고 메시지로 표시
   - 오류 발생 시 진행바 초기화

이제 여러 수신자에게 이메일을 전송할 때 진행 상황을 실시간으로 확인할 수 있으며, 전송 결과도 더 자세히 표시됩니다.

---

**User**

방금 내용을 추가하고 나니까 이메일 목록이 있어도 수신자 이메일을 추가해달라는 경고 메시지가 떠. 수정해줘.

---

**Cursor**

`email_form.py` 파일을 확인하여 이메일 목록을 가져오는 부분을 수정하겠습니다:

```python


문제를 확인했습니다. `main_window.py`의 `_send_email` 메서드에서 `kwargs.get('to', [])`로 수신자 목록을 가져오고 있는데, `email_form.py`에서는 `to_emails`라는 이름으로 전달하고 있습니다. 이를 수정하겠습니다:

```python


```python
    def _send_email(self, **kwargs):
        """이메일 전송"""
        try:
            config = EmailConfig()
            sender = EmailSender(config)
            
            # 수신자 목록 가져오기
            recipients = kwargs.get('to_emails', [])  # 'to' 대신 'to_emails' 사용
            total_recipients = len(recipients)
            
            if total_recipients == 0:
                messagebox.showwarning("경고", "수신자 이메일 주소를 입력해주세요.")
                return
            
            # 진행바 초기화
            self.progress_bar['value'] = 0
            self.progress_label['text'] = "이메일 전송 중..."
            self.update()
            
            # 각 수신자에게 이메일 전송
            success_count = 0
            for i, recipient in enumerate(recipients, 1):
                # 현재 수신자에게 이메일 전송
                kwargs['to'] = [recipient]  # 단일 수신자로 설정
                result = sender.send_email(**kwargs)
                
                if result:
                    success_count += 1
                
                # 진행 상태 업데이트
                progress = (i / total_recipients) * 100
                self.progress_bar['value'] = progress
                self.progress_label['text'] = f"전송 중... ({i}/{total_recipients})"
                self.update()
            
            # 전송 결과 표시
            if success_count == total_recipients:
                messagebox.showinfo("성공", f"모든 이메일이 성공적으로 전송되었습니다. ({success_count}/{total_recipients})")
                self.email_form.clear()
            else:
                messagebox.showwarning("경고", f"일부 이메일 전송에 실패했습니다. ({success_count}/{total_recipients})")
            
            # 진행바 초기화
            self.progress_bar['value'] = 0
            self.progress_label['text'] = ""
            
        except Exception as e:
            messagebox.showerror("오류", str(e))
            # 진행바 초기화
            self.progress_bar['value'] = 0
            self.progress_label['text'] = ""
```

주요 변경사항:
1. `kwargs.get('to', [])`를 `kwargs.get('to_emails', [])`로 변경하여 `email_form.py`에서 전달하는 수신자 목록의 키 이름과 일치시켰습니다.

이제 이메일 목록이 있을 때 올바르게 수신자 목록을 가져와서 처리할 수 있습니다. 경고 메시지는 이메일 목록이 실제로 비어있을 때만 표시될 것입니다.

