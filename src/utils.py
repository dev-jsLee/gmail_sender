"""
유틸리티 함수들을 제공하는 모듈
"""
# utils.py 파일은 유틸리티 함수들을 제공하는 모듈입니다.
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
