import os
import sys
import subprocess
from pathlib import Path

# 마야 스크립트 경로 가져오기 (Windows 기준)
maya_scripts_dir = Path.home() / "OneDrive"/ "문서" / "maya" / "2023" /"scripts"
site_packages_dir = maya_scripts_dir / "site-packages"
print(maya_scripts_dir)
# 1. 라이브러리 설치

subprocess.run([
    sys.executable,
    "-m", "pip", "install", "-r", "D:/gitclonetest/gp/requirements.txt",
    "--target", str(site_packages_dir)
])

source_dir = "D:/gitclonetest/gp/gpclean"
# 2. 툴 소스코드 복사
import shutil
shutil.copytree(source_dir, maya_scripts_dir / "gpclean", dirs_exist_ok=True)

# 3. userSetup.py 덮어쓰기
shutil.copy("D:/gitclonetest/gp/userSetup.py", maya_scripts_dir / "userSetup.py")

print("[+] 설치 완료! 마야를 실행하면 gpclean 이 자동 로드됩니다.")

# 🔹 Blender 애드온 파일 복사 (필요 시 버전 수정!)



blender_addon_dir = Path.home() / "AppData" / "Roaming" / "Blender Foundation" / "Blender" / "3.6" / "scripts" / "addons"
addon_file = script_dir / "C:/Users/User/OneDrive/Desktop/gp-clean/gpclean/blender/addon.py.py"  # 너가 만든 애드온 파일명
blender_addon_file_dst = blender_addon_dir / "gpclean_blender_addon.py"

# 디렉토리 없으면 생성
blender_addon_dir.mkdir(parents=True, exist_ok=True)

# 파일 복사
shutil.copy(addon_file, blender_addon_file_dst)
print(f"[+] Blender 애드온 설치 완료 → {blender_addon_file_dst}")
print("[📌] 블렌더 Preferences → Add-ons → 'GP Clean Blender Addon' 검색 후 체크하세요!")