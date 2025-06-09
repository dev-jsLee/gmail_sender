"""
EmailSender 클래스에 대한 테스트
"""
# tests/test_email_sender.py 파일은 EmailSender 클래스에 대한 테스트 코드를 포함하는 파일입니다.
import unittest
from unittest.mock import patch, MagicMock
from src.email_sender import EmailSender
from src.config import EmailConfig
from src.utils import validate_email_address

class TestEmailSender(unittest.TestCase):
    def setUp(self):
        """테스트 전 환경 설정"""
        self.config = EmailConfig()
        self.config.username = 'jslee7518@gmail.com'
        self.config.password = 'irpz rucu vhhg dlji'
        self.sender = EmailSender(self.config)
        
        self.test_email = {
            'to_emails': ['miraclelee0613@gmail.com'],
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
