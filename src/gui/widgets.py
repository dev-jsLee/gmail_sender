"""
커스텀 위젯 모듈
"""
import tkinter as tk
from tkinter import ttk
from typing import List, Callable
import re

class EmailEntry(ttk.Frame):
    """이메일 주소 입력을 위한 커스텀 위젯"""
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self._emails: List[str] = []
        self._create_widgets()
        
    def _create_widgets(self):
        """위젯 생성"""
        # 메인 프레임 (입력 필드와 리스트를 좌우로 배치)
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # 왼쪽: 이메일 입력 프레임
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        # 이메일 입력 필드
        self.entry = ttk.Entry(input_frame)
        self.entry.pack(fill=tk.X)
        self.entry.bind('<Return>', self._add_email)
        self.entry.bind('<FocusOut>', self._add_email)
        
        # 입력 안내 레이블
        ttk.Label(
            input_frame,
            text="Enter 키를 누르거나\n다른 곳을 클릭하면\n이메일이 추가됩니다",
            justify=tk.LEFT,
            wraplength=150
        ).pack(fill=tk.X, pady=(5, 0))
        
        # 오른쪽: 이메일 목록과 버튼을 포함하는 프레임
        list_container = ttk.Frame(main_frame)
        list_container.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # 이메일 목록 프레임
        list_frame = ttk.Frame(list_container)
        list_frame.pack(fill=tk.BOTH, expand=True)
        
        # 이메일 목록
        self.listbox = tk.Listbox(list_frame, height=6)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # 스크롤바
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.configure(yscrollcommand=scrollbar.set)
        
        # 버튼 프레임 (리스트 아래에 배치)
        button_frame = ttk.Frame(list_container)
        button_frame.pack(fill=tk.X, pady=(5, 0))
        
        # 제거 버튼
        ttk.Button(
            button_frame,
            text="선택 제거",
            command=self._remove_email
        ).pack(side=tk.LEFT)
        
        # 전체 제거 버튼
        ttk.Button(
            button_frame,
            text="전체 제거",
            command=self.clear
        ).pack(side=tk.RIGHT)
        
    def _add_email(self, event=None):
        """이메일 주소 추가"""
        email = self.entry.get().strip()
        if email and self._validate_email(email):
            if email not in self._emails:
                self._emails.append(email)
                self.listbox.insert(tk.END, email)
                self.entry.delete(0, tk.END)
                
    def _remove_email(self):
        """선택된 이메일 주소 제거"""
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            self._emails.pop(index)
            self.listbox.delete(index)
    
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
        self.entry.delete(0, tk.END)
        self.listbox.delete(0, tk.END)

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
