"""
이메일 설정을 관리하는 모듈
"""
# config.py 파일은 이메일 설정을 관리하는 모듈입니다.
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
