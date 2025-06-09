"""
Gmail 이메일 전송을 위한 핵심 모듈
"""
# email_sender.py 파일은 Gmail 이메일 전송을 위한 핵심 모듈입니다.
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import (
    List, 
    Optional
)
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
