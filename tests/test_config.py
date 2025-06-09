"""
EmailConfig 클래스에 대한 테스트
"""
# tests/test_config.py 파일은 EmailConfig 클래스에 대한 테스트 코드를 포함하는 파일입니다.
import os
import unittest
from unittest.mock import patch
from src.config import EmailConfig

class TestEmailConfig(unittest.TestCase):
    def setUp(self):
        """테스트 전 환경 설정"""
        self.test_env = {
            'GMAIL_USER': 'jslee7518@gmail.com',
            'GMAIL_PASSWORD': 'irpz rucu vhhg dlji'
        }
    
    def test_init_with_valid_env(self):
        """유효한 환경 변수로 초기화 테스트"""
        with patch.dict(os.environ, self.test_env):
            config = EmailConfig()
            self.assertEqual(config.username, 'jslee7518@gmail.com')
            self.assertEqual(config.password, 'irpz rucu vhhg dlji')
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
