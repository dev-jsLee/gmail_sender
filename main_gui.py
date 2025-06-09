"""
GUI 프로그램 진입점
"""
from src.gui.main_window import MainWindow

def main():
    app = MainWindow()
    app.mainloop()

if __name__ == "__main__":
    main()
