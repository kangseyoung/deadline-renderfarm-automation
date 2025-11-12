import os

def to_unc(p: str) -> str:
    if not p:
        return p
    return p.replace("\\", "/")

def safe_join(dir_, prefix, ext):
    # 토큰은 실제 렌더러/Deadline에서 해석되도록 남겨둠
    prefix = prefix.replace("/", os.sep)
    return os.path.join(dir_, prefix) + "." + ext

def decide_output_ext(renderer: str, default_ext="exr"):
    if not renderer:
        return default_ext
    r = renderer.lower()
    if r in ("arnold", "mtoa", "cycles"):
        return "exr"
    return default_ext
