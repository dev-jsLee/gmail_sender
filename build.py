"""
EXE 파일 생성을 위한 빌드 스크립트
"""
# build.py 파일은 프로그램을 빌드하는 스크립트입니다.
# 프로그램을 빌드하려면 터미널에서 다음 명령어를 실행하세요:
# python build.py
# 빌드 후에는 dist 디렉토리에 실행 파일이 생성됩니다.
import os
import shutil
import subprocess
import tomli
from pathlib import Path

def get_version():
    """pyproject.toml에서 버전 정보를 가져옵니다."""
    with open("pyproject.toml", "rb") as f:
        pyproject = tomli.load(f)
    return pyproject["project"]["version"]

def build_exe():
    # 버전 정보 가져오기
    version = get_version()
    
    # 빌드 디렉토리 생성
    build_dir = Path("build")
    dist_dir = Path("dist")
    
    # 기존 빌드 디렉토리 정리
    if build_dir.exists():
        shutil.rmtree(build_dir)
    if dist_dir.exists():
        shutil.rmtree(dist_dir)
    
    # PyInstaller 명령어 구성
    cmd = [
        "pyinstaller",
        f"--name=gmail_sender_v{version}",  # 실행 파일 이름
        "--onefile",  # 단일 EXE 파일로 생성
        "--windowed",  # GUI 모드로 실행
        # "--icon=resources/icon.ico",  # 아이콘 파일 (필요시 추가)
        "--add-data=.env;.",  # 환경 변수 파일 포함
        "main_gui.py"  # 메인 스크립트
    ]
    
    # PyInstaller 실행
    subprocess.run(cmd, check=True)
    
    print("빌드가 완료되었습니다.")
    print(f"실행 파일 위치: {dist_dir / f'gmail_sender_{version}.exe'}")

if __name__ == "__main__":
    build_exe() 