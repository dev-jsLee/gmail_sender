"""
메인 윈도우 모듈
"""
import tkinter as tk
from tkinter import ttk, messagebox
from .email_form import EmailForm
from .settings import SettingsWindow
from ..email_sender import EmailSender
from ..config import EmailConfig

class MainWindow(tk.Tk):
    """메인 윈도우"""
    def __init__(self):
        super().__init__()
        
        self.title("Gmail 전송 프로그램")
        self.geometry("600x500")
        
        self._create_widgets()
        self._setup_menu()
        
    def _create_widgets(self):
        """위젯 생성"""
        # 메인 프레임
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # 이메일 폼
        self.email_form = EmailForm(main_frame, on_send=self._send_email)
        self.email_form.pack(fill=tk.BOTH, expand=True)
        
        # 진행 상태 프레임
        progress_frame = ttk.Frame(main_frame)
        progress_frame.pack(fill=tk.X, pady=(10, 0))
        
        # 진행 상태 레이블
        self.progress_label = ttk.Label(progress_frame, text="")
        self.progress_label.pack(side=tk.LEFT)
        
        # 진행바
        self.progress_bar = ttk.Progressbar(
            progress_frame,
            mode='determinate',
            length=300
        )
        self.progress_bar.pack(side=tk.LEFT, padx=(5, 0))
        
    def _setup_menu(self):
        """메뉴 설정"""
        menubar = tk.Menu(self)
        
        # 파일 메뉴
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="설정", command=self._show_settings)
        file_menu.add_separator()
        file_menu.add_command(label="종료", command=self.quit)
        menubar.add_cascade(label="파일", menu=file_menu)
        
        # 도움말 메뉴
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="사용 방법", command=self._show_help)
        help_menu.add_command(label="정보", command=self._show_about)
        menubar.add_cascade(label="도움말", menu=help_menu)
        
        self.config(menu=menubar)
        
    def _send_email(self, **kwargs):
        """이메일 전송"""
        try:
            config = EmailConfig()
            sender = EmailSender(config)
            
            # 수신자 목록 가져오기
            recipients = kwargs.get('to_emails', [])
            total_recipients = len(recipients)
            
            if total_recipients == 0:
                messagebox.showwarning("경고", "수신자 이메일 주소를 입력해주세요.")
                return
            
            # 진행바 초기화
            self.progress_bar['value'] = 0
            self.progress_label['text'] = "이메일 전송 중..."
            self.update()
            
            # 각 수신자에게 이메일 전송
            success_count = 0
            for i, recipient in enumerate(recipients, 1):
                # 현재 수신자에게 이메일 전송
                current_kwargs = kwargs.copy()
                current_kwargs['to_emails'] = [recipient]  # 'to' 대신 'to_emails' 사용
                result = sender.send_email(**current_kwargs)
                
                if result:
                    success_count += 1
                
                # 진행 상태 업데이트
                progress = (i / total_recipients) * 100
                self.progress_bar['value'] = progress
                self.progress_label['text'] = f"전송 중... ({i}/{total_recipients})"
                self.update()
            
            # 전송 결과 표시
            if success_count == total_recipients:
                messagebox.showinfo("성공", f"모든 이메일이 성공적으로 전송되었습니다. ({success_count}/{total_recipients})")
                self.email_form.clear()
            else:
                messagebox.showwarning("경고", f"일부 이메일 전송에 실패했습니다. ({success_count}/{total_recipients})")
            
            # 진행바 초기화
            self.progress_bar['value'] = 0
            self.progress_label['text'] = ""
            
        except Exception as e:
            messagebox.showerror("오류", str(e))
            # 진행바 초기화
            self.progress_bar['value'] = 0
            self.progress_label['text'] = ""
            
    def _show_settings(self):
        """설정 창 표시"""
        SettingsWindow(self)
        
    def _show_help(self):
        """도움말 표시"""
        messagebox.showinfo(
            "사용 방법",
            "1. 수신자 이메일 주소를 입력하세요.\n"
            "2. 제목과 본문을 작성하세요.\n"
            "3. 필요한 경우 파일을 첨부하세요.\n"
            "4. 전송 버튼을 클릭하세요."
        )
        
    def _show_about(self):
        """정보 표시"""
        messagebox.showinfo(
            "정보",
            "Gmail 전송 프로그램 v1.0\n"
            "이메일 전송을 위한 GUI 프로그램입니다."
        )
