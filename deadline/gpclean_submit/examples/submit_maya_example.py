# Maya Script Editor에서 실행 예시
# import sys; sys.path.append(r"C:/path/to/your/package")  # 필요 시
from gpclean_submit.cli import submit_job

# 씬/프로젝트가 NAS 경로에 있고, mtoa 등 플러그인 준비가 되어 있어야 함
ok, out, err = submit_job("maya", name="Shot01_Lighting_Test")
print("OK:", ok)
print(out)
print(err)
