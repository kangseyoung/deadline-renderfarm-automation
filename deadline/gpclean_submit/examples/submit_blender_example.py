# Blender 텍스트 에디터에서 실행 예시
# import sys; sys.path.append(r"C:/path/to/your/package")  # 필요 시
from gpclean_submit.cli import submit_job

ok, out, err = submit_job("blender", name="Shot01_Render_Test")
print("OK:", ok)
print(out)
print(err)
