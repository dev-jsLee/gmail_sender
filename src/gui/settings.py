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
