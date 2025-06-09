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
