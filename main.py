"""
Gmail 이메일 전송 예제 프로그램
"""
# main.py 파일은 Gmail 이메일 전송 예제 프로그램입니다.
import os
from typing import List, Optional
from dotenv import load_dotenv
from src.email_sender import EmailSender
from src.config import EmailConfig

# send_email 함수는 이메일을 전송하는 함수입니다.
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

def test_email_sender():
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
    # test_email_sender()
    send_email(
        to_emails=["miraclelee0613@gmail.com"],
        subject="테스트 이메일",
        body="테스트 이메일입니다.",
        is_html=False
    )
