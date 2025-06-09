"""
커스텀 위젯 모듈
"""
import tkinter as tk
from tkinter import ttk
from typing import List, Callable
import re

class EmailEntry(ttk.Entry):
    """이메일 주소 입력을 위한 커스텀 위젯"""
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self._emails: List[str] = []
        self.bind('<Return>', self._add_email)
        self.bind('<FocusOut>', self._add_email)
        
    def _add_email(self, event=None):
        """이메일 주소 추가"""
        email = self.get().strip()
        if email and self._validate_email(email):
            if email not in self._emails:
                self._emails.append(email)
                self.delete(0, tk.END)
                
    def _validate_email(self, email: str) -> bool:
        """이메일 주소 유효성 검사"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    def get_emails(self) -> List[str]:
        """저장된 이메일 주소 목록 반환"""
        return self._emails.copy()
    
    def clear(self):
        """입력 필드 초기화"""
        self._emails.clear()
        self.delete(0, tk.END)

class FileList(ttk.Frame):
    """첨부 파일 목록을 표시하는 커스텀 위젯"""
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self._files: List[str] = []
        self._create_widgets()
        
    def _create_widgets(self):
        """위젯 생성"""
        self.listbox = tk.Listbox(self, height=3)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        button_frame = ttk.Frame(self)
        button_frame.pack(side=tk.RIGHT, fill=tk.Y)
        
        ttk.Button(button_frame, text="추가", command=self._add_file).pack(fill=tk.X)
        ttk.Button(button_frame, text="삭제", command=self._remove_file).pack(fill=tk.X)
        
    def _add_file(self):
        """파일 추가"""
        from tkinter import filedialog
        files = filedialog.askopenfilenames()
        for file in files:
            if file not in self._files:
                self._files.append(file)
                self.listbox.insert(tk.END, file)
                
    def _remove_file(self):
        """선택된 파일 삭제"""
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            self._files.pop(index)
            self.listbox.delete(index)
            
    def get_files(self) -> List[str]:
        """첨부 파일 목록 반환"""
        return self._files.copy()
    
    def clear(self):
        """파일 목록 초기화"""
        self._files.clear()
        self.listbox.delete(0, tk.END)
