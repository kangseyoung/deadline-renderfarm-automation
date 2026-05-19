from .types import SceneInfo, RenderSettings

class PreflightError(RuntimeError):
    pass

def run_common_checks(scene: SceneInfo, rend: RenderSettings):
    # 최소 검증: 씬 경로, 출력 디렉토리, 프레임 범위
    if not scene.scene_file:
        raise PreflightError("씬 파일 경로가 비어 있습니다. NAS 경로로 저장 후 제출하세요.")
    if rend.frame_end < rend.frame_start:
        raise PreflightError("프레임 범위가 올바르지 않습니다.")
    # 추가 체크는 프로젝트 환경에 맞게 확장하세요.
    return True
