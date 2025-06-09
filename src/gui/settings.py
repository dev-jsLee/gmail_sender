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
        print(self.settings_dir)
        
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
