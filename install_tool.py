import os
import sys
import subprocess
from pathlib import Path
import shutil
import zipfile




#  install_tool.py가 있는 디렉토리 기준으로 상대 경로 설정
script_dir = Path(__file__).resolve().parent
print(script_dir)

#  [1] 마야 경로
maya_scripts_dir = Path.home() / "OneDrive" / "문서" / "maya" / "2023" / "scripts"
site_packages_dir = maya_scripts_dir / "site-packages"
print(f"[+] Maya scripts dir: {maya_scripts_dir}")

#  [2] pip로 라이브러리 설치
subprocess.run([
    sys.executable,
    "-m", "pip", "install",
    "-r", str(script_dir / "requirements.txt"),
    "--target", str(site_packages_dir)
])

#  [3] gpclean 소스코드 복사
source_dir = script_dir / "gpclean"
shutil.copytree(source_dir, maya_scripts_dir / "gpclean", dirs_exist_ok=True)

#  [4] userSetup.py 복사
shutil.copy(script_dir / "userSetup.py", maya_scripts_dir / "userSetup.py")

print("[] 마야 설치 완료! 마야를 실행하면 gpclean이 자동 로드됩니다.")

# Blender 설치 경로의 내장 Python 경로 지정 (🧠 너 경로 맞게 수정해)
blender_python_exe = Path("C:/Program Files/Blender Foundation/Blender 4.2/4.2/python/bin/python.exe")
blender_site_packages = Path("C:/Program Files/Blender Foundation/Blender 4.2/4.2/python/lib/site-packages")

# Blender 사용자 경로
blender_user_path = Path.home() / "AppData" / "Roaming" / "Blender Foundation" / "Blender" / "4.2" / "scripts"
blender_addon_dir = blender_user_path / "addons" / "gpclean"
blender_modules_dir = blender_user_path / "modules" / "site-packages"

# 현재 스크립트 위치
script_dir = Path(__file__).resolve().parent
gpclean_source = script_dir / "gpclean"

# 0. 필요 폴더 생성
blender_addon_dir.mkdir(parents=True, exist_ok=True)
blender_modules_dir.mkdir(parents=True, exist_ok=True)

# 1. 애드온 복사
shutil.copytree(gpclean_source, blender_addon_dir, dirs_exist_ok=True)
print(f"[+] 애드온 복사 완료 → {blender_addon_dir}")

# 2. Blender 내장 Python에 pip 설치 (ensurepip)
subprocess.run([blender_python_exe, "-m", "ensurepip"])
subprocess.run([blender_python_exe, "-m", "pip", "install", "--upgrade", "pip"])

# 3. PySide2 + shiboken2 설치 (Blender 내장 Python 기준)
subprocess.run([
    blender_python_exe,
    "-m", "pip", "install",
    "PySide6==6.6.1",
    "--upgrade",
    "--target", str(blender_modules_dir)
])


# 4. requirements.txt 추가 설치 (옵션)
req_file = script_dir / "requirements.txt"
if req_file.exists():
    subprocess.run([
        blender_python_exe, "-m", "pip", "install",
        "-r", str(req_file),
        "--target", str(blender_site_packages)
    ])


