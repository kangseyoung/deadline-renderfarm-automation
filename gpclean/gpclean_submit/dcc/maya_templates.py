# Maya 전용 plugin_info 확장 포인트 예시
# 필요시 AOV, 렌더 레이어 옵션 등 추가 필드 구성
def add_maya_specifics(lines: list, options: dict) -> None:
    # lines.append("UseLegacyRenderLayers=true")  # 예시
    # lines.append(f"RenderLayer={options.get('layer')}")
    return
