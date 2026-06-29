from ..core.types import SceneInfo, RenderSettings
from ..core.paths import to_unc

class BlenderAdapter:
    def gather_scene_info(self) -> SceneInfo:
        try:
            import bpy  # 지연 임포트
        except Exception as e:
            raise RuntimeError("Blender 환경이 아닙니다.") from e
        scene_path = to_unc(bpy.data.filepath)
        return SceneInfo(dcc="blender", scene_file=scene_path)

    def gather_render_settings(self) -> RenderSettings:
        import bpy
        r = bpy.context.scene.render
        engine = r.engine.lower()  # CYCLES/BLENDER_EEVEE 등
        s = int(bpy.context.scene.frame_start)
        e = int(bpy.context.scene.frame_end)
        step = int(bpy.context.scene.frame_step) or 1
        outdir = to_unc(bpy.path.abspath(r.filepath))
        ext = (r.file_extension or ".exr").lstrip(".")
        return RenderSettings(renderer=engine, version=str(bpy.app.version_string),
                              frame_start=s, frame_end=e, frame_step=step,
                              image_prefix="<Scene>/<Camera>", output_ext=ext, output_dir=outdir)

    def validate(self) -> None:
        # 필요시 Cycles/Device 체크 추가
        return
