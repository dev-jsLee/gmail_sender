"""
Gmail 전송 모듈
이 모듈은 Gmail을 통해 이메일을 전송하는 기능을 제공합니다.
"""
# __init__.py 파일은 패키지의 초기화 파일입니다.
from .email_sender import EmailSender
from .config import EmailConfig

# 모듈 내부에서 사용할 모듈들을 명시적으로 내보내기
__all__ = ['EmailSender', 'EmailConfig']
